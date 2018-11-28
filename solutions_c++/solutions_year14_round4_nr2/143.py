#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;
#define ll long long
#define ld long double
#define vi vector<int>
#define pb push_back
#define pii pair<int,int>
#define mp make_pair
#define st first
#define nd second
#define mini(a,b) a=min(a,(b))
#define maxi(a,b) a=max(a,(b))
#define RE(i,n) for(int i=0,_n=(n);i<_n;++i)
#define RI(i,n) for(int i=1,_n=(n);i<=_n;++i)
const int inf=1e9+5, nax=1e6+5;

int t[nax];

int Test() {
	int res = 0;
	int n;
	cin >> n;
	RI(i, n) cin >> t[i];
	int low = 1, high = n;
	while (low < high) {
		int mi = low;
		for(int i = low; i <= high; ++i)
			if(t[i] < t[mi])
				mi = i;
		// pod mi jest najmniejszy
		if(mi - low < high - mi) {
			// przesuwamy na lewo
			res += mi - low;
			int memo = t[mi];
			for(int i = mi; i > low; --i)
				t[i] = t[i - 1];
			t[low] = memo;
			low++;
		}
		else {
			res += high - mi;
			int memo = t[mi];
			for(int i = mi; i < high; ++i)
				t[i] = t[i + 1];
			t[high] = memo;
			high--;
		}
	}
	return res;
}

int main()
{
	ios_base::sync_with_stdio(0);
	int z;
	cin >> z;
	RI(i, z) {
		cout << "Case #" << i << ": " << Test() << "\n";
	}
	return 0;
}
