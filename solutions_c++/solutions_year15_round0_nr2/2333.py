#include <bits/stdc++.h>
using namespace std;
int main(){
int T;
scanf("%d",&T);
for(int Case=1;Case<=T;Case++){
int D;cin >> D;
int plates[D];
for(int i =0;i<D;i++)cin >> plates[i];
sort(plates,plates+D);
int ans=plates[D-1];
for(int i=1;i<plates[D-1];i++){
int val=0;
for(int j=0;j<D;j++){
if(i>plates[j]) continue;
val+=plates[j]/i+(plates[j] % i != 0)-1;
}
ans=min(ans,val+i);
}
printf("Case #%d: %d\n",Case,ans);
}
}
