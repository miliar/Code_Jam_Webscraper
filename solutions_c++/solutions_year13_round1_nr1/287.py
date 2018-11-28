#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <string>
#define rep(i,j,k) for (int i=j;i<=k;++i)
#define rrep(i,j,k) for (int i=j;i>=k;--i)

using namespace std;

typedef long long digit;
class bigNum{
public:
    vector <long long> a;
    long long n;
public:
    bigNum(){//构造函数 
	n=0;
    }
    long long make (long long c){//将数字转化为向量 
	long long l=0;
	a.resize(30);
	while (c>0){
	    a[l++]=c%10;
	    c/=10;
	}
	--l;
	while (l>0 && a[l]==0) --l;
	n=l+1;
	return l+1;
    }
    long long make (string c){//将字符数组转化为向量 
	long long l=c.size();
	a.resize(l+10);
	n=l;
	for (long long i=0;i<l;++i){
	    a[i]=c[l-i-1]-'0';
	}
	--l;
	while (l>0 && a[l]==0) --l;
	n=l+1;
	return l+1;
    }
    void pout(){//输出 
	for (long long i=n-1;i>-1;--i)
	    printf("%lld",a[i]);
	printf("\n");
    }
    friend bigNum operator+(bigNum &a,bigNum &b){//重载+ 
	bigNum r;
	long long m=a.n>b.n?a.n:b.n;
	r.n=m;
	r.a.resize(m+10);
	for (long long i=0;i<m;++i){
	    if (a.n>i) r.a[i]+=a.a[i];
	    if (b.n>i) r.a[i]+=b.a[i];
	    r.a[i+1]+=r.a[i]/10;
	    r.a[i]%=10;
	}
	++r.n;
	while (r.n>0 && r.a[r.n]==0) --r.n;
	++r.n;
	return r;
    }
    friend bigNum operator -(bigNum &a,bigNum &b){//默认传入a>b 重载- 	
	bigNum r=a;
	long long m=r.n;
	for (long long i=0;i<m;++i){
	    if (b.n>i) r.a[i]-=b.a[i];long long j=i;
	    while (r.a[j]<0){
		r.a[j]+=10;
		--r.a[j+1];
	    }
	}
	--m;
	while (m>0 && r.a[m]==0) --m;
	r.n=m+1;
	return r;
    }
    friend bool operator >(bigNum &a,bigNum &b){//重载> 比较大小 
	if (a.n>b.n) return 1;
	if (a.n<b.n) return 0;
	for (long long i=a.n-1;i>=0;--i){
	    if (a.a[i]>b.a[i]) return 1;
	    if (a.a[i]<b.a[i]) return 0;
	}
	return 0;
    }
    friend bool operator >=(bigNum &a,bigNum &b){//重载>= 比较大小 
	if (a.n>b.n) return 1;
	if (a.n<b.n) return 0;
	for (long long i=a.n-1;i>=0;--i){
	    if (a.a[i]>b.a[i]) return 1;
	    if (a.a[i]<b.a[i]) return 0;
	}
	return 1;
    }
    friend bool operator <(bigNum &a,bigNum &b){//重载< 比较大小
	if (a.n<b.n) return 1;
	if (a.n>b.n) return 0;
	for (long long i=a.n-1;i>=0;--i){
	    if (a.a[i]>b.a[i]) return 0;
	    if (a.a[i]<b.a[i]) return 1;
	}
	return 0;
    }
    friend bool operator <=(bigNum &a,bigNum &b){//重载< 比较大小
	if (a.n<b.n) return 1;
	if (a.n>b.n) return 0;
	for (long long i=a.n-1;i>=0;--i){
	    if (a.a[i]>b.a[i]) return 0;
	    if (a.a[i]<b.a[i]) return 1;
	}
	return 1;
    }
    friend bool operator ==(bigNum &a,bigNum &b){//重载== 
	if (a.n!=b.n) return 0;
	for (long long i=0;i<a.n;++i)
	    if (a.a[i]!=b.a[i]) return 0;
	return 1;
    }
    friend bigNum operator * (bigNum &a,long long b){//重载* 高精度*低精度 
	bigNum r=a;
	r.a.resize(r.n+100);
	long long m=r.n;
	for (long long i=0;i<m;++i)
	    r.a[i]*=b;
	for (long long i=0;i<m;++i){
	    r.a[i+1]+=r.a[i]/10;
	    r.a[i]%=10;
	}
	while (r.a[m]>=10) {r.a[m+1]+=r.a[m]/10;r.a[m++]%=10;}
	r.n=m+1;while (r.a[r.n-1]==0) --r.n;
	return r;
    }
    friend bigNum operator * (bigNum &a,bigNum &b){//重载* 高精度*高精度 
	bigNum r,temp;
	if (a.n<b.n) {temp = a;a = b;b = temp;}
	r.a.resize(a.n+b.n+100);
	long long k;
	for (long long i=0;i<a.n;++i){
	    if (b.n<=i) continue;
	    temp=a*b.a[i];
	    temp=temp<<i;
	    r=r+temp;
	}
	r.n=a.n+b.n-1;
	for (long long i=0;i<r.n;++i){
	    r.a[i+1]+=r.a[i]/10;
	    r.a[i]%=10;
	}
	while (r.n>0 && r.a[r.n]==0) --r.n;
	++r.n;
	return r;
    }
    friend bigNum operator / (bigNum &a,long long b){
	bigNum r,rr;
	r.a.resize(a.n);r.n = 0;
	rr.a.resize(a.n);rr.n = 0;
	long long p = 0,pos= a.n-1;
	while (p<b)
	    p = p*10+a.a[pos--];
	for (long long i = pos+1;i>=0;--i){
	    r.a[r.n++] = p/b;
	    p = p % b;
	    p = p*10+a.a[i-1];
	}
	for (long long i=0;i<r.n;++i)
	    rr.a[i] = r.a[r.n-i-1];
	rr.n = r.n;
	return rr;
    }
    friend bigNum operator % (bigNum &a,long long b){
	bigNum r;
	r.a.resize(a.n);r.n = 0;
	long long p = 0,pos= a.n-1;
	while (p<b)
	    p = p*10+a.a[pos--];
	for (long long i = pos;i>=0;--i){
	    p = p % b;
	    p = p*10+a.a[i];
	}
	r.n = 1;
	r.a[0] = p%b;
	return r;
    }
    friend bigNum operator << (bigNum &a,long long b){//重载左移运算符，扩大10倍 
	bigNum r;
	r.a.resize(a.n+b);
	for (long long i=0;i<a.n;++i)
	    r.a[i+b]=a.a[i];
	r.n=a.n+b;
	return r;
    }
};
string sa,sb;


int main()
{
    freopen("aa.in","r",stdin);
    freopen("a.out","w",stdout);
    long long T;
    cin >> T;
    rep(test,1,T)
	{
	    bigNum r,t,start,one,two,four;
	    bigNum midd,use;
	    one.make("1");
	    two.make("2");
	    four.make("4");
	    cin >> sa >> sb;
	    r.make(sa);
	    t.make(sb);
	    start.make(sa);
	    start = start + start;
	    start = start + one;

	    long long left,right,mid,ans = 0;
	    left = 0,right = 1807106781;
	    while (left <=right )
		{
		    mid = (left + right) >> 1;
		    midd.make(mid);
		    use = start * 2;
		    bigNum tmp;
		    tmp.make(mid-1);
		    tmp = tmp * 4;
		    use = use + tmp;
		    use = use * midd;
		    use = use / 2;
		    //use = (2 * start + (mid - 1) * 4) * mid / 2;
		    /*
		    cout << "Mid "<<mid << endl;
		    start.pout();
		    tmp.pout();
		    use.pout();
		    cout << endl;
		    */
		    if (use <= t) ans = mid,left = mid+1;
		    else right = mid-1;
		}
	    cout << "Case #" << test << ": " << ans << endl;
	}
    return 0;
}
