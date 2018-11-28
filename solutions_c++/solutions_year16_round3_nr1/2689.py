#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cassert>
#include<sstream>
#include<vector>
#include<iterator>
#include<cassert>
#define FORFROM(var, start, end) for(int var = (start); var < (end); ++var)
#define FOR(var, end) FORFROM(var, 0, end)
#define ALL(x) (x).begin(), (x).end()
using namespace std;

struct party{
    char c;
    int n;
};

string solveCase(){
    int N, M=0;
    cin >> N;
    vector<party> P;
    FOR(i, N)
    {
	int n;
	cin >> n;
	M += n;
	P.push_back({'A' + i, n});
    }

    auto cmp = [](party& l, party&r){ return l.n < r.n;};
    make_heap(P.begin(), P.end(), cmp);

    auto pop_party = [&]()
    { 
	pop_heap(P.begin(), P.end(), cmp);
	auto r = P.back();
	P.pop_back();
	return r;
    };

    auto push_party = [&](party const& p)
    { 
	P.push_back(p);
	push_heap(P.begin(), P.end(), cmp);
    };

    auto get_char = [&]()
    {
	pop_heap(P.begin(), P.end(), cmp);
	P.back().n--;
	auto result = P.back().c;
	push_heap(P.begin(), P.end(), cmp);
	return result;
    };

    vector<string> result;
    string cur;
    while(M-- >0)
    {
	cur += get_char();

	assert(cur.size() <= 2);

	if(2 * P[0].n <= M)
	{
	    assert(!cur.empty());

	    result.push_back(cur);
	    cur.clear();
	}
    }
    
    ostringstream sout;
    ostream_iterator<string> out(sout, " ");
    copy(result.begin(), result.end(), out); 
    return sout.str();
}


int main(int argc, char** argv){
    cin.sync_with_stdio(false);
    if(argc > 1){
	    freopen(argv[1], "r", stdin);
    }
    int T;
    cin >> T;
    FOR(c, T){
        cout << "Case #" << (c + 1) << ": " << solveCase() << endl;
    }
}
