#define FILE_IO

#include<iostream>
#include<algorithm>
#include<cstdio>
#include<cstring>

using namespace std;

typedef long long ll;
#ifdef unix
#define LLD "%lld"
#else
#define LLD "%I64d"
#endif 

typedef double lf; 

typedef pair<int,int> pii;
typedef pair<lf,lf> pff;
#define mp make_pair
#define X first
#define Y second  

#define pb push_back
#define forI_(i,V,_) for(typeof(V.end())i=_;i!=V.end();++i)
#define forI(i,V) forI_(i,V,V.begin())


const int maxn=10010;
const int P=1000002013;
ll s[maxn];
pii a[maxn];
int b[maxn];

bool inter(const pii &a,const pii &b){
  return a.X<b.X&&b.X<=a.Y&&a.Y<b.Y
       ||b.X<a.X&&a.X<=b.Y&&b.Y<a.Y;
}

int main(){
#ifdef FILE_IO
  freopen("t.in","r",stdin);
  freopen("t.out","w",stdout);
#endif
  int T,Test=0;
  int n,m;
  int i,j,L;
  ll pos,org;
  bool found;
  for(scanf("%d",&T);T--;){
    ++Test;
    printf("Case #%d: ",Test);
    fprintf(stderr,"%d\n",Test);
    scanf("%d%d",&n,&m);
    for(i=1;i<n;++i)
      s[i]=s[i-1]+i-1;
    org=0;
    for(i=0;i<m;++i){
      scanf("%d%d%d",&a[i].X,&a[i].Y,b+i);
      org+=s[a[i].Y-a[i].X]*b[i];
    }
    found=1;
    while(found){
      found=0;
      for(i=0;i<m;++i)
        for(j=0;j<m;++j)
          if(inter(a[i],a[j])){
            if(b[i]>b[j])
              a[m]=a[i],b[m++]=b[i]-b[j],b[i]=b[j];
            else if(b[j]>b[i])
              a[m]=a[j],b[m++]=b[j]-b[i],b[j]=b[i];
            swap(a[i].Y,a[j].Y);
            //fprintf(stderr,"m=%d\n",m);
            found=1;
          }
    }
    pos=0;
    for(i=0;i<m;++i){
      //scanf("%d%d%d",&a[i].X,&a[i].Y,b+i);
      pos+=s[a[i].Y-a[i].X]*b[i];
    }
    printf("%lld\n",(pos-org)%P);
  }
  return 0;
}
