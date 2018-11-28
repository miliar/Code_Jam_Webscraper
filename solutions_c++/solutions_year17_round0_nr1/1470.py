#include <bits/stdc++.h>

using namespace std;


int main()
{
//
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t,k,cnt;
    bool check=0;
    string s;
    cin>>t;
    for(int tc=1;tc<=t;tc++){
        check=0; cnt=0;
        cin>>s>>k;
        for(int i=0;i<s.length();i++){
            if(s[i]=='-'){
                cnt++;
                for(int j=0;j<k;j++){
                    if(j+i==s.length()){
                        check=1;
                        break;
                    }
                    if(s[i+j]=='-') s[i+j]='+';
                    else s[i+j]='-';
                }
                if(check) break;
            }
        }
        printf("Case #%d: ",tc);
        if(check) printf("IMPOSSIBLE\n");
        else printf("%d\n",cnt);
    }



}
