#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
using namespace std;


void print_lawn(std::vector<std::vector<int> > &lawn) {
    for (int i=0; i<lawn.size(); i++) {
        for (int j=0; j<lawn[i].size(); j++)
            cout << lawn[i][j];
        cout << endl;
    }
}


bool reduce(std::vector<std::vector<int> > &lawn, int height) {

    // remove rows
    std::vector<int> removable_rows;
    for (int i=0; i<lawn.size(); i++) {
        bool can_reduce = true;
        for (int j=0; j<lawn[i].size(); j++)
            if (lawn[i][j] != height) can_reduce = false;
        if (can_reduce) removable_rows.push_back(i);
    }

    for (std::vector<int>::reverse_iterator ri = removable_rows.rbegin(); ri != removable_rows.rend(); ++ri)
        lawn.erase(lawn.begin() + *ri);

   // remove columns
    std::vector<int> removable_columns;
    for (int j=0; j<lawn[0].size(); j++) {
        bool can_reduce = true;
        for (int i=0; i<lawn.size(); i++)
            if (lawn[i][j] != height) can_reduce = false;
        if (can_reduce) removable_columns.push_back(j);
    }

    for (int i=0; i<lawn.size(); i++)
        for (std::vector<int>::reverse_iterator ri = removable_columns.rbegin(); ri != removable_columns.rend(); ++ri)
            lawn[i].erase(lawn[i].begin() + *ri);

    for (int i=0; i<lawn.size(); i++)
        for (int j=0; j<lawn[i].size(); j++)
            if (lawn[i][j] == height) return false;

    return true;
}


int main(int argc, char **argv) {

    ifstream testf(argv[1]);
    string line;
    stringstream linestream;
    int num_tests;

    getline(testf, line);
    linestream.str(line);
    linestream >> num_tests;

    int n,m;
    for (int t=0; t<num_tests; t++) {
        getline(testf, line);
        linestream.clear();
        linestream.str(line);
        linestream >> n >> m;

        std::vector<std::vector<int> > lawn(n);
        for (int i=0; i<n; i++) lawn[i].resize(m);

        for (int i=0; i<lawn.size(); i++) {
            getline(testf, line);
            linestream.clear();
            linestream.str(line);
            for (int j=0; j<lawn[i].size(); j++)
                linestream >> lawn[i][j];
        }

        int height = 1;
        while (true) {
            bool success = reduce(lawn, height);
            if (!success) {
                std::cout << "Case #" << t+1 << ": NO" << endl;
                break;
            }
            if (lawn.size() == 0) {
                std::cout << "Case #" << t+1 << ": YES" << endl;
                break;
            }
            height += 1;
        }

    }

    return 0;
}

