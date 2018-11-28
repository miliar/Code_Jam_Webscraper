#include <bits/stdc++.h>
#define loop(i,s,e) for(int i =s ;i < e;i++)
#define space " "
using namespace std;
int s[2000];
int ss,standpeople = 0,smax;
string sss;
int main(){
freopen("A-large.in","r",stdin);
freopen("outlarge.out","w",stdout);
int tc = 1,cs = 1;
cin >>tc;
while(tc--){
cin >> smax>>sss;
loop(i,0,sss.size()) s[i] = sss[i]-'0';
//loop(i,0,sss.size()) cout<<s[i]<<space;cout<<endl;
standpeople = s[0];
int c = 0;
loop(i,1,sss.size()){
   // cout<<(i <= standpeople)<<space<<i<<space<<standpeople<<endl;
if(i <= standpeople){
    standpeople += s[i];
}else{
c++;
standpeople+=s[i]+1;
}
}
printf("Case #%d: %d\n",cs++,c);
}
    return 0;
}
