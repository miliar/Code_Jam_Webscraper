//#include "InfInt/InfInt.cpp"
#include <bits/stdc++.h>
/*#include <iostream>
#include <iostream>
#include <stdlib.h>
#include <stdio.h>
#include <map>
#include <algorithm>
#include <math.h>
#include <iostream>
#include <string>
#include <sstream>
#include <cmath>*/

using namespace std;
//std::map <int, long> cache;
char keys[100], word[100], cur[100];
int K, L, S;
long total, maxm, cnt;
int keysl, wordl;

int countSubstring( char *str, char *sub)
{
    int length = strlen(sub);
    if (length == 0) return 0;
    int count = 0;
    char *pos = str;

    while (1) {
        pos = strstr(pos, sub);
        if (pos == NULL) break;
        pos++;
        ++count;
    }

    return count;
}

void mx(int pos) {
    if (pos == S) {
        cur[pos] = 0;
        //cout << cur << endl;
        int tmp = countSubstring(cur, word);
        /*if (tmp > 0) {
            cout << cur << " ";
            cout << tmp << endl ;
        }*/
        if (tmp > maxm) maxm = tmp;
        cnt += tmp;
        total++;
        return;
    } else {
        for (int i=0; i<keysl; i++) {
            cur[pos] = keys[i];
            mx(pos + 1);
        }
    }
}


double solve() {
    cin >> K >> L >> S;
    cin >> keys;
    cin >> word;

    keysl = strlen(keys);
    wordl = strlen(word);

    total = 0;
    maxm = 0;
    cnt = 0;

    mx(0);

    double pay = 1.0 * cnt / total;



    /*cout << "Total " << total << endl;
    cout << "cnt " << cnt << endl;
    cout << "Pay " << pay << endl;
    cout << "Maxm " << maxm << endl;*/


    return 1.0*maxm - pay;

}

int main()
{
    //precalc();
    //cout << rev(99989);
    //return 0;
    //freopen("A.in", "r", stdin);
    //freopen("A.in", "r", stdin);
    freopen("B-small-attempt3.in", "r", stdin);
   	freopen("out.txt", "w", stdout);
    int cases = 123;
    //scanf("%d", &cases);
    cin >> cases;
    cout << std::setprecision( 7 );
    //cout << "CASES " << cases << endl;
    for (int c=0; c < cases; c++) {
         cout << "Case #" << (c + 1) << ": " << solve() << endl;
//         return 0;
    }

    return 0;
}
