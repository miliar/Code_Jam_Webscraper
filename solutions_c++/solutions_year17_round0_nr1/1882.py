#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen("input.in","r",stdin);
    freopen("output.txt","w",stdout);
    int T;
    cin>>T;
    int cases= 0;
    while(T--){
        cases++;
        string x;int k;
        cin>>x>>k;
        int ans=0;
        for(int i=0;i+k<=x.size();i++){
            if(x[i]=='-'){
                ans++;
                for(int j=i;j<i+k;j++)
                    if(x[j]=='+')
                        x[j]='-';
                    else
                        x[j]='+';
            }
        }
        for(int i=0;i<x.size();i++){
            if(x[i]=='-')
                ans=-1;
        }
        if(ans!=-1)
            cout<<"Case #"<<cases<<": "<<ans<<endl;
        else
            cout<<"Case #"<<cases<<": IMPOSSIBLE\n";
    }
    return 0;
}
