/* Trân Vu Lâm */
/*             */
/*             */
#include <algorithm>
#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <string>
#include <vector>
#include <deque>
#include <cstring>
#include <set>
#include <math.h>
#include <map>
#include <stack>
#include <queue>

#define ii pair<int, int>
#define si pair<string, int>
#define is pair<int, string>

#define mp make_pair
#define foreach(it, ar) for ( typeof(ar.begin()) it = ar.begin(); it != ar.end(); it++ )
#define fill(ar, val) memset(ar, val, sizeof(ar))
#define pbp(a,b) push_back(make_pair(a,b))
#define insp(a,b) insert(make_pair(a,b))
#define pb(a) push_back(a)
#define ins(a) insert(a)

#define uint64 unsigned long long
#define int64 long long

#define INF 1071071071
#define Pr 9875321
#define pi 3.1415926535897932384626433832795
#define eps 1e-8
#define maxN 100005

using namespace std;

vector <string> all;

bool lore(string s1, string s2) {
    if (s1.size() != s2.size())
        return s1.size() < s2.size();
    for (int i = 0; i < s1.size(); i++)
        if (s1[i] > s2[i])
            return false;
        else if (s1[i] < s2[i])
            return true;
    return true;
}
bool le(string s1, string s2) {
    //cout<<s1<< " "<<s2<<endl;
    if (s1.size() != s2.size())
        return s1.size() < s2.size();
    for (int i = 0; i < s1.size(); i++)
        if (s1[i] < s2[i]) return true;
        else if (s1[i] > s2[i])
                return false;
    return false;
}
int main(void) {
    //freopen("C-small-attempt2.in", "r", stdin);
    //freopen("ans.out", "w", stdout);
    all.pb("1");
    all.pb("4");
    all.pb("9");
    all.pb("121");
    all.pb("484");
    all.pb("12321");
    all.pb("14641");
    all.pb("44944");
    all.pb("1234321");
    all.pb("121242121");
    all.pb("123454321");
    all.pb("125686521");
    all.pb("12102420121");
    all.pb("12345654321");
    all.pb("1210024200121");
    all.pb("1212225222121");
    all.pb("1214428244121");
    all.pb("1232346432321");
    all.pb("1234567654321");
    all.pb("121000242000121");
    all.pb("121242363242121");
    all.pb("123212464212321");
    all.pb("123456787654321");
    all.pb("12100002420000121");
    all.pb("12102202520220121");
    all.pb("12104402820440121");
    all.pb("12122232623222121");
    all.pb("12124434743442121");
    all.pb("12321024642012321");
    all.pb("12323244744232321");
    all.pb("12343456865434321");
    all.pb("12345678987654321");
    all.pb("1210000024200000121");
    all.pb("1210242036302420121");
    all.pb("1212203226223022121");
    all.pb("1212445458545442121");
    all.pb("1232100246420012321");
    all.pb("1232344458544432321");
    all.pb("1234323468643234321");
    int n, len = all.size();
    cin>>n;
    for (int tcNo = 1; tcNo <= n; tcNo++) {
        string a, b;
        cin>>a>>b;
        int fa = 0, fb = 0;
        while (fa < len && le(all[fa], a)) fa++;
        while (fb < len && lore(all[fb], b)) fb++;
        //cout<<a<<" "<<b<<" "<<fb<<" "<<fa<<endl;
        printf("Case #%d: %d\n", tcNo, fb - fa);
    }

    return 0;
}
