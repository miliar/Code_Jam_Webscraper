#include <bits/stdc++.h>

using namespace std;

#define max(a,b) ((a)>(b)?(a):(b))
#define min(a,b) ((a)<(b)?(a):(b))
#define abs(x) ((x)<0?-(x):(x))
#define pii pair<int,int>
#define m_p make_pair(n,m)
#define mod 1000000007
#define pb push_back
#define bp(x) __builtin_popcount(x)
typedef long long int ll;
bool isPrime[1000005];
vector <int > prime;
ll ipow(int a, int b)
{
	ll x=1,y=a; 
	while(b > 0)
	{
		if(b%2 == 1)
		{
			x=(x*y);
		}
		y = (y*y);
		b /= 2;
	}
	return x;
}
void sieve(int N) {
    for(int i = 0; i <= N;++i) {
        isPrime[i] = true;
    }
    isPrime[0] = false;
    isPrime[1] = false;
    for(int i = 2; i * i <= N; ++i) {
         if(isPrime[i]==true) {
         	prime.push_back(i);
             for(int j = i * i; j <= N ;j += i)
                 isPrime[j]=false;
        }
    }
}
int main()
{
	#ifndef ONLINE_JUDGE
		freopen("input.txt","r",stdin);
		freopen("output.txt","w",stdout);
	#endif
	ios::sync_with_stdio(false);cin.tie(0);
	int t,z,n,j,i,l,r,q;
	ll sum=0;
	int arr[18];
	cin>>t;
	sieve(1000005);
	for(z=1;z<=t;z++)
	{
		cout<<"Case #"<<z<<": \n";
		int c=0;
		vector <int > v;
		cin>>n>>j;
		for(i=1<<(n-1);i<(1<<n);i++)
		{	if(i%2==1)
			{
				q=0;
				int num=i;
				while(num!=0)
				{
					arr[q]=num%2;
					num/=2;
					q++;
				}
				v.clear();
				for(r=2;r<=10;r++)
				{
					sum=0;
					for(l=0;l<q;l++)
					{
						sum+=arr[l]*ipow(r,l);
					}
					//cout<<sum<<"\n";
					for(l=0;l<prime.size();l++)
					{
						if(sum%prime[l]==0)
						{
							v.push_back(prime[l]);
							break;
						}
					}
				}
				if(v.size()==9)
				{
					for(l=q-1;l>=0;l--)
						cout<<arr[l];
					cout<<" ";
					for(l=0;l<v.size();l++)
					{
						cout<<v[l]<<" ";
					}
					cout<<"\n";
					c++;
					if(c>=j)
						break;
				}
			}
		}
	}
	return 0;
}
