/*Author:@abs51295*/
#include <bits/stdc++.h>
#include<fstream>
#define fr freopen("B-large.in","r",stdin)
#define fw freopen("B-large.out","w",stdout)
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

bool string_same(const string& s) {
    return s.find_first_not_of('+') == string::npos;
}

main(){

        fw;fr;

    iOs;
    int t,j=1; cin >> t;
    while(t--){
        int step=0;
        string s; cin >> s;
    while(!string_same(s)){
        if(s[0]=='-'){
            int pos = s.find_last_of('-');
            //cout << pos << endl;
            for(int i=0;i<=pos;i++){
                if(s[i]=='+'){
                    s[i]='-';
                }
                else{
                    s[i]='+';
                }
            }
            reverse(s.begin(),s.begin()+pos+1);
            //cout << s << endl;
            step++;
        }
        else{
            for(int i=0;i<s.length();i++){
                if(s[i]=='+'){
                    s[i] = '-';
                }
                else{
                    break;
                }
            }
            //cout << s << endl;
            step++;
        }
    }
    cout << "Case #" << j++ << ": " << step << endl;
    }
}
