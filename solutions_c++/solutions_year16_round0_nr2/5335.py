#include <iostream>
#include <bits/stdc++.h>


using namespace std;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("ans.txt","w",stdout);
    int t;
    cin>>t;
    for(int h=1;h<=t;h++){
        string s;
        cin>>s;
        int len=s.length();
        int i;
        cout<<"Case #"<<h<<": ";
        for(i=0;i<len;i++){
            if(s[i]=='+')
                break;
        }
        if(i==len)
            cout<<1<<endl;
        else{
                int j=0,ans=0;
                for(j=0;j<len;j++){
                    if(s[j]=='+')
                        break;
                }
                if(j>0)
                    ans++;

            while(j<len){
                if(s[j]=='-'){
                    while(s[j]=='-'&&j<len){
                        j++;
                    }
                    ans+=2;
                }
                j++;
            }
          cout<<ans<<endl;
        }
    }
    return 0;
}
