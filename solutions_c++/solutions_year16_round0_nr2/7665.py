#include <bits/stdc++.h>
using namespace std;

int main()
{

    freopen ("B-large.in","r",stdin);
    freopen ("B-large.out","w",stdout);
    int t;
    cin>>t;
    for(int f=1; f<=t; f++){
        string str;
        cin>>str;

        int res =0;
        int i=0;
        while(i<str.size() && str[i]=='-')
            i++;
        if(i>0)
            res++;
        for(; i<str.size(); i++){
            if(str[i] == '-'){
                while(i<str.size() && str[i]=='-')
                    i++;
                res+=2;
            }
        }

        cout<<"Case #"<<f<<": "<<res<<endl;

    }

    return 0;
}
