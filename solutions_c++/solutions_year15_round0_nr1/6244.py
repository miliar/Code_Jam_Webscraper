//Lasha Bukhnikashvili
#include<iostream>
#include<stdio.h>
#include<math.h>
#include<iomanip>
#include<algorithm>
#include<vector>
#include<map>
#include<queue>
#include<string>
#define Pi 3.14159265358
#define mod9 %1000000009
#define INF 1000000000
#define mod7 %1000000007
#define LL  long long
#define time clock()/(double)CLOCKS_PER_SEC
using namespace std;
  int T,n,i,x,y,ans;
  char ch;
int main(){
 #ifndef ONLINE_JUDGE
   freopen("input.txt","r",stdin);
   freopen("output.txt","w",stdout);
 #endif
    cin>>T;
    int r=0;
    while (T--){

        cin>>n;
        r++;
        x=y=ans=0;
        for (i=0;i<=n;i++){
            cin>>ch;
            x=ch-'0';
            if (y>=i) y+=x;
            else ans+=i-y,y+=i-y,y+=x;
        }
        cout<<"Case #"<<r<<": "<<ans<<endl;
    }
 return 0;
}
