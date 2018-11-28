#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
using namespace std;

typedef long long LL;
#define rep(it,s) for(__typeof((s).begin()) it=(s).begin();it!=(s).end();it++)

bool done[2010];
int n;
string s;

string numbers[] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE" };
int total[10];

int getCount(char c) {
    int tot = 0;
    for (int i=0; i<n; i++) if (!done[i] && s[i]==c)
        tot++;

    return tot;

}

map<char,int> cnt;

int main() {

    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    int t;
    cin>>t;
    for (int c=0; c<t; c++) {

        cin>>s;
        n = s.length();
        for (int i=0; i<n; i++) done[i] = 0;
        for (int i=0; i<10; i++) total[i] = 0;

        //zeros
        int tot = getCount('Z');
        total[0] = tot;

        cnt.clear();
        for (int i=0; i<numbers[0].length(); i++) cnt[numbers[0][i]] = tot;

        for (int i=0; i<n; i++) if (!done[i] && cnt[s[i]]>0) {
            cnt[s[i]]--;
            done[i] = 1;
        }

        //two
        tot = getCount('W');
        total[2] = tot;

        for (int i=0; i<numbers[2].length(); i++) cnt[numbers[2][i]] = tot;

        for (int i=0; i<n; i++) if (!done[i] && cnt[s[i]]>0) {
            cnt[s[i]]--;
            done[i] = 1;
        }

        //four
        tot = getCount('U');
        total[4] = tot;

        for (int i=0; i<numbers[2].length(); i++) cnt[numbers[4][i]] = tot;

        for (int i=0; i<n; i++) if (!done[i] && cnt[s[i]]>0) {
            cnt[s[i]]--;
            done[i] = 1;
        }

        //siz
        tot = getCount('X');
        total[6] = tot;

        for (int i=0; i<numbers[6].length(); i++) cnt[numbers[6][i]] = tot;

        for (int i=0; i<n; i++) if (!done[i] && cnt[s[i]]>0) {
            cnt[s[i]]--;
            done[i] = 1;
        }

        //eight
        tot = getCount('G');
        total[8] = tot;

        for (int i=0; i<numbers[8].length(); i++) cnt[numbers[8][i]] = tot;

        for (int i=0; i<n; i++) if (!done[i] && cnt[s[i]]>0) {
            cnt[s[i]]--;
            done[i] = 1;
        }

        //seven
        tot = getCount('S');
        total[7] = tot;

        for (int i=0; i<numbers[7].length(); i++) cnt[numbers[7][i]] = tot;

        for (int i=0; i<n; i++) if (!done[i] && cnt[s[i]]>0) {
            cnt[s[i]]--;
            done[i] = 1;
        }

        //five
        tot = getCount('V');
        total[5] = tot;

        for (int i=0; i<numbers[5].length(); i++) cnt[numbers[5][i]] = tot;

        for (int i=0; i<n; i++) if (!done[i] && cnt[s[i]]>0) {
            cnt[s[i]]--;
            done[i] = 1;
        }

        //one
        tot = getCount('O');
        total[1] = tot;

        for (int i=0; i<numbers[1].length(); i++) cnt[numbers[1][i]] = tot;

        for (int i=0; i<n; i++) if (!done[i] && cnt[s[i]]>0) {
            cnt[s[i]]--;
            done[i] = 1;
        }

         //nine
        tot = getCount('N');
        total[9] = tot/2;

        for (int i=0; i<numbers[9].length(); i++) cnt[numbers[9][i]] = tot/2;

        for (int i=0; i<n; i++) if (!done[i] && cnt[s[9]]>0) {
            cnt[s[i]]--;
            done[i] = 1;
        }

         //three
        tot = getCount('T');
        total[3] = tot;

        for (int i=0; i<numbers[3].length(); i++) cnt[numbers[3][i]] = tot;

        for (int i=0; i<n; i++) if (!done[i] && cnt[s[9]]>0) {
            cnt[s[i]]--;
            done[i] = 1;
        }

        cout<<"Case #"<<c+1<<": ";
        for (int i=0; i<10; i++) {
            for (int j=0; j<total[i]; j++) cout<<i;
        }
        cout<<endl;

    }

    return 0;

}
