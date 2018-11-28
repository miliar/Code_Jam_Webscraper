#include<bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
typedef vector<pii> vpii;
typedef unsigned long long ULL;

#define author ayushtomar
#define rf freopen("in.in", "r", stdin)
#define wf freopen("out.txt", "w", stdout)
#define debug(x) cerr<<#x<<" "<<x<<endl;
#define f first

#define s second
#define mp make_pair
#define pb push_back
ULL mulmod(ULL a, ULL b, ULL c){
	ULL x = 0,y = a%c;

	while(b>0){
		if(b&1) x = (x+y)%c;
		y = (y<<1)%c;
		b >>= 1;
	}

	return x;
}

ULL pow(ULL a, ULL b, ULL c){
	ULL x = 1, y = a;

	while(b>0){
		if(b&1) x = mulmod(x,y,c);
		y = mulmod(y,y,c);
		b >>= 1;
	}

	return x;
}

bool miller_rabin(ULL p, int it){
	if(p<2) return false;
	if(p==2) return true;
	if((p&1)==0) return false;

	ULL s = p-1;
	while(s%2==0) s >>= 1;

	while(it--){
		ULL a = rand()%(p-1)+1,temp = s;
		ULL mod = pow(a,temp,p);

		if(mod==-1 || mod==1) continue;

		while(temp!=p-1 && mod!=p-1){
			mod = mulmod(mod,mod,p);
			temp <<= 1;
		}

		if(mod!=p-1) return false;
	}

	return true;
}

long long int modular_pow(long long int base, int exponent,
                          long long int modulus)
{
    long long int result = 1;

    while (exponent > 0)
    {
        if (exponent & 1)
            result = (result * base) % modulus;

        exponent = exponent >> 1;

        base = (base * base) % modulus;
    }
    return result;
}

long long int PollardRho(long long int n)
{
    srand (time(NULL));

    if (n==1) return n;

    if (n % 2 == 0) return 2;

    long long int x = (rand()%(n-2))+2;
    long long int y = x;

    long long int c = (rand()%(n-1))+1;

    long long int d = 1;

    while (d==1)
    {
        x = (modular_pow(x, 2, n) + c + n)%n;

        y = (modular_pow(y, 2, n) + c + n)%n;
        y = (modular_pow(y, 2, n) + c + n)%n;

        d = __gcd(abs(x-y), n);

        if (d==n) return PollardRho(n);
    }

    return d;
}
queue <ll > Q;
vector < ll >  v;
vector < ll > ans;
int main()
{
    wf;
    int t,n,jule;
    scanf("%d",&t);
    while(t--){
            scanf("%d %d",&n,&jule);
    printf("Case #1:\n");
    int counts=0;
    Q.push(1);
    int hue=(1<<(n-1))-1;
    while(hue--)
    {
        ll x=Q.front();
       // cout<<x<<"\n";
        v.pb(x);
        Q.pop();
        Q.push(x*10+0);
        Q.push(x*10+1);
    }
    ll x= v[v.size()-1];
    counts=0;
    int y=1<<(n-2);
    for(int i=v.size()-1;i>=v.size()-y;i--)
        {
            ans.clear();
            int flag=0;
            for(ll zz=2;zz<=10;zz++)
            {

                  ll qq=v[i]*10LL+1;
                  ll number=0;
                  while(qq)
                  {
                      number=number*zz+qq%10;
                      qq=qq/10;
                  }
                  if(miller_rabin(number,5))
                  {
                      flag=1;
                      break;
                  }

                  ans.pb(PollardRho(number));
            }
            if(flag==0)
            {
                ll pretty_please=v[i]*10LL+1LL;
                counts++;
                ll please=0;
                while(pretty_please)
                {
                    please=please*10LL+pretty_please%10;
                    pretty_please=pretty_please/10;
                }
                cout<<please<<" ";
                for(int i=0;i<ans.size();i++)
                    printf("%d ",ans[i]);
                printf("\n");
                if(counts==jule)
                    break;
            }

        }
    }

    return 0;
}
