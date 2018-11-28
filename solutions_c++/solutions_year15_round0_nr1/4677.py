#include <iostream>
#include <fstream>
#include <cmath>

using namespace std;

int main()
{
    //freopen("A-large.in.txt","r",stdin);
    //freopen("output.txt","w",stdout);
    int t; cin>>t;
    for (int tt=1;tt<=t;tt++) {
        int m; string str; cin>>m; cin>>str;
        int c=0,res=0;
        for (int i=0;i<str.size();i++) {
            if (i>res) res+=(i-res);
            c+=str[i]-'0';
            res+=str[i]-'0';
        }
        cout<<"Case #"<<tt<<": "<<res-c<<endl;
    }
    return 0;
}
