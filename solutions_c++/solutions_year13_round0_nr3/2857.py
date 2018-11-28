//shjj-Fair and Square

#include <iostream>
#include <cstring>
#include <cstdio>
#include <cstdlib>

using namespace std;

const long long oo=10,gjL=200;
typedef long long gj[gjL+3];
gj X,a,s,aa;
int ls;
long long ans;

void clean(gj &a){memset(a,0,sizeof(a));}
void Copygj(gj &a,gj b){for (int i=a[0]+1;i<=b[0];i++) a[i]=0;for (int i=1;i<=b[0];i++) a[i]=b[i];a[0]=b[0];a[gjL]=b[gjL];}
int Lar(gj a,gj b)
{
if (a[0]>b[0]) return 1;if (a[0]<b[0]) return -1;
for (int i=a[0];i>=1;i--){if (a[i]>b[i]) return 1;if (a[i]<b[i]) return -1;}
return 0;
}
void Relaxup(gj &a)
{
for (int i=1;i<=a[0];i++)if (a[i]>=oo) {a[i+1]+=a[i]/oo;a[i]%=oo;}
if (!a[a[0]+1]) return;a[0]++;
for (;a[a[0]]>=oo;) {a[a[0]+1]+=a[a[0]]/oo;a[a[0]]%=oo;a[0]++;}
}
void Relaxdown(gj &a){for (;a[0]>1&&!a[a[0]];a[0]--);}
void Chenge(gj &a,gj b)
{
gj tmp;clean(tmp);for (int i=1;i<=a[0];i++)for (int j=1;j<=b[0];j++) tmp[i+j-1]+=a[i]*b[j];
tmp[0]=a[0]+b[0]-1;Relaxup(tmp);Copygj(a,tmp);
}
bool check(gj a)
{
int l=(a[0]+1)>>1;
for (int i=1;i<=l;i++) if (a[l]!=a[a[0]-l+1]) return false;
return true;
}

long long find(long long x)
{
if (!x) return 0;int ss=0;if (x>=9) ss++;clean(X);
X[1]=0;for (;x;) X[++X[0]]=x%10,x/=10;
ls=1;a[1]=0;
for (;;)
  {
  int w=1;
  for (;a[w]==2;w++);
  a[w]++;
  for (int i=w-1;i>=1;i--) a[w]=0;
  if (w>ls) ls=w;
  memcpy(aa,a,sizeof(aa));
  
  for (int i=1;i<=ls;i++) aa[ls+i]=aa[ls-i+1];
  
  aa[0]=ls*2;
  memcpy(s,aa,sizeof(s));
  Chenge(s,aa);
  int typ=Lar(s,X);
  if (typ==1) break;
  if (check(s)) 
  {
	ss++;
	}
  }

clean(a);
ls=1;a[1]=0;
for (;;)
  {
  int w=1;
  for (;a[w]==2;w++);
  a[w]++;
  for (int i=w-1;i>=1;i--) a[w]=0;
  if (w>ls) ls=w;
  memcpy(aa,a,sizeof(aa));
  
  for (int i=1;i<ls;i++) aa[ls+i]=aa[ls-i];
  
  aa[0]=ls*2-1;
  memcpy(s,aa,sizeof(s));
  Chenge(s,aa);
  int typ=Lar(s,X);
  if (typ==1) break;
  if (check(s)) 
    {
	ss++;
	}
  }

return ss;
}

int main()
{
freopen("C.in","r",stdin);
freopen("C.out","w",stdout);
int Test,TT=0;scanf("%d",&Test);
for (;Test--;)
  {
  long long L,R;
  scanf("%I64d%I64d",&L,&R);
  ans=find(R)-find(L-1);
  printf("Case #%d: %I64d\n",++TT,ans);
  }
}