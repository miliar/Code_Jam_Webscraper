#include<bits/stdc++.h>
#include<stdio.h>
#include<string.h>
using namespace std;
int main(){

int t,smax,i;
char a[1010];
int uptillnow;
/*#ifndef ONLINE_JUDGE
freopen("input.txt", "r" , stdin);
freopen("output.txt", "w", stdout);
#endif
*/

//scanf("%d",&t);
cin>>t;
int j;
for(j=1;j<=t;j++){
//for(i=0;i<1010;i++) uptillnow[i]=0;
//scanf("%d",&smax);
cin>>smax;
//scanf("%s",&a);
cin>>a;
int extra=0;
uptillnow=0;
if(a[0]=='0') { extra+=1;uptillnow=1;} else uptillnow+=a[0]-48;
//printf("%d\n",extra);
for(i=1;i<=smax;i++){
if(i>uptillnow){ extra+=i-uptillnow; uptillnow+=i-uptillnow;}


uptillnow+=a[i]-48;
//printf("%d\n",extra);
}

//printf("Case #%d: %d\n",j,extra);
cout<<"Case #"<<j<<": "<<extra<<endl;
}

return 0;
}
