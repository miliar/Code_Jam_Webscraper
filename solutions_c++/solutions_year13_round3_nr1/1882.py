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
#define S(x) cin>>x

using namespace std;
int main(){
  int t;
  S(t);
  for(int c=1;c<=t;c++){
    printf("Case #%d: ",c);
    string str;
    int N;
    int cntr=0;
    S(str);S(N);
    int sz=str.length();
    
    for(int i=0;i<sz;i++){
      int tmp2=-1;
      
      for(int j=1;i+j<=sz;j++){
      int Nvalue=1<<29; 
       string st=str.substr(i,j);
      int tmp=0;
      REP(k,j){
              if(st[k]!='a'&&st[k]!='i'&&st[k]!='e'&&st[k]!='o'&&st[k]!='u') tmp++;
              else {
                if(tmp>=N) {cntr++;
                break;
              }
             tmp=0;
             }
            if(tmp>=N) {
              cntr++;
              break;
            }  
          
          }
   
    }
   }
 cout<<cntr<<endl;
 }
 }            
