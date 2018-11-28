#include <cstdlib>
#include <cmath>
#include <map>
#include <utility>
#include <set>
#include <sstream>
#include <iostream>
#include <iterator>
#include <string>
#include <vector>
#include <list>
#include <algorithm>
#include <functional>
#include <stack>
#include <queue>
#include <numeric>
using namespace std;

#define	mp						make_pair
#define	pb						push_back
#define	bg						begin
#define	ed						end
#define	fs						first
#define	sc						second
#define	sz(x)					((int)((x).size()))
#define	For(i,a,b)				for(int i=(a);i<(b);++i)
#define	rep(i,n)				For(i,0,(n))
#define	rFor(i,a,b)				for(int i=(a);i>=(b);--i)
#define	rrep(i,n)				rFor(i,(n),0)
#define	all(v)					(v).begin(),(v).end()
#define	ITER(type)				type::iterator
#define	EACH(type,cont,it)		for(ITER(type) it=(cont).bg,s___=(cont).ed;it!=s___;++it)

typedef	long long				LL;
typedef	vector<int>				VI;
typedef	vector<LL>				VLL;
typedef	vector<vector<int> >	VVI;
typedef	vector<bool>			VB;
typedef	vector<string>			VS;
typedef	list<int>				LI;
typedef	list<LL>				LLL;
typedef	list<string>			LS;
typedef	pair<int,int>			PII;

int mergecount(VI &a) {
	int count = 0;
	int n = a.size();
	if(n > 1) {
		VI b(a.bg(), a.bg() + n / 2);
		VI c(a.bg() + n / 2, a.ed());

		count += mergecount(b);
		count += mergecount(c);

		int j = 0, k = 0;
		rep(i, n) {
			if(k == c.size()) {
				a[i] = b[j++];
			} else if(j == b.size()) {
				a[i] = c[k++];
			} else if(b[j] <= c[k]) {
				a[i] = b[j++];
			} else {
				a[i] = c[k++];
				count += n / 2 - j;
			}
		}
	}
	return count;
}

int check(const vector<PII> &seq)
{
	int pos = 1;

	while(pos < seq.size() && seq[pos-1].fs < seq[pos].fs)
		++pos;
	while(pos < seq.size() && seq[pos-1].fs > seq[pos].fs)
		++pos;
	if(pos != seq.size())
		return 1 << 30;

	VI tmp(seq.size());
	rep(i, seq.size())
		tmp[seq[i].sc] = i;

	return mergecount(tmp);
}

int solve()
{
	int N;

	cin >> N;

	VI A(N);
	rep(i, N)
		cin >> A[i];

	int res = 1 << 30;
	vector<PII> seq;

	rep(i, A.size())
		seq.pb(mp(A[i], i));
	sort(all(seq));
	do {
		res = min(res, check(seq));
	} while(next_permutation(all(seq)));

	return res;
}

int main( void )
{
	int T;

	cin >> T;
	rep(i, T)
		cout << "Case #" << (i + 1) << ": " << solve() << endl;
}
