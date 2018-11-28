#include <bits/stdc++.h>
using namespace std;
#define gc getchar_unlocked
#define fo(i,n) for(i=0;i<n;i++)
#define Fo(i,k,n) for(i=k;i<n;i++)
#define ll long long
#define pii pair<int,int>
#define vi vector<int>
#define pb push_back
#define mp make_pair
#define F first
#define S second
#define pt(x) printf("%d\n",x)
#define ptl(x) printf("%lld\n",x)
const int mod = 1000000007;

void sd(int &x);
void sd(ll &x);
int mpow(int base, int exp); 


int main()
{
	int t;
	sd(t);
	int i,n,dig;
	ll no, x;
	int T;
	fo(T,t)
	{
		cout<<"Case #"<<T+1<<": ";
		sd(n);
		int cnt[10];
		fo(i,10)
			cnt[i]=0;
		if (n==0){
			cout<<"INSOMNIA\n";
			continue;
		}
		int flag = 0;
		no = 0;
		while(flag!=10){
		 	no += n;
			x = no;
			while(no>0){
				dig = no%10;
				no /= 10;
				if (cnt[dig]==0){
					flag++;
					cnt[dig] = 1;
				}
				
			}
			no = x;
		}
		cout<<x<<endl;
	
	}
	
	return 0;
} 



void sd(int &x)
{
    register int c = gc();
    x = 0;
    for(;(c<48 || c>57);c = gc());
    for(;c>47 && c<58;c = gc()) {x = (x<<1) + (x<<3) + c - 48;}
}

void sd(ll &x)
{
    register int c = gc();
    x = 0;
    for(;(c<48 || c>57);c = gc());
    for(;c>47 && c<58;c = gc()) {x = (x<<1) + (x<<3) + c - 48;}
}

int mpow(int base, int exp) {
  base %= mod;
  int result = 1;
  while (exp > 0) {
    if (exp & 1) result = ((ll)result * base) % mod;
    base = ((ll)base * base) % mod;
    exp >>= 1;
  }
  return result;
}