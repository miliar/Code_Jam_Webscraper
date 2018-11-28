#include <cstdio>
#include <cmath>
const int MAXN=101;
/*class Tiint{
   public:
      int a[MAXN],len;
      Tiint(){
	 this->len=0;
	 for(int i=0;i<MAXN;++i) this->a[i]=0;
      };
      void initial(){
	 char c;
	 int l=0;
	 for(;!(('0'<=c)&&(c<='9'));scanf("%c",&c));
	 for(;(('0'<=c)&&(c<='9'));scanf("%c",&c)) this->a[l++]=c-'0';
	 this->len=l;
      }
      Tiint operator+(const Tiint &t1){
	 Tiint to;
	 if(this->len > t1->len) to.len=this->len;
	 else to.len=t1->len;
	 for(int i=0;i<to.len;++i){
	    to.a[i]+=this->a[i]+t1->a[i];
	    if(to.a[i]>9) {to.a[i]-=10; to.a[i+1]=1}
	    else to.a[i+1]=0;
	 }
	 if(to.a[l+1]>0) ++(to.len);
	 return to;
	 }
      Tiiint &operator+=(const Tiint &t1){
	 if(this->len < t1->len) this->len=t1->len;
	 for(int i=0;i<this->len;++i){
	    this->a[i]+=t1->a[i];
	    if(this->a[i]>9) {this->a[i]-=10; this->a[i+1]=1}
	    else this->a[i+1]=0;
	 }
	 if(this->a[l+1]>0) ++(this->len);
	 return *this;
      }
      Tiint &operator*=(const Tiint &t1){
      }
}*/
int T;
bool isfair(long long n){
   int l=0;
   int a[20];
   for(;n>0;n=n/10) a[l++]=n%10;
   bool flag=true;
   for(int i=0;i<=(l>>1);++i)
      if(a[i]!=a[l-i-1]) flag=false;
   return flag;
}
int main(){
   scanf("%d",&T);
   for(int testcase=0;testcase<T;++testcase){
      long long a,b,l,r;
      long long cnt=0;
      scanf("%lld%lld",&a,&b);
      l=sqrt(a);
      if(l*l<a) ++l;
      r=sqrt(b);
      for(long long n=l;n<=r;++n)
	 if(isfair(n)){
	    long long m=n*n;
	    if(isfair(m)){
	       ++cnt;
	       //printf("%lld ",m);
	    }
	 }
      printf("Case #%d: %lld\n",testcase+1,cnt);
   }
}
