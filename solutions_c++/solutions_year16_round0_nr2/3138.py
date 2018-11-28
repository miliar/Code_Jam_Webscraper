#include<bits/stdc++.h>
using namespace std;
#define pb push_back
#define ll unsigned long long
#define lp(i,a) for(int i=0;i<a.size();i++)
#define mp make_pair
#define pii pair<int,int>
#define no(s) s=='-' ? '+' : '-'
bool check(string s){
    lp(i,s){
        if(s[i]=='-')return 0;
    }
    return 1;
}
string sw(string s){
    string t=s;
    int i;
    if(s[0]=='+'){
    i = 0;
    while(s[i]=='+')i++;
    i--;
    }
    else if(s.back()=='-') {
    i=s.length()-1;
    while(s[i]!='-')i--;
    }

    else {
    i=0;
     while(s[i]=='-')i++;
    i--;
    }
    for(int j=0;j<=i;j++)
       t[j]=no(s[i-j]);
    return t;
}
int main(){
    freopen("B.in","r",stdin);
    freopen("out.txt","w",stdout);
    int tc;cin>>tc;
    for(int t=1;t<=tc;t++){
         printf("Case #%d: ",t);
         string s;cin>>s;
         int ans = 0;
         do{
            if(check(s))
            {
                cout<<ans<<endl;
                break;
            }
            ans++;
            s=sw(s);
         }while(true);
    }

}
