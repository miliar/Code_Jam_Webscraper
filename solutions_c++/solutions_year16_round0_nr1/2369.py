#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>
#include <fstream>
#include <cstring>

using namespace std;
typedef long long LL;

bool a[10];

int assign(LL n) {
	int ret=0;
	while (n>0) {
		int t=n%10;
		if (!a[t]) {
			a[t]=1;
			ret++;
		}
		n/=10;
	}
	return ret;
}

int main() {
	freopen("counting_sheep.in","r",stdin);
	freopen("counting_sheep.out","w",stdout);
	int tc, nt=1;
	cin>>tc;
	while (tc--) {
		LL n;
		cin>>n;
		cout<<"Case #"<<nt++<<": ";
		if (n==0) {
			cout<<"INSOMNIA"<<endl;
			continue;
		}
		memset(a,0,sizeof(a));
		LL c=0, i=1;
		while (c!=10) {
			c+=assign(n*i);
			i++;
		}
		cout<<(1LL*n*(i-1))<<endl;
	}
}
