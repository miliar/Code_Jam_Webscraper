#include <iostream>
#include<cstring>
#include<algorithm>
#include<cstdio>
using namespace std;

int main()
{
    int T;
    freopen("sha.txt","w",stdout);
    cin>>T;
    int t=T;
    while (T--){
        string z;
        cin>>z;
        reverse(z.begin(),z.end());
        char c='+';
        int ans=0;
        for (int j=0;j<z.size();j++){
            if (z[j]!=c){
                ans++;
                c=z[j];
            }
        }
        cout<<"Case #"<<t-T<<": "<<ans<<endl;
    }
    return 0;
}
