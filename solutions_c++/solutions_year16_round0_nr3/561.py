#include <bits/stdc++.h>
#include <stdlib.h>
using namespace std;

#define f(i,a)  for(int i=0;(i)<(a);++i)
#define fab(i,a,b) for (int i = (a); (i) < (b); ++i)
#define fba(i,a,b) for (int i = (b) - 1; (i) >= (a); --i)
#define fit(it,c) for(__typeof((c).begin()) it = (c).begin(); it != (c).end(); ++it)
#define all(c) (c).begin(),(c).end()


typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef unsigned int uint;
typedef char u8;
typedef vector <int> vi;
typedef pair <int, int> pii;
int divs[11];
int get_divisor(ll x, int base){
	fab(i,2,1+(int)sqrt(x))
		if(x%i==0){
			divs[base]=i;
			return i;
		}
	return 0;
}

ll check(ll x, int base){
	ll y=0,b=1;
	while(x){
		y+=(x%2)*b;
		x/=2;
		b*=base;
	}
	return y;

}

int all_prime(int x){
	fab(i,2,11)
		if(!get_divisor(check(x,i),i))
			return 0;
	return 1;
}
int check_plus_one(int x){
	fab(i,2,11)
		if(check(x,i)%(i+1))
			return 0;
	return 1;
}

int main()
{
    ios_base::sync_with_stdio(0);cin.tie(0);
    int T,t,n,j;//,k=0;
    ull x,y,plus_one[100000],psize=0;
    char s[35];
    cin>>T;
    f(t,T){
        cout<<"Case #"<<t+1<<":\n";
	cin>>n>>j;
	if(n<=16){
		x=(1<<(n-1))+1;
		y=1<<n;
		for(int i=x;i<y;i+=2)
			if(all_prime(i)){
				bitset<32> x(i);
				cout<<x.to_string().substr(32-n,n)<<" ";
				fab(k,2,11)
					cout<<divs[k]<<" ";
				cout<<"\n";
				//k++;
				if(!(--j))
					return 0;
			}
		//cout<<k<<"\n";
	} else {

		for(int i=3;i<256;i+=2)
			if(all_prime(i) && check_plus_one(i))
				plus_one[psize++]=i;
		ull z=((ull)1<<(n-1));
		f(i,psize){
			x=plus_one[i];
			while(x<z)
				x<<=1;
			f(k,psize){
				bitset<32> xy(x+plus_one[k]);
				cout<<xy.to_string().substr(32-n,n)<<" 3 4 5 6 7 8 9 10 11\n";
				if(!(--j))
					return 0;
			}
		}
		if(j)
			cout<<"error for "<<n<<" "<<j<<"\n";
	}
    }

    return 0;
}
