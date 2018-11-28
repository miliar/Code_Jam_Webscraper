/*Author:@abs51295*/
#include <bits/stdc++.h>
#include<fstream>
#define fr freopen("A-large.in","r",stdin)
#define fw freopen("A-large.out","w",stdout)
#define iOs ios_base::sync_with_stdio(false);
#define INF 1000000009
#define MOD 1000000007
#define all(x) (x).begin(), (x).end()
using namespace std;
typedef long long ll;
typedef long double ld;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<vi> vvi;

main(){

        fw;fr;

    iOs;
    int t,j=1; cin >> t;
    string s;
    while(t--){
        string v;
        string::iterator it;
        cin >> s;
        v+=s[0];
        for(int i=1;i<s.length();i++){
            if(s[i]>=v[0]){
                it=v.begin();
                v.insert(it,s[i]);
            }
            else{
                v.push_back(s[i]);
            }
        }
        cout << "Case #" << j++ << ": " << v << endl;
    }
}
