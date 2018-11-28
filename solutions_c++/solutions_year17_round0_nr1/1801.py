
#include <iostream>
#include <fstream>
#include <string>
#include <math.h>
#include <stdlib.h>
#include <vector>
#include <algorithm>
#include <sstream>
#include <deque>

using namespace std;

int flips;



string shrink(string s, int K){
    int len = s.size();
    //cout << s << endl;
    string out = "";
    int flip_count = 0;
    if (s[len-1] == '-'){
        for (int i=len-1; i>len-1-K; i--){
            if (s[i] == '-') s[i] = '+';
            else s[i] = '-';
        }
        flips++;
    }
    //cout << s << endl;
    if (s[0] == '-') {
        for (int i=0; i<K; i++){
            if (s[i] == '-') s[i] = '+';
            else s[i] = '-';
        }

        flips++;
    }
    //cout << s << endl;
    //cout << endl;
    for (int i=1; i<len-1; i++){
        out.push_back(s[i]);
    }
    return out;

}

int main()
{
    int T,K,L;
    int allminus, allplus, finalflip;
    string s;

    cin >> T;
    for (int tc=1; tc <= T; tc++){
        cin >> s >> K;
        flips = 0;
        while (s.size()>K){
            s = shrink(s, K);
        }
        allminus = 1;
        allplus = 1;
        finalflip = 1;
        L = s.size();
        for (int i=0; i<L; i++){
            if (s[i] == '-') allplus = 0;
            if (s[i] == '+') {
                allminus = 0;
                finalflip = 0;
            }
        }
        cout << "Case #" << tc << ": ";
        if (allplus) cout << flips << endl;
        else if (allminus && K==L) cout << flips+1 << endl;
        else cout << "IMPOSSIBLE" << endl;




    }
    return 0;
}
