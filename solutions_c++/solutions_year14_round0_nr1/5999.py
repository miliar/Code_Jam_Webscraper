/* 
 * File:   magic_trick.cc
 * Author: vivek
 *
 * Created on April 12, 2014, 6:31 AM
 */

#include <cstdlib>

#include <iostream>
#include <cstdio>


#include <vector>
#include <set>
#include <algorithm>
#include <map>

#include <cmath>



using namespace std;

/*
 * 
 */
#define SIZE 4

vector<int> read_ith_row(int row) {
    vector<int> m;
    for (int i = 0; i < SIZE; i++) {
        for (int j = 0; j < SIZE; j++) {
            int temp;
            cin >> temp;
            if (i + 1 == row) {
                m.push_back(temp);
            }
        }

    }
    std::sort(m.begin(), m.end());
    return m;
}

int main(int argc, char** argv) {
    int t;
    cin >> t;

    for (int i = 1; i <= t; i++) {
        int answer_1, answer_2;
        vector<int> row_of_answer_1, row_of_answer_2;

        cin >> answer_1;
        row_of_answer_1 = read_ith_row(answer_1);

        cin >> answer_2;
        row_of_answer_2 = read_ith_row(answer_2);

        vector<int> ans;

        std::set_intersection(row_of_answer_1.begin(), row_of_answer_1.end(), row_of_answer_2.begin(), row_of_answer_2.end(),  std::back_inserter(ans));

        cout << "Case #" << i << ": " ;
        if (ans.size() == 0) {
            cout << "Volunteer cheated!";
        } else if (ans.size() > 1) {
            cout << "Bad magician!";
        } else {
            cout << ans.at(0);
        }
        cout << endl;


    }


    return 0;
}

