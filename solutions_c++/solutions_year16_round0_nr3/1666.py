#include <iostream>
#include <cstdio>
#include <set>
#include <cmath>
#include <ctime>
#include <vector>
#include <algorithm>
#include <queue>
#include <map>
#include <cstring>
#include <unordered_map>
#include <unordered_set>
#include <list>
#include <cassert>
#include <cstdlib>


#define LL long long int
#define Li long int
#define ULL unsigned long long int
#define mp make_pair
#define pb push_back
#define forr(i,n) for(int i=0;i<int(n);i++)
#define foor(i,a,b) for(int i=int(a);i<int(b);i++)
#define infloop for(;;)
#define loop(i,s) for(auto i : s)
#define endl "\n"
#define qq_endln endl

#define gcd __gcd

#define mod 1000000007ll

using namespace std;

typedef set<int> sint;
typedef multiset<int> msint;
typedef vector<int> vint;
typedef map<int, int> mint;
typedef unordered_map<int, int> _mint;
typedef queue<int> qint;
typedef unordered_set<int> _sint;
typedef list<int> lint;
typedef pair<int, int> pint;
typedef pair<long int, long int> plint;

unsigned long long int power(ULL x,ULL y){
	if(y==0)
		return (ULL)1;
	ULL q = power(x , (ULL)(y/(ULL)(2)));
	if(y%2==0)
		return q*q;
	else
		return q*q*x;

}

int main()
{
	int T;
	cin>>T;
	for(int i=1;i<=T;i++)
	{
		cout<<"Case #"<<i<<":"<<qq_endln;
		int N,J;
		cin>>N>>J;
		int syc=0;
		for(int k=0;k<15;k++)
			for(int l=k+1;l<15;l++)
				for(int n=0;n<15;n++)
					for(int m=n+1;m<15;m++)
			{
				if(syc==500)
					break;
				cout<<"1";
				for(int f=0;f<30;f++)
					{
						if(f==2*k or f==2*l or f==2*n+1 or f==2*m+1)
							cout<<"1";
						else
							cout<<"0";
					}
				cout<<"1";
				for(int z=2;z<11;z++)
					cout<<" "<<z+1;
				cout<<qq_endln;
				syc++;

			}
		cout<<qq_endln;
	}
	return 0;
}


