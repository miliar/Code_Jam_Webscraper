#include<algorithm>
#include<cstdio>
#include<cstring>

using namespace std;

int a[15],v[20];
long long pow[11][20];
int n,m,ca,cas,i,j,k;

void Work(int x){

int i;

  memset(v,0,sizeof(v));
  memset(a,0,sizeof(a));
  i=1;
  while (x){
    v[i++]=x % 2;
    x>>=1;
  }
 // for (i=n;i>=1;i--) printf("%d",v[i]);
 // printf("\n");
}

int Check(int x){

int i,c,f;
long long t;

  Work(x);
  for (i=2;i<=10;i++){
    t=0;
    for (j=1;j<=n;j++) t+=v[j]*pow[i][j-1];
 //   printf("%lld\n",t);
    f=0;
    for (j=2;j<=500;j++)
      if (t % j==0){
        f=1;
        a[i]=j;
      }
    if (!f) return 0;
  }


}

void Put(){

int i;

  for (i=n;i>=1;i--) printf("%d",v[i]);
  for (i=2;i<=10;i++) printf(" %d",a[i]);
  printf("\n");

}

int main(){

 // n=4;
  for (i=2;i<=10;i++){
    pow[i][0]=1;
    for (j=1;j<=17;j++) pow[i][j]=pow[i][j-1]*i;
  }

  freopen("C_s.in","r",stdin);
  freopen("C_s.out","w",stdout);



  scanf("%d",&cas);
  for (ca=1;ca<=cas;ca++){
    printf("Case #%d:\n",ca);
    scanf("%d%d",&n,&m);




    for (i=(1<<(n-1));i<1<<n;i++){
      if ((i & 1) && Check(i)){
        m--;
        Put();
        if (m==0) break;
      }
    }
  }


  //Check(9);
 // Put();
  return 0;


}
