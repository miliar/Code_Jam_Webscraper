#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <queue>
#include <bitset>
#include <set>
using namespace std;
#define int unsigned long
typedef long long LL;

//*******************
//*******************
vector<int> primes;

bool tab[131072];

void prime()
{
	for(int i=0; i<2000; i++)
		tab[i]=0;
	for(int i=2; i<500; i++)
	{
		if(tab[i] == 0)
		{
			primes.push_back(i);
			tab[i]=1;
			int j=i; while(j<10000)
			{
				tab[j]=1;
				j+=i;
			}
		}
	}
}
set<int> S;


bool check(int i)
{
	// cout<<i<<endl;
	if(i%2==0)
		return false;
	if(i>=65536)
		return false;
	if(i<0)
		return false;

	vector<int> v;

	for(int j=2; j<=10; j++)
	{
		int num = 0;
		int k= i;
		int w = 1;
		while(k>0)
		{
			num+= w*(k%2);
			w*=j;
			k/=2;
		}
		// if(j==10)
		// 	cout<<endl<<num<<endl;
		bool czy = false;
		for(int& x : primes)
			if(num%x==0)
				{v.push_back(x); czy=true; break;}
		if(czy==false)
			return false;
	}


	cout<<bitset<16>(i)<<" ";
	for(int&x : v)
		cout<<x<<" ";
	cout<<endl;

	return true;
	// if(i)
}

main() {
  ios::sync_with_stdio(false);
  prime();
  // cout<<primes.size();

  // cout<<endl;
  int a,b,c; cin>>a>>b>>c;
  	  // cout<<M.size()<<endl;
  	srand((unsigned)time(0)); 

  cout<<"Case #1:"<<endl;
  int ile = 0; int i =32769;
  while(ile<50)
  {
	int r = (rand()%(32768)) + 32769;
	if(S.find(r) != S.end())
		continue;
	S.insert(r);
	if(check(r))
  		ile++;
  }
  return 0;
}