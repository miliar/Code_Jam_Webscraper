#include <iostream>
#include <vector>
#include <algorithm>
#include <istream>
#include <fstream>

using namespace std;

int main() {

	ifstream read("input.txt");
	ofstream write("output.txt");
    int T, ans1, ans2;
    int matrix[4][4], matrix1[4][4];
    read>>T;
    for(int i = 0; i < T; i++) {
        read >> ans1;
        for(int j = 0; j < 4; j++) {
            for(int k = 0; k < 4; k++) {
                read >> matrix[j][k];
            }
        }
        read >> ans2;
        for(int j = 0; j < 4; j++) {
            for(int k = 0; k < 4; k++) {
                read >> matrix1[j][k];
            }
        }
        sort(matrix[ans1 - 1], matrix[ans1 - 1] + 4);
        sort(matrix1[ans2 - 1], matrix1[ans2 - 1] + 4);
		vector<int> intersect(4);
        vector<int>::iterator it = set_intersection(matrix[ans1 - 1], matrix[ans1 - 1] + 4, matrix1[ans2 - 1], matrix1[ans2 - 1] + 4, intersect.begin());
        intersect.resize(it - intersect.begin());
        if(intersect.size() == 1) {
            it = intersect.begin();
            write << "Case #" << i + 1 << ": " << *it << endl;
        }
        else if(intersect.size() == 0) {
            write << "Case #" << i + 1 << ": " << "Volunteer cheated!" << endl;
        }
        else if(intersect.size() > 1) {
            write << "Case #" << i + 1 << ": " << "Bad magician!" << endl;
        }
    }
    return 0;
}
