//Md. Ahsan Kabir Shohagh
#include<bits/stdc++.h>
using namespace std;
#define sz 100000
#define pb(a) push_back(a)
#define ll long long
#define ull unsigned long long
#define fread freopen("input.txt","r",stdin)
#define fwrite freopen("output.txt","w",stdout)
#define inf (1<<29)
#define mem(abc,z) memset(abc,z,sizeof(abc))
#define PI acos(-1)

int main(){
   int t,Smx,ans,curPeople;
   string s;
   fread;
   fwrite;
   cin>>t;
   for(int ca=1;ca<=t;ca++){
     cin>>Smx>>s;
     ans=curPeople=0;
     for(int i=0;i<Smx+1;i++){
        if(i>curPeople){
            ans+=(i-curPeople);
            curPeople+=(i-curPeople+s[i]-'0');
        }
        else {
            curPeople+=(s[i]-'0');
        }
     }
     cout<<"Case #"<<ca<<": "<<ans<<endl;
   }
   return 0;
}
