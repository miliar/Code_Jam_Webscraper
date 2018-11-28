#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
int T;
int N;
double a[2000],b[2000];
int main(){
    freopen("D-large.in","r",stdin);
    freopen("D-large.txt","w",stdout);
    cin>>T;
    for(int cas=1;cas<=T;++cas){
          scanf("%d",&N);
          for(int i=0;i<N;++i){
                  scanf("%lf",a+i);
          }
          for(int i=0;i<N;++i){
                  scanf("%lf",b+i);
          }
          sort(a,a+N);
          sort(b,b+N);
          int cnt1=0;
          int cnt2=0;
          int i=0,j=0;
          for(j=0;j<N;++j){
                  while(i<N && a[i]<b[j])
                            i++;
                  if(i>=N)
                          break;
                  else{
                       cnt1++;
                       i++;
                  }
          }
          j=0;
          for(i=0;i<N;++i){
                           while(j<N && b[j]<a[i])
                                     j++;
                           if(j>=N)
                                   break;
                           else{
                                cnt2++;
                                j++;
                           }
          }
          printf("Case #%d: %d %d\n",cas,cnt1,N-cnt2);
    }
    return 0;
}
