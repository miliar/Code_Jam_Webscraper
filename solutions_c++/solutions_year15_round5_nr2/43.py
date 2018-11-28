// another fine solution by misof
// #includes {{{
#include <algorithm>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <tuple>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>

#include <cassert>
#include <cctype>
#include <cstdio>
#include <cstdlib>
#include <cstring>

#include <cmath>
#include <complex>
using namespace std;
// }}}

/////////////////// PRE-WRITTEN CODE FOLLOWS, LOOK DOWN FOR THE SOLUTION ////////////////////////////////

// pre-written code {{{
// BEGIN CUT HERE
#define DEBUG(var) { cout << #var << ": " << (var) << endl; }
template <class T> ostream& operator << (ostream &os, const vector<T> &temp) { os << "[ "; for (unsigned int i=0; i<temp.size(); ++i) os << (i?", ":"") << temp[i]; os << " ]"; return os; } // DEBUG
template <class T> ostream& operator << (ostream &os, const set<T> &temp) { os << "{ "; for(__typeof((temp).begin()) it=(temp).begin();it!=(temp).end();++it) os << ((it==(temp).begin())?"":", ") << (*it); os << " }"; return os; } // DEBUG
template <class T> ostream& operator << (ostream &os, const multiset<T> &temp) { os << "{ "; for(__typeof((temp).begin()) it=(temp).begin();it!=(temp).end();++it) os << ((it==(temp).begin())?"":", ") << (*it); os << " }"; return os; } // DEBUG
template <class S, class T> ostream& operator << (ostream &os, const pair<S,T> &a) { os << "(" << a.first << "," << a.second << ")"; return os; } // DEBUG
template <class S, class T> ostream& operator << (ostream &os, const map<S,T> &temp) { os << "{ "; for(__typeof((temp).begin()) it=(temp).begin();it!=(temp).end();++it) os << ((it==(temp).begin())?"":", ") << (it->first) << "->" << it->second; os << " }"; return os; } // DEBUG
namespace aux{
    template<std::size_t...> struct seq{};
    template<std::size_t N, std::size_t... Is> struct gen_seq : gen_seq<N-1, N-1, Is...>{};
    template<std::size_t... Is> struct gen_seq<0, Is...> : seq<Is...>{};
    template<class Ch, class Tr, class Tuple, std::size_t... Is> void print_tuple(std::basic_ostream<Ch,Tr>& os, Tuple const& t, seq<Is...>) { using swallow = int[]; (void)swallow{0, (void(os << (Is == 0? "" : ", ") << std::get<Is>(t)), 0)...}; }
} // aux::
template<class Ch, class Tr, class... Args> auto operator<<(std::basic_ostream<Ch, Tr>& os, std::tuple<Args...> const& t) -> std::basic_ostream<Ch, Tr>& { os << "("; aux::print_tuple(os, t, aux::gen_seq<sizeof...(Args)>()); return os << ")"; }
// END CUT HERE
#define FOR(i,a,b) for(int i=(int)(a);i<=(int)(b);++i)
#define REP(i,n) for(int i=0;i<(int)(n);++i)
#define SIZE(t) ((int)((t).size()))
// }}}

/////////////////// CODE WRITTEN DURING THE COMPETITION FOLLOWS ////////////////////////////////

long long eval(const vector<pair<long long,long long> > &intervaly) {
    long long mn=intervaly[0].first, mx=intervaly[0].second;
    for (auto in:intervaly) {
        mn = min(mn,in.first);
        mx = max(mx,in.second);
    }
    return mx-mn;
}

long long how_much_shift_right(vector<pair<long long,long long> > &intervaly) {
    long long max_right = intervaly[0].second;
    REP(i,SIZE(intervaly)) max_right = max( max_right, intervaly[i].second );
    long long answer = 0;
    REP(i,SIZE(intervaly)) answer += max_right - intervaly[i].second;
    return answer;
}

/*
long long how_much_shift_left(vector<pair<long long,long long> > &intervaly) {
    long long min_left = intervaly[0].second;
    REP(i,SIZE(intervaly)) max_right = max( max_right, intervaly[i].second );
    long long answer = 0;
    REP(i,SIZE(intervaly)) answer += max_right - intervaly[i].second;
    return answer;
}
*/

void shift_right(vector<pair<long long,long long> > &intervaly) {
    int kto = 0;
    REP(i,SIZE(intervaly)) {
        if (intervaly[i].second < intervaly[kto].second) kto = i;
        if (intervaly[i].second == intervaly[kto].second) if (intervaly[i].first < intervaly[kto].first) kto = i;
    }
    ++intervaly[kto].first;
    ++intervaly[kto].second;
}

void shift_left(vector<pair<long long,long long> > &intervaly) {
    int kto = 0;
    REP(i,SIZE(intervaly)) {
        if (intervaly[i].first > intervaly[kto].first) kto = i;
        if (intervaly[i].first == intervaly[kto].first) if (intervaly[i].second > intervaly[kto].second) kto = i;
    }
    --intervaly[kto].first;
    --intervaly[kto].second;
}

int main() {
    int T; cin >> T;
    FOR(t,1,T) {
        int N, K;
        cin >> N >> K;
        vector<long long> S(N-K+1);
        for (auto &s:S) cin >> s;
        vector< pair<long long,long long> > intervaly;
        for (int k=0; k<K; ++k) {
            long long cur=(k==K-1 ? S[0] : 0);
            long long mn=cur, mx=cur;
            int kde=k;
            while (true) {
                if (kde+K >= N) break;
                cur = cur + S[kde+1] - S[kde];
                kde += K;
                mn = min(mn,cur);
                mx = max(mx,cur);
            }
            intervaly.push_back( {mn,mx} );
        }
        /*
        DEBUG("");
        DEBUG(intervaly);
        DEBUG(SIZE(intervaly));
        vector<int> dlzky;
        for (auto in:intervaly) dlzky.push_back(in.second - in.first);
        DEBUG(dlzky);
        */
        // align all the intervals approximately
        long long csum = 0;
        for (auto in:intervaly) csum += in.first + in.second;
        long long stred = (csum + N)/(2*N);
        long long delta = 0;
        for (auto &in:intervaly) {
            long long posun = stred - (in.first+in.second)/2;
            delta += posun;
            in.first += posun;
            in.second += posun;
        }
        while (delta > 0) { --delta; shift_left(intervaly); }
        while (delta < 0) { ++delta; shift_right(intervaly); }
        //DEBUG(intervaly);

        long long minleft = intervaly[0].first;
        for (auto &in:intervaly) minleft = min( minleft, in.first );

        long long answer = eval(intervaly);

        for (int left = minleft-10; left <= minleft+10; ++left) {
            // shift all intervals left
            delta = 0;
            vector<long long> posuny;
            for (auto &in:intervaly) {
                long long posun = left - in.first;
                delta += posun;
                in.first += posun;
                in.second += posun;
                posuny.push_back(posun);
            }
            /*
            while (delta > 0) { --delta; shift_left(intervaly); }
            while (delta < 0) { ++delta; shift_right(intervaly); }
            */
            if (delta < 0 && how_much_shift_right(intervaly) + delta >= 0) answer = min( answer, eval(intervaly) );
            REP(i,SIZE(intervaly)) {
                intervaly[i].first -= posuny[i];
                intervaly[i].second -= posuny[i];
            }
        }

        REP(loop,1000) {
            shift_left(intervaly);
            shift_right(intervaly);
            answer = min( answer, eval(intervaly) );
        }
        cout << "Case #" << t << ": " << answer << endl;
    }
}
// vim: fdm=marker:commentstring=\ \"\ %s:nowrap:autoread
