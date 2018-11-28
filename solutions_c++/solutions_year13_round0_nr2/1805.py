#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <list>
using namespace std;

#define WIN32_LEAN_AND_MEAN
#undef UNICODE
#include <windows.h>

size_t listFiles(const string &dir, const string &prefix, const string &sufix, list<string> *files);

int main(int argc, char **args)
{
    string dir = "./";
    list<string> files;
    if (listFiles(dir, "B-", ".in", &files) == 0)
        return -2;

    for (list<string>::iterator fileIte = files.begin(); fileIte != files.end(); ++fileIte)
    {
        ifstream input((dir + *fileIte).c_str());
        ofstream output((dir + fileIte->substr(0, fileIte->find('.')) + ".out").c_str());

        int numCases;
        input >> numCases;
        for (int caseNum = 0; caseNum < numCases; ++ caseNum)
        {
        	int n, m;
        	input >> n;
        	input >> m;

        	int **lawn = new int*[n];

        	int *maxPerRow = new int[n];
        	memset(maxPerRow, 0, sizeof(int) * n);
        	int *maxPerCol = new int[m];
        	memset(maxPerCol, 0, sizeof(int) * m);

			for (int i = 0; i < n; i++) {
				lawn[i] = new int[m];

				for (int j = 0; j < m; j++) {
					int &height = lawn[i][j];
					input >> height;

					if (height > maxPerRow[i])
						maxPerRow[i] = height;
					if (height > maxPerCol[j])
						maxPerCol[j] = height;
				}
			}

			bool impossible = false;
			for (int i = 0; i < n && !impossible; i++) {
				for (int j = 0; j < m; j++) {
					int &height = lawn[i][j];

					if (height < maxPerRow[i] && height < maxPerCol[j]) {
						impossible = true;
						break;
					}
				}
			}

//			printf("\n");
			for (int i = 0; i < n; ++i) {
//				for (int j = 0; j < m; j++)
//					printf("%d", lawn[i][j]);
//				printf("\n");
			    delete[] lawn[i];
			}
//			printf("\n");
			delete[] lawn;
			delete[] maxPerRow;
			delete[] maxPerCol;

            string result = (impossible ? "NO" : "YES");

            stringstream caseResult;
            caseResult << "Case #" << caseNum + 1 << ": " << result;
            output << caseResult.str() << endl;
            cout << caseResult.str() << endl;
        }
    }

    return 0;
}

size_t listFiles(const string &dir, const string &prefix, const string &sufix, list<string> *files)
{
    files->clear();

    string fileMask = dir + "\\" + prefix + "*" + sufix;
    WIN32_FIND_DATA info;
    HANDLE hFind = FindFirstFile(fileMask.c_str(), &info);
    if (hFind != INVALID_HANDLE_VALUE)
    {
        do
        {
            if (strlen(info.cFileName) > 0)
                files->push_back(info.cFileName);
        } while (FindNextFile(hFind, &info));

        FindClose(hFind);
    }

    return files->size();
}
