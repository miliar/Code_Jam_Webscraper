#include<cstdio>
#include<cmath>
#include<ctime>
#include<cstdlib>
#include<cstring>
#include<set>
#include<map>
#include<vector>
#include<string>
#include<algorithm>
#include<iostream>
#include<iomanip>
#define REP(i,n) for (int i=0;i<(n);i++)
#define X first
#define Y second
using namespace std;
typedef pair<int,int> PII;
typedef pair<double,double> PDD;
const PII dir4[4]={PII(0,1),PII(0,-1),PII(1,0),PII(-1,0)};
const PII dir8[8]={PII(0,1),PII(0,-1),PII(1,0),PII(-1,0),PII(1,1),PII(1,-1),PII(-1,1),PII(-1,-1)};
const int inf=1000000000;
const double Zero=1e-7;
const double pi=cos(-1.0);
template<class T>T Min(T a,T b){return a<b?a:b;}
template<class T>T Max(T a,T b){return a>b?a:b;}
template<class T>T Abs(T a){return a>0?a:-a;}
template<class T>double getDist(pair<T,T> u,pair<T,T> v){return sqrt((u.X-v.X)*(u.X-v.X)+(u.Y-v.Y)*(u.Y-v.Y));}
template<class T>double getDist2(pair<T,T> u,pair<T,T> v){return Abs(u.X-v.X)+Abs(u.X-v.X);}
template<class T>double operator/(pair<T,T> u,pair<T,T> v){return u.X*v.Y-v.X*u.Y;}
template<class T>double operator*(pair<T,T> u,pair<T,T> v){return u.X*v.X+u.Y*v.Y;}
template<class T>pair<T,T> operator+(pair<T,T> a,pair<T,T> b){return make_pair(a.X+b.X,a.Y+b.Y);}
template<class T>pair<T,T> operator-(pair<T,T> a,pair<T,T> b){return make_pair(a.X-b.X,a.Y-b.Y);}
template<class T>pair<T,T> operator*(T a,pair<T,T> b){return make_pair(a*b.X,a*b.Y);}
template<class T1,class T2>istream& operator>>(istream& is,pair<T1,T2> &a){is>>a.X>>a.Y;return is;}
template<class T1,class T2>ostream& operator<<(ostream& os,pair<T1,T2> &a){os<<'<'<<a.X<<','<<a.Y<<'>';return os;}
typedef vector<int> BN;
#define BN_MODO 1000
BN operator+(BN a,BN b){int n=Max(a.size(),b.size());BN c;c.resize(n);int j=0;REP(i,n){c[i]=(i<a.size()?a[i]:0)+(i<b.size()?b[i]:0)+j;j=c[i]/BN_MODO;c[i]%=BN_MODO;}if (j)c.push_back(j);return c;}
BN operator-(BN a,BN b){int n=Max(a.size(),b.size());BN c;c.resize(n);int j=0;REP(i,n){c[i]=(i<a.size()?a[i]:0)-(i<b.size()?b[i]:0)+j;j=c[i]/BN_MODO;c[i]%=BN_MODO;}if (j)c.push_back(j);while (c.size()!=0 && *c.end()==0)c.pop_back();return c;}
BN operator*(BN a,BN b){int n=a.size(),m=b.size();BN c;c.resize(n+m-1);REP(i,n+m-1)c[i]=0;REP(i,n)REP(j,m)c[i+j]+=a[i]*b[j];int j=0;REP(i,n+m-1){c[i]+=j;j=c[i]/BN_MODO;c[i]%=BN_MODO;}if (j)c.push_back(j);return c;}
ostream& operator<<(ostream& os,BN &a){for (BN::reverse_iterator i=a.rbegin();i!=a.rend();i++){if (i!=a.rbegin())for (int j=(*i+(*i==0))*10;j<BN_MODO;j*=10)os<<0;os<<*i;};return os;}
struct point{double x,y,z;point(){}point(double x_,double y_,double z_):x(x_),y(y_),z(z_){}double mo(){return sqrt(x*x+y*y+z*z);}};
double getDist(point a,point b){return sqrt((a.x-b.x)*(a.x-b.x)+(a.y-b.y)*(a.y-b.y)+(a.z-b.z)*(a.z-b.z));}
point operator+(point a,point b){return point(a.x+b.x,a.y+b.y,a.z+b.z);}
point operator-(point a,point b){return point(a.x-b.x,a.y-b.y,a.z-b.z);}
point operator*(double a,point b){return point(a*b.x,a*b.y,a*b.z);}
double operator*(point a,point b){return a.x*b.x+a.y*b.y+a.z*b.z;}
istream& operator>>(istream& is,point &a){is>>a.x>>a.y>>a.z;return is;}


const int N=10000+100;
int value[N];
int rest[N];
int recover[N];
PII item[N];
int main(){
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int Test;
	scanf("%d",&Test);
	for (int test=1;test<=Test;++test){
		int e,r,n;
		long long ans=0;
		scanf("%d%d%d",&e,&r,&n);
		for (int i=0;i<n;i++){
			cin>>value[i];
			item[i].X=-value[i];
			item[i].Y=i;
			rest[i]=r;
			recover[i]=r;
		}
		rest[0]=e;
		recover[0]=e;
		sort(item,item+n);
		for (int i=0;i<n;i++){
			int j=item[i].Y;
			for (int k=j;k>=0 && e-(j-k)*r>0;k--){
				int tmp=e-(j-k)*r;
				if (tmp>recover[k])
					tmp=recover[k];
				if (recover[k]-tmp<rest[k]){
					ans+=(long long)(rest[k]-(recover[k]-tmp))*value[j];
					rest[k]=recover[k]-tmp;
				}
			}
		}
		cout<<"Case #"<<test<<": "<<ans<<endl;
	}
}
