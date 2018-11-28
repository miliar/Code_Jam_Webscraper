#include <stdio.h>
#include <vector>
#include <algorithm>
#include <map>
using namespace std;

void input();
void proc();
void output();

int main()
{
	freopen ("input.txt","r",stdin);
	freopen ("output.txt","w",stdout);

	int Test,Case=1;
	scanf ("%d",&Test); while (Test--){
		input();
		proc();
		printf ("Case #%d: ",Case++);
		output();
	}

	return 0;
}

int N,K;
map<long long, long long> P;
long long ans;
const long long mod = 1000002013;

void input()
{
	int i; long long s,e,v;

	P.clear(); ans = 0;
	scanf ("%d %d",&N,&K);
	for (i=0;i<K;i++){
		scanf ("%lld %lld %lld",&s,&e,&v);
		P[s] += v;
		P[e] -= v;
		ans = (ans + v * (((e - s) * (N * 2 - (e-s-1)) / 2) % mod) % mod) % mod;
	}
}

vector<pair<long long, long long> > U;
void proc()
{
	map<long long, long long>::iterator I;
	int last=0,dif,i;

	U.clear();
	for (I=P.begin();I!=P.end();I++){
		dif = I->first - last;
		last = I->first;
		for (i=0;i<U.size();i++){
			ans = (ans + mod - (U[i].second * (dif * (U[i].first * 2 - dif + 1) / 2) % mod) % mod) % mod;
			U[i].first -= dif;
		}

		if (I->second > 0){
			U.push_back(make_pair(N,I->second));
		}
		else if (I->second < 0){
			sort(U.begin(),U.end());
			long long v = -I->second;
			for (i=((int)U.size())-1;i>=0;i--){
				if (U[i].second > v){
					U[i].second -= v;
					break;
				}
				else{
					v -= U[i].second;
					U.pop_back();
				}
			}
		}
	}
}

void output()
{
	printf ("%lld\n",ans);
}
