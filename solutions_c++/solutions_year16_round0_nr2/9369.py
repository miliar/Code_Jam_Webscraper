#include <bits/stdc++.h>
#define pb push_back
#define Long long long
using namespace std;

int main() {
   freopen("B-large.in" , "r", stdin);
   freopen("output.txt" , "w" , stdout);
   int t;
   string s,ss;
   cin >> t;
   for(int i = 1; i <= t; ++ i) {

        cin >> s;
        ss = "";
        cout<<"Case #"<<i<<": ";

        for(int i = 0; i < s.size(); i ++) {

            if(s[i] != ss[ss.size() - 1] || ss.size() == 0)
                ss = ss + s[i];
        }

        int l = ss.size();
        if(ss[l - 1] == '+') ss = ss.substr(0 , l - 1);
        cout<<ss.size()<<endl;
   }
}
