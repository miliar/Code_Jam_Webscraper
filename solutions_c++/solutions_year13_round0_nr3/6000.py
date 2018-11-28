#include <iostream>
#include<fstream>
#include<vector>

using namespace std;


ofstream outfile;

void output(int caseNum, int result) {
    outfile << "Case #" << caseNum << ": " << result << endl;
}

int main()
{
    vector<int> a;
    a.push_back(1);
    a.push_back(4);
    a.push_back(9);
    a.push_back(121);
    a.push_back(484);
    int checked_num = 1000;
    ifstream infile;
    infile.open("C-small-attempt1.in", ifstream::in);
    outfile.open("out.txt", ofstream::out);

    int case_num, from, to;
    int index_from, index_to;
    infile >> case_num;

    for (int i = 1; i <= case_num; i++) {
        infile >> from >> to;
        int count = 0;
        for (vector<int>::iterator it = a.begin(); it != a.end(); it++ ){
            if (*it >= from && *it <= to)
                count++;
        }

        output(i, count);
    }

    return 0;
}
