/* 
 * File: main.cpp
 * Copyright © Jan Škoda
 */

#include <cstdlib>
#include <iostream>
#include <cstdio>
#include <cassert>
#include <string>
#include <stack>
#include <vector>
#include <algorithm>


using namespace std;

#define MAX_L 10001

auto multi = new char[255][255]();
auto divid = new char[255][255]();

void init_tables() { // -1 = M; -i = I; -j = J; -k = K.
    multi['1']['1'] = '1';
    multi['1']['i'] = 'i';
    multi['1']['j'] = 'j';
    multi['1']['k'] = 'k';
    multi['1']['M'] = 'M';
    multi['1']['I'] = 'I';
    multi['1']['J'] = 'J';
    multi['1']['K'] = 'K';    
    
    multi['i']['1'] = 'i';
    multi['i']['i'] = 'M';
    multi['i']['j'] = 'k';
    multi['i']['k'] = 'J';
    multi['i']['M'] = 'I';
    multi['i']['I'] = '1';
    multi['i']['J'] = 'K';
    multi['i']['K'] = 'j';    

    multi['j']['1'] = 'j';
    multi['j']['i'] = 'K';
    multi['j']['j'] = 'M';
    multi['j']['k'] = 'i';
    multi['j']['M'] = 'J';
    multi['j']['I'] = 'k';
    multi['j']['J'] = '1';
    multi['j']['K'] = 'I';    

    multi['k']['1'] = 'k';
    multi['k']['i'] = 'j';
    multi['k']['j'] = 'I';
    multi['k']['k'] = 'M';  
    multi['k']['M'] = 'K';
    multi['k']['I'] = 'J';
    multi['k']['J'] = 'i';
    multi['k']['K'] = '1';     
    
    multi['M']['1'] = 'M';
    multi['M']['i'] = 'I';
    multi['M']['j'] = 'J';
    multi['M']['k'] = 'K';
    multi['M']['M'] = '1';
    multi['M']['I'] = 'i';
    multi['M']['J'] = 'j';
    multi['M']['K'] = 'k';    
    
    multi['I']['1'] = 'I';
    multi['I']['i'] = '1';
    multi['I']['j'] = 'K';
    multi['I']['k'] = 'j';
    multi['I']['M'] = 'i';
    multi['I']['I'] = 'M';
    multi['I']['J'] = 'k';
    multi['I']['K'] = 'J';    

    multi['J']['1'] = 'J';
    multi['J']['i'] = 'k';
    multi['J']['j'] = '1';
    multi['J']['k'] = 'I';
    multi['J']['M'] = 'j';
    multi['J']['I'] = 'K';
    multi['J']['J'] = 'M';
    multi['J']['K'] = 'i';    

    multi['K']['1'] = 'K';
    multi['K']['i'] = 'J';
    multi['K']['j'] = 'i';
    multi['K']['k'] = '1';    
    multi['K']['M'] = 'k';
    multi['K']['I'] = 'j';
    multi['K']['J'] = 'I';
    multi['K']['K'] = 'M';
    
    // divid
    auto symbols = {'1','i','j','k','M','I','J','L'};
    for (char sym1 : symbols) {
        for (char sym2 : symbols) {
            char sym3 = multi[sym1][sym2];
            divid[sym1][sym3] = sym2;
        }
    }
    
}

auto cache = new char[MAX_L][255]; ///!< indexy: odkud-znak; hodnota: delka posloupnosti

void clear_cache() {
    for (int i = 0; i < MAX_L; i++) {
        for (int j = 0; j < 255; j++) {
            cache[i][j] = 0;
        }
    }
}

/**
 * 
 * @param str vstupni retezec
 * @param x kolikrat se str opakuje
 * @param ch hledany znak
 * @param start_i odkud zacit nasobit
 * @return index stop_i konce posloupnosti od start_i, ktery po soucinu dela ch nebo -1
 */
int find_char(string str, int x, char goal_c, int start_i) {
    //Pri nasobeni postupne ukladat mezivysledky do cache
    int i = start_i % str.size();
    int cached_steps = cache[i][goal_c];
    if (cached_steps != 0) {
        int end_i = start_i + cached_steps -1;
        if (end_i < x * str.size())
            return end_i;
        else 
            return -1;
    }
    
    char ch = str[i];
    int steps = 0;
    char orig[MAX_L];
    for (int i = 0; i < MAX_L; i++) {
        orig[i] = 0;
    }

    while (ch != goal_c) {
        i++; i%=str.size(); steps++;
        char ch2 = str[i];
        ch = multi[ch][ch2];
        if (orig[i]==0)
            orig[i] = ch;
        else if ((ch == orig[i]) && (ch != goal_c)) { //Loop
            return -1;
        }
    }
    cache[start_i % str.size()][goal_c] = steps + 1;
    int end_i = start_i + steps;
    if (end_i < x * str.size())
        return end_i;
    else
        return -1;   
}

char mul(string str, int begin, int end) { //including end
    char ch = str[begin%str.size()];
    for (int i = begin+1; i <= end; i++) {
        char ch2 = str[i%str.size()];
        ch = multi[ch][ch2];
    }
    return ch;
}

vector<int> idxs;
bool recurse(string str, int x, char goal1, char goal2, char goal3, int start_i) {
    if (goal1 == 0) {
        if (start_i == str.size()*x) {
#if 0
            //output idxs
            for (int i : idxs) 
                cout << i << ",";
            cout << endl;
            //check
            int start = 0;
            for (int i : idxs) {
                cout << mul(str,start,i) << ",";
                start = i+1;
            }
            cout << endl;
#endif
            
            return true;
        } else 
            return false;
    }
    int end_i = start_i-1;
    char state = '1';
    while (true) {
        char d = divid[state][goal1];
        end_i = find_char(str, x, divid[state][goal1], end_i + 1);
        state = goal1;
        if (end_i == -1) {
            return false;
        }
        idxs.push_back(end_i); //Kde to konci
        bool possible = recurse(str, x, goal2, goal3, 0, end_i + 1);
        idxs.pop_back();
        if (possible)
            return possible;        
    }
}

bool dumb(string str, int x, char goal1, char goal2, char goal3, int start_i) {
    int len = str.size()*x;
    int ss = str.size();
    for (int i = 0; i < len - 1; i++) {
        char ch = str[0];
        for (int k = 1; k < i; k++) {
            ch = multi[ch][str[k % ss]];
        }
        if (ch != 'i')
            continue;
        for (int j = i+1; j < len; j++) {
            char ch = str[i % ss];
            for (int k = i+1; k < j; k++) {
                ch = multi[ch][str[k % ss]];
            }
            if (ch != 'j')
                continue;
            ch = str[j % ss];
            for (int k = j+1; k < len; k++) {
                ch = multi[ch][str[k % ss]];
            }
            if (ch != 'k')
                continue;
            return true;
        }
    }
    return false;    
}

int main(int argc, char** argv) {
    init_tables();
    int N;
    cin >> N;
    for (int i = 1; i <= N; i++) {
        int L, X;
        cin >> L >> X;
        string str;
        cin >> str;
        clear_cache();
        
        bool possible = recurse(str, X, 'i', 'j', 'k', 0);
        //bool possible = dumb(str, X, 'i', 'j', 'k', 0);
        //printf("Case #%d: %s (%d %d)\n",i,possible ? "YES":"NO",L,X);        
        printf("Case #%d: %s\n",i,possible ? "YES":"NO");
    }
}

