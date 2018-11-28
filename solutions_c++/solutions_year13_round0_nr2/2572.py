// author : theycallhimavi
#include <iostream>
#include <cstdio>
#include <vector>
#include <map>
#include <iterator>
#include <set>
#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstring>
#include <string>
#include <list>
#include <queue>
#include <stack>
#include <ctype.h>
#include <iomanip>
#include <ctime>
#include <cstdlib>
#include <utility>
using namespace std;
/*inline long long read_long long() {
char c;
while ((c=getchar_unlocked()) < 48 || c > 57);
long long p = c-48;
while ((c=getchar_unlocked()) >= 48 && c <= 57) p=p*10+c-48;
return p;
}*/

#define maximum(x,y) ((x)<(y) ? (y) : (x))
#define MIN(x,y) ((x)<(y) ? (x) : (y))
#define SWAP(x,y) do { a+=b; b=a-b; a=a-b; } while( 0 )
#define mod1 1000000007ll
#define mod2 10000007ll
#define inf 99999999999999999ll
#define REP(i,n) for(i=0;i<n;i++)
#define REPI(i,j,n) for(i=j;i<n;i++)
#define PER(i,n) for(i=n-1;i>=0;i--)
typedef vector<long long> vi;
typedef pair<long long, long long> ii;

template <class T>
T power(T x,T y,T m)
{
	T temp;
	if( y == 0)
		return 1;
	temp = power(x,y/2,m)%m;
	if (y%2 == 0)
		return ((temp % m)*(temp% m))%m;
	else
		return (((((x)*(temp))%m)*(temp))%m)%m;
}


int main(){
	long long cases;
	long long C = 0;
	cin>>cases;
	while(cases--){
		C++;
		long long n,m;
		cin>>n>>m;
		vector<vi >v(n,vi (m));
		vi horizontal_rows(n);
		vi vertical_coloumns(m);
		for(long long i = 0;i < n;i++){
			long long maximum = 0;
			for(long long j = 0;j < m;j++){
				cin>>v[i][j];
				if(v[i][j] > maximum)
					maximum = v[i][j];
			}
			horizontal_rows[i] = maximum;
		}
		for(long long j = 0;j < m;j++){
			long long maximum = 0;
			for(long long i = 0;i < n;i++){
				if(v[i][j] > maximum)
					maximum = v[i][j];
			}
			vertical_coloumns[j] = maximum;
		}
		bool switch_selector = 0;
		for(long long i = 0;i < n;i++){
			for(long long j = 0;j < m;j++){
				if(v[i][j] < horizontal_rows[i] && v[i][j] < vertical_coloumns[j])
					switch_selector = 1;
				if(switch_selector == 1)
					break;
			}
			if(switch_selector == 1)
				break;
		}
		if(switch_selector == 0)
			cout<<"Case #"<<C<<": YES"<<endl;
		else
			cout<<"Case #"<<C<<": NO"<<endl;
	}
	return 0;
}