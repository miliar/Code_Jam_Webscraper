#include<stdio.h>
#include<iostream>
#include<algorithm>
#include<cmath>
#include<vector>
#include<cstdlib>
#include<stack>
#include<queue>
#include<string>
#include<cstring>
#include<set>
#include<map>
#include<utility>

#define PR(x) cout<<#x<<"="<<x<<endl
#define READ2(x,y) scanf("%d %d",&x,&y)
#define REP(i,a) for(int i=0;i<a;i++)
#define READ(x) cin>>x
#define PRARR(x,n) for(int i=0;i<n;i++)printf(#x"[%d]=\t%d\n",i,x[i])
#define rd(arr,i,n) for(int i=0;i<n;i++) cin>>arr[i]
#define PB push_back
#define SUM(arr,n,sum) {sum=0;for(int i=0;i<n;i++) sum+=arr[i]; }
#define VC vector
#define CLR(arr) memset(arr,0,sizeof(arr))
#define FILL(arr,val) memset(arr,val,sizeof(arr))
using namespace std;
int cnt[1001];
bool check(int num){
  char nmbr[20];
  sprintf(nmbr,"%d",num);
  int idx=0;
  while(num){
  if(num%10+'0'!=nmbr[idx++]) return false;
  num/=10;  
  }
  
 return true;
}
void pre(){
  for(int i=1;i*i<=1000;i++){
    int num=i*i;
    if(check(i)&&check(num)) cnt[num]++;
  }
for(int i=1;i<=1000;i++) cnt[i]+=cnt[i-1];
}
int main(){
  pre();
  int t;
  scanf("%d",&t);
  for(int cases=1;cases<=t;cases++){
    printf("Case #%d: ",cases);
    int a,b;
    scanf("%d %d",&a,&b);
    printf("%d\n",cnt[b]-cnt[a-1]);
  }
}
