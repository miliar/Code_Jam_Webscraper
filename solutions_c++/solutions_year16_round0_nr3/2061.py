#include<bits/stdc++.h>
int tot = 0;
typedef long long LL;
using namespace std;
#define BIT 16
vector<bitset<BIT> > ans;
bitset<BIT> s(0);
class Primality {
public:
    typedef long long LL;
    // 判断num是否为质数
    bool miller_rabin(LL num){
        if(num<=1) return false;
        if(num<=3) return true;
        if(~num&1) return false;
        const int u[]={2,3,5,7,11,13,17,19,23,29,0};
        LL e=num-1,a,c=0;
        while(~e&1) e/=2,c++;
        for(int i=0;u[i];i++){
            if(num<=u[i]) return true;
            a=POW(u[i],e,num);
            if(a==1) continue;
            for(int j=1;a!=num-1;j++){
                if(j==c) return false;
                a=MUL(a,a,num);
            }
        }
        return true;
    }
    // 求一个小于n的因数，期望复杂度为O(n^0.25)，当n为非合数时返回n本身
    LL pollard_rho(LL n){
        if(n<=3 || miller_rabin(n)) return n; // 保证n为合数时可去掉这行
        while(1){
            int i=1,cnt=2;
            LL x=rand()%n,y=x,c=rand()%n;
            if(!c || c==n-2) c++;
            do{
                LL u=__gcd(n-x+y,n);
                if(u>1 && u<n) return u;
                if(++i==cnt) y=x,cnt*=2;
                x=(c+MUL(x,x,n))%n;
            }while(x!=y);
        }
        return n;
    }
    // 使用rho方法对n做质因数分解，建议先筛去小质因数后再用此函数
    vector<LL> factorize(LL n){
        vector<LL> u;
        if(n>1) u.push_back(n);
        for(size_t i=0;i<u.size();i++){
            LL x=pollard_rho(u[i]);
            if(x==u[i]) continue;
            u[i--]/=x;
            u.push_back(x);
        }
        sort(u.begin(),u.end());
        return u;
    }
    // 返回x与y相乘模m的结果，x与m要小于2^62
    LL MUL(LL x, LL y, LL m){
        LL c,s=0;
        for(c=x%m;y;c=(c+c)%m,y>>=1)
            if(y&1) s=(s+c)%m;
        return s;
    }
    // 返回x的y次方模m的结果，x与m要小于2^62
    LL POW(LL x, LL y, LL m){
        LL c,s=1;
        for(c=x%m;y;c=MUL(c,c,m),y>>=1)
            if(y&1) s=MUL(s,c,m);
        return s;
    }
} Prime;
LL calc(bitset<BIT> a,int p)
{
	LL ret = 0;
	LL x = 1;
	for (int i=0;i<BIT;i++)
	{
		ret += a[i] * x;
		x *= p;
	}
	return ret;
}
void debug()
{
	
}
int Stack[10];
void addAns(int n,int k,int start)
{
	if (k==0)
	{
		for (int i=2;i<=10;i+=2)
		{
			LL tmp = calc(s,i);
			//cout<<tmp<<endl; 
			if (Prime.miller_rabin(tmp)) return;	
		}
		ans.push_back(s);
		//cout<<tot<<endl;
		//cout<<s<<endl;
		tot--;
		return;
	}
	for (int i=start;i<n-1;i++)
		if (s[i]==0)
		{
			s[i] = 1;
			Stack[k] = i;
			addAns(n,k-1,i + 1);
			s[i] = 0;
		}
}
int main()
{
	s[0] = 1;
	s[BIT - 1] = 1;		
	freopen("C.in","r",stdin);
	freopen("C.out","w",stdout);
	int T = 1,test = 0,n,m;
	scanf("%d",&T);
	scanf("%d%d",&n,&m);
	//n = 16; m = 50;
	tot = m;
	for (int i=2;i<n;i+=2)
	{
		addAns(n,i,1);
		if (tot <=0) break;
	}
	int p = 0;
	cout<<"Case #1:\n";
	for (int i=1;i<=m;i++)
	{	
		cout<<ans[p]<<ans[p];
		for (int j=2;j<=10;j++)
		{
			LL tmp = calc(ans[p],j);	
			cout<<" "<<Prime.pollard_rho(tmp);
		}
		p++;
		cout<<endl;
			
		
	}
} 
