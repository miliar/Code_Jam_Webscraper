#include<bits/stdc++.h>
using namespace std;
long long t,l,n,ans,k,i;
string s;
int main(){
    freopen("B.in","r",stdin);
    freopen("B.out","w",stdout);
    cin>>t;
    for(l=0;l<t;l++){
        cin>>s;
        cout<<"Case #"<<l+1<<": ";
        ans=0;
        for(i=s.size()-1;i>=0;i--)
            if (s[i]=='+') s.pop_back(); else break;
        while(s.size()>0){
            k=0;
            if (s[0]=='-'){
                ans++;
                i=1;
                while(s[i]=='-'){
                    i++;
                }
                s.erase(s.begin(),s.begin()+i);
                reverse(s.begin(),s.end());
                for(i=0;i<s.size();i++)
                    if (s[i]=='+') s[i]='-'; else s[i]='+';
                //cout<<i<<" "<<s<<endl;
            } else {
                ans+=2;
                for(i=1;i<s.size();i++){
                    if (s[i]=='-') k=1;
                    if (s[i]=='+' && k==1) break;
                }
                s.erase(s.begin(),s.begin()+i);
                reverse(s.begin(),s.end());
                for(i=0;i<s.size();i++)
                    if (s[i]=='+') s[i]='-'; else s[i]='+';
                //cout<<"+++ "<<i<<" "<<s<<endl;
            }
        }
        cout<<ans<<endl;
    }
    return 0;
}
