#include<iostream>
#include<set>
#include<vector>
#include<algorithm>
using namespace std;




int main() {
    int num_p;
    int row_1;
    int row_2;
    cin >> num_p;
    for(int i = 1; i <= num_p; ++i) {

        vector<vector<int> > board_f;
        cin >> row_1;
        for(int j = 0; j < 4; ++j) {
            vector<int> curr_row;
            for(int k = 0; k < 4; ++k) {
                int next;
                cin >> next;
                curr_row.push_back(next);

            }
            board_f.push_back(curr_row);
        }
        vector<vector<int> > board_s;
        cin >> row_2;
        for(int j = 0; j < 4; ++j) {
            vector<int>  curr_row;
            for(int k = 0; k < 4; ++k) {
                int next;
                cin >> next;
                curr_row.push_back(next);
            }
            board_s.push_back(curr_row);
        }
        vector<int> intersect(4);
        vector<int> s1 = board_f.at(row_1-1);
        std::sort(s1.begin(), s1.end());
        vector<int> s2 = board_s.at(row_2-1);
        std::sort(s2.begin(), s2.end());
        vector<int>::iterator it = std::set_intersection( s1.begin(), s1.end(), s2.begin(), s2.end(),
                               intersect.begin());
        intersect.resize(it - intersect.begin());
        cout << "Case #" << i<< ": ";
        if(intersect.size() == 0) {
            cout << "Volunteer cheated!" << endl;
        } else if(intersect.size() == 1) {
            cout << intersect.at(0) << endl;
        } else {
            cout << "Bad magician!" << endl;
        }

    }

}
