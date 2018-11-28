#include <bits/stdc++.h>

using namespace std;
typedef long long  ll;


int main()
{
    freopen("ini.txt","r",stdin);
    freopen("filla.txt","w",stdout);
    int t;
    cin>>t;
    for (int z = 1; z<t+1; z++) {
        string s ;
        cin>>s;
        reverse(s.begin(), s.end());
        int begi= 0 ,sol=0;
        for (int i = 0; i<s.length(); i++) {
            if (begi==1 && s[i]!=s[i-1]) {
                sol++;
            }
            if (s[i]=='-') {
                begi=1;
            }
           
        }
        
        
        
        cout<<"Case #"<<z<<": "<<sol+begi<<endl;

    }
    
    
    return 0 ;
}