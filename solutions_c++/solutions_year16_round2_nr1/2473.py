#include <bits/stdc++.h>
#define ll long long int
#define pii pair <int,int>
#define f first
#define s second
#define pi acos(-1.0)
#define pb push_back
using namespace std;

template < class T > inline T gcd(T a, T b) {while(b) {a %= b; swap(a, b);} return a;}
inline int nxt() {int wow; scanf("%d", &wow); return wow;}
inline ll lxt() {ll wow; scanf("%lld", &wow); return wow;}

/***************** Mission Begin *******************/

string str[] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};

int main()
{
    freopen("out.txt", "w", stdout);
    int t, cse = 0;
    cin >> t;
    while (t--){
        string s;
        cin >> s;
    //    cout << s << endl;
        int x = s.length(), hit[202] = {0}, ans[11] = {0};
        for (int i=0; i<x; i++){
            hit[s[i]]++;
        }
    //    cout << hit['Z'] << ' ' << hit['W'] << endl;
        while (hit['Z'] > 0){
            for (int i=0; i<str[0].length(); i++){
                hit[str[0][i]]--;
            }
            ans[0]++;
        }
        while (hit['W'] > 0){
            for (int i=0; i<str[2].length(); i++) hit[str[2][i]]--;
            ans[2]++;
        }
    //      cout << hit['Z'] << ' ' << hit['W'] << endl;

        while (hit['U'] > 0){
            for (int i=0; i<str[4].length(); i++) hit[str[4][i]]--;
            ans[4]++;
      }
      while (hit['R'] > 0){
            for (int i=0; i<str[3].length(); i++) hit[str[3][i]]--;
            ans[3]++;
      }

      while (hit['X'] > 0){
            for (int i=0; i<str[6].length(); i++) hit[str[6][i]]--;
            ans[6]++;
      }
      while (hit['G'] > 0){
            for (int i=0; i<str[8].length(); i++) hit[str[8][i]]--;
            ans[8]++;
      }
      while (hit['O'] > 0){
            for (int i=0; i<str[1].length(); i++) hit[str[1][i]]--;
            ans[1]++;
        }
        while (hit['F'] > 0){
            for (int i=0; i<str[5].length(); i++) hit[str[5][i]]--;
            ans[5]++;
        }
        while (hit['V'] > 0){
            for (int i=0; i<str[7].length(); i++) hit[str[7][i]]--;
            ans[7]++;
        }
        while (hit['I'] > 0){
            for (int i=0; i<str[9].length(); i++) hit[str[9][i]]--;
            ans[9]++;
        }
        printf("Case #%d: ", ++cse);
        for (int i=0; i<10; i++){
            for (int j=0; j<ans[i]; j++) printf("%d", i);
        }
        cout << endl;
    }
    return 0;
}
