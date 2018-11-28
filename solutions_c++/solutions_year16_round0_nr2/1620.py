#include<bits/stdc++.h>
using namespace std;
int main(){
    ios_base::sync_with_stdio(0);
    cin.tie(nullptr);
    int t;
    cin>>t;
    for(int z=1;z<=t;z++){
        string s;
        cin>>s;
        int ans=0;
        reverse(s.begin(),s.end());
        for(int i=0;i<(int)s.size();i++){
            if(s[i]=='+')continue;
            bool f=(s[s.size()-1]=='+');
            int cnt=1;
            for(int j=s.size()-2;j>=i;j--){
                if(s[j]==s[s.size()-1])cnt++;
                else break;
            }
            if(!f){
                ans++;
                string x=s.substr(i,s.size()-i);
                string y=s.substr(0,i);
                reverse(x.begin(),x.end());
                for(int j=0;j<(int)x.size();j++){
                    if(x[j]=='+')x[j]='-';
                    else x[j]='+';
                }
                s=y+x;
            }else{
                ans+=2;
                for(int j=s.size()-1;cnt>0;j--,cnt--){
                    s[j]='-';
                }
                string x=s.substr(i,s.size()-i);
                string y=s.substr(0,i);
                reverse(x.begin(),x.end());
                for(int j=0;j<(int)x.size();j++){
                    if(x[j]=='+')x[j]='-';
                    else x[j]='+';
                }
                s=y+x;
            }
        }
        cout<<"Case #"<<z<<": "<<ans<<"\n";
    }
    return 0;
}
