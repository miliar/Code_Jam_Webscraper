//
//  main.cpp
//  codejam13
//
//  Created by Chang Lan on 4/6/13.
//  Copyright (c) 2013 Chang Lan. All rights reserved.
//

#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <map>
#include <string>

using namespace std;


inline bool iszero(int arr[100][100], int n, int m)
{
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            if (arr[i][j] != 0) {
                return false;
            }
        }
    }
    return true;
}

void lawnmower(int case_num)
{
    int n, m;
    cin >> n >> m;
    int lawn[100][100];
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            cin >> lawn[i][j];
        }
    }
    // row max
    int row_max[100];
    for (int i = 0; i < n; ++i) {
        row_max[i] = 1;
        for (int j = 0; j < m; ++j) {
            row_max[i] = (row_max[i] > lawn[i][j]) ? row_max[i] : lawn[i][j];
        }
    }
    // col max
    int col_max[100];
    for (int j = 0; j < m; ++j) {
        col_max[j] = 1;
        for (int i = 0; i < n; ++i) {
            col_max[j] = (col_max[j] > lawn[i][j]) ? col_max[j] : lawn[i][j];
        }
    }
    
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            if (lawn[i][j] < row_max[i] && lawn[i][j] < col_max[j]) {
                std::cout << "Case #" << case_num << ": " << "NO" << endl;
                return;
            }
        }
    }
    
    std::cout << "Case #" << case_num << ": " << "YES" << endl;
    return;
    
}

inline bool check(char state[4][5], char symbol, int start_x, int start_y)
{
    int count;
    
    // horizonal
    count = 0;
    for (int i = start_y + 1; i < 4; ++i) {
        if (state[start_x][i] == symbol || state[start_x][i] == 'T')
            ++count;
        else
            break;
    }
    if (count >= 3) {
        return true;
    }
    
    // vertical
    count = 0;
    for (int i = start_x + 1; i < 4; ++i) {
        if (state[i][start_y] == symbol || state[i][start_y] == 'T')
            ++count;
        else
            break;
    }
    if (count >= 3) {
        return true;
    }
    
    // diagonal '\'
    count = 0;
    int i, j;
    for (i = start_x + 1, j = start_y + 1;
         i < 4 && j < 4; ++i, ++j) {
        if (state[i][j] == symbol || state[i][j] == 'T')
            ++count;
        else
            break;
    }
    if (count >= 3) {
        return true;
    }
    
    // diagonal '/'
    count = 0;
    for (i = start_x + 1, j = start_y - 1;
         i < 4 && j >= 0; ++i, --j) {
        if (state[i][j] == symbol || state[i][j] == 'T')
            ++count;
        else
            break;
    }
    if (count >= 3) {
        return true;
    }
    
    return false;
}

void tictattoetomek(int case_num)
{
    char state[4][5] = {0};
    for (int i = 0; i < 4; ++i) {
        cin >> state[i];
    }
    
    bool completed = true;
    
    for (int i = 0; i < 4; ++i) {
        for (int j = 0; j < 4; ++j) {
            switch (state[i][j]) {
                case 'X':
                    if (check(state, 'X', i, j)) {
                        std::cout << "Case #" << case_num << ": " << "X won" << endl;
                        goto finished_tttt;
                    }
                    break;
                case 'O':
                    if (check(state, 'O', i, j)) {
                        std::cout << "Case #" << case_num << ": " << "O won" << endl;
                        goto finished_tttt;
                    }
                    break;
                case 'T':
                    if (check(state, 'X', i, j)) {
                        std::cout << "Case #" << case_num << ": " << "X won" << endl;
                        goto finished_tttt;
                    }
                    
                    if (check(state, 'O', i, j)) {
                        std::cout << "Case #" << case_num << ": " << "O won" << endl;
                        goto finished_tttt;
                    }
                    
                    break;
                case '.':
                    completed = false;
                    break;
                default:
                    break;
            }
        }
    }
    if (completed) {
        std::cout << "Case #" << case_num << ": " << "Draw" << endl;
    } else {
        std::cout << "Case #" << case_num << ": " << "Game has not completed" << endl;
    }
    
finished_tttt:
    return;
}

void reversewords(int case_num)
{
    std::string words;
    getline(cin, words);
    string::iterator start;
    string::iterator it = start = words.begin();
    
    for (;;) {
        if (it == words.end()) {
            reverse(start, it);
            break;
        } else if (*it == ' ') {
            reverse(start, it);
            start = it + 1;
        }
        ++it;
    }
    
    reverse(words.begin(), words.end());
    
    std::cout << "Case #" << case_num << ": " << words << endl;
    
}

void storecredit(int case_num)
{
    int credit, n;
    std::cin >> credit >> n;
    std::map<int, int> items;
    for (int i = 0; i < n; ++i) {
        int val;
        std::cin >> val;
        if (items.find(credit - val) != items.end()) {
            std::cout << "Case #" << case_num << ": " << items[credit-val] << " " << i+1 << std::endl;
        }
        items[val] = i+1;
    }
}

int main(int argc, const char * argv[])
{
    freopen("B-large-0.in", "r", stdin);
    freopen("B-large-0.out", "w", stdout);
    int case_num;
    string nonsense;
    std::cin >> case_num;
    //getline(cin, nonsense);
    for (int i = 0; i < case_num; ++i) {
        lawnmower(i+1);
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}


