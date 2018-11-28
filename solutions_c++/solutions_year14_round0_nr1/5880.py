//
//  main.cpp
//  jam
//
//  Created by shenghua on 4/11/14.
//  Copyright (c) 2014 umich. All rights reserved.
//

#include <iostream>
using namespace std;

int main()
{
    int test_num = 0;
    cin >> test_num;
    int first_row = 0, second_row = 0;
    int first_array[4] = {0};
    int second_array[4]= {0};
    int answer_num = 0;
    int answer = 0;
    int trash;
    
    for (int i = 1; i <= test_num; i++) {
        answer_num = 0;
        int row = 0;
        
        cin >> first_row;
        
        for (row = 1; row <= 4; row++) {
            if (row == first_row) {
                cin >> first_array[0] >> first_array[1] >> first_array[2] >> first_array[3];
                //cout << first_array[0] << first_array[1] <<  first_array[2] << first_array[3] << endl;

            } else {
                cin >> trash >> trash >> trash >> trash;
            }
        }
        
        row = 0;

        cin >> second_row;
        
        for (row = 1; row <= 4; row++) {
            if (row == second_row) {
                cin >> second_array[0] >> second_array[1] >> second_array[2] >> second_array[3];
                //cout << second_array[0] << second_array[1] <<  second_array[2] << second_array[3] << endl;
            } else {
                cin >> trash >> trash >> trash >> trash;
            }
        }
        
        for (int j = 0; j < 4; j++) {
            for (int k = 0; k < 4; k++) {
                if (first_array[j] == second_array[k]) {
                    answer_num++;
                    answer = first_array[j];
                }
            }
        }

        
        if (answer_num == 1) {
            printf("Case #%d: %d\n", i, answer);
        } else if (answer_num > 1) {
            printf("Case #%d: Bad magician!\n", i);
        } else {
            printf("Case #%d: Volunteer cheated!\n", i);
        }
    }
    
    return 0;
}

