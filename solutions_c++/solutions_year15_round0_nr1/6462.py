// Monjurul Huda Munna
// Daffodil International University

#include <string>
#include <cstring>
#include <cmath>
#include <map>
#include <deque>
#include <stack>
#include <queue>
#include <vector>
#include <list>
#include <set>
#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <algorithm>

using namespace std;

typedef long long int lld;

#define Max 10000009


int main(){

//    #ifdef munnapagol
//    freopen("input.txt", "r", stdin);
//    freopen("result.txt", "w", stdout);
//    #endif


    int i, j, k, h, test, kase = 0;
    int friend_needed, maxshyness;
    string str;

    cin >> test;
    while(test--){
        cin >> maxshyness >> str;
//        cout << maxshyness << " " << str << endl;
        friend_needed = 0;
        int len_str = str.length();

        int extra_needed, tot_standing = 0;
        for( i=0 ; i<len_str ; i++ ){
            if( tot_standing < i ){
                extra_needed = i - tot_standing;
                tot_standing += extra_needed;
                friend_needed += extra_needed;
            }

            tot_standing += (str[i] - '0') ;
        }

        cout << "Case #" << ++kase << ": " << friend_needed << endl;

    }



    return 0;
}

