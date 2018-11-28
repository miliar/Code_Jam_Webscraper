#include <iostream>
#include <fstream>
#include <queue>
#include <string>
#include <algorithm>

using namespace std;

void readInput(const char *fileName, vector<int> &v) {
	ifstream in_file;
    int nCases, size, size2, nMotes, mote, oper, oper2;
    priority_queue<int, vector<int>, greater<int> > q;

	in_file.open(fileName, ifstream::in);
	if (in_file.fail()) cout << "**Opening file error**" << endl;
	else {
		in_file >> nCases;
		for (int i = 0; i < nCases; i++) {
            in_file >> size;
            in_file >> nMotes;
            oper = 0;
            for (int j = 0; j < nMotes; j++) {
                in_file >> mote;
                q.push(mote);
            }
            while (not q.empty()) {
                if (q.top() < size) {
                    size += q.top();
                    q.pop();
                }
                else if (size == 1) {
                    oper = q.size();
                    while (not q.empty()) q.pop();
                }
                else {
                    size2 = size;
                    oper2 = 0;
                    while (size2 <= q.top()) {
                        size2 += size2 - 1;
                        oper2++;
                    }
                    if (oper2 >= q.size()) {
                        oper += q.size();
                        while (not q.empty()) q.pop();
                    }
                    else {
                        size = size2 + q.top();
                        oper += oper2;
                        q.pop();
                    }
                }
            }
            v.push_back(oper);
            cout<<"Case "<<i<<" done"<<endl;
		}
		in_file.close();
	}
}

void writeOutput(const char *fileName, vector<int> &v) {
	ofstream out_file;

	out_file.open(fileName, ofstream::out);
	if (out_file.fail()) cout << "**Opening file error**" << endl;
	else {
        for (int i = 0; i < v.size(); i++) out_file << "Case #" << i+1 << ": " << v[i] << endl;
		out_file.close();
	}
}

int main()
{
    vector<int> results;

    readInput("A-small.in", results);
    writeOutput("A-small.out", results);
    return 0;
}
