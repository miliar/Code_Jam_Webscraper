#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <cmath>
#include <iostream>
#include <algorithm>
#define forup(i,a,b) for (int i=a;i<=b;i++)
#define fordown(i,a,b) for (int i=a;i>=b;--i)
#define p 1000002013

using namespace std;

int test,m;
long long n;
long long people[1001],in[1001],out[1001],peoplein[1001],peopleout[1001],posin[1001],posout[1001];

bool cmp1(const int &x,const int &y){
    return(in[x]<in[y]);
}

bool cmp2(const int &x,const int &y){
    return(out[x]<out[y]);
}

long long calc(long long A,long long B,long long C){
    return((((n*2-B+A)*(B-A+1)/2)%p*C)%p);
}

int main(){
    freopen("1.txt","r",stdin);
    freopen("2.txt","w",stdout);
    scanf("%d",&test);
    forup(uu,1,test)
    {
         printf("Case #%d: ",uu);
         scanf("%I64d%d",&n,&m);
         int begin=0;
         forup(i,1,m) 
         {
             scanf("%I64d%I64d%I64d",&in[i],&out[i],&people[i]);
             peoplein[i]=peopleout[i]=people[i];
             begin+=calc(in[i],out[i],people[i]);
             begin%=p;
         }
         int end=0;
         forup(i,1,m) posin[i]=i,posout[i]=i;
         sort(posin+1,posin+m+1,cmp1),
         sort(posout+1,posout+m+1,cmp2);
         int Left=1;
         fordown(i,m,1)
         {
              forup(j,1,m)
              if (!peoplein[posin[i]]) break;
              else
              if (out[posout[j]]>=in[posin[i]] && peopleout[posout[j]])
              {
                  int will=min(peoplein[posin[i]],peopleout[posout[j]]);
                  end+=calc(in[posin[i]],out[posout[j]],will);end%=p;
                  peoplein[posin[i]]-=will;peopleout[posout[j]]-=will;
              }
         }
         begin-=end;
         begin+=p;
         if (begin>=p) begin-=p;
         printf("%d\n",begin);
    }
}

