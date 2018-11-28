#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen("myfile.in","r",stdin);
    freopen("myfile.out","w",stdout);

    int t;
    cin>>t;
    for(int f=1; f<=t; f++){
        string str;
        cin>>str;

        string res;
        res += str[0];
        for(int i=1; i<str.size(); i++){
            if(str[i] >= res[0])
                res = str[i] + res;
            else
                res+=str[i];
        }
        cout<<"Case #"<<f<<": "<<res<<endl;
    }
    return 0;
}
