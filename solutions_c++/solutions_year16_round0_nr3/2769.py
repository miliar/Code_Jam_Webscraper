#include <bits/stdc++.h>
using namespace std;
#define max(a,b) ((a) > (b) ? (a) : (b))
#define min(a,b) ((a) < (b) ? (a) : (b))
#define abs(x) ((x) < 0 ? -(x) : (x))


struct dat{
	string bn;
	long long dv[11];
};
vector <dat> ans;
dat tmp;
string tobinary(long long x) {
	string ret;
	while (x>0) {
		if (x&1) ret.insert(0,"1");
		else ret.insert(0,"0");
		x>>=1;
	}
	return ret;
}

long long getdiv(long long x) {
	for (long long i=2;i*i<=x;++i) {
		if (x%i==0) return i;
	}
	return -1;
}

long long cnv(long long x, long long b) {
	long long t=1; long long ret=0;
	while (x>0) {
		if (x&1) ret+=t;
		t*=b;
		x>>=1;
	}
	return ret;
}
int dum;
long long num,baseconv;
bool ok;
int j=50;
int main()
{
	cin.sync_with_stdio(0);
	cin >> dum >> dum >> dum;
	cout << "Case #1:\n";
	num=32769;
	while (j>0) {
		tmp.bn=tobinary(num);
		ok=true;
		for (int i=2;i<=10;++i) {
			baseconv=cnv(num,i);
			tmp.dv[i]=getdiv(baseconv);
			if (tmp.dv[i]==-1) {
				ok=false;
				break;
			}
		}
		if (ok) {
			--j;
			//cout << "found\n";
			ans.push_back(tmp);
		}
		num+=2;
	}
	for (int i=0;i<50;++i) {
		cout << ans[i].bn;
		for (int k=2;k<=10;++k) cout << ' ' << ans[i].dv[k];
		cout << '\n';
	}
	return 0;
}

