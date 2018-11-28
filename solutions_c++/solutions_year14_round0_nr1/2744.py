//
//  main.cpp
//  Magic Trick
//
//  Created by lmotorin on 4/12/14.
//  Copyright (c) 2014 Lior. All rights reserved.
//

#include <iostream>
using namespace std;
#define N 4
int main(int argc, const char * argv[])
{

    size_t tc = 0 , tc_i = 0;
    cin >> tc;
    
    for (tc_i=1;tc_i<=tc;++tc_i)
    {
        int count_cards[N*N+1] = {0};
        int first_board[N][N] = {0};
        int second_board[N][N] = {0};
        int i = 0 , j = 0;
        int first_row = 0;
        int second_row = 0;
        
        cin >> first_row;
        first_row--;
        
        for (i=0;i<N;++i)
        {
            for (j=0;j<N;++j)
            {
                cin >> first_board[i][j];
            }
        }
        
        // Do first row processing
        for (j=0;j<N;++j)
        {
            count_cards[first_board[first_row][j]]++;
        }
        
        cin >> second_row;
        second_row--;
        
        for (i=0;i<N;++i)
        {
            for (j=0;j<N;++j)
            {
                cin >> second_board[i][j];
            }
        }
        
        // Do Second row processing
        int number_of_matches = 0;
        int number = -1;
        for (j=0;j<N;++j)
        {
            if (count_cards[second_board[second_row][j]]>0)
            {
                number_of_matches++;
                number = second_board[second_row][j];
            }
        }
        
        if (number_of_matches == 1)
        {
            cout << "Case #" << tc_i <<": " << number << endl;
        }
        else if (number_of_matches == 0)
        {
            cout << "Case #" << tc_i <<": Volunteer cheated!" << endl;
        }
        else
        {
            cout << "Case #" << tc_i <<": Bad magician!" << endl;
        }
        
        
        
    }
    return 0;
}

