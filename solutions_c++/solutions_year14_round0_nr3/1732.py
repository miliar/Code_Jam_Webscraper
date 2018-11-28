#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>
#include <climits>
#include <cfloat>
#include <ctime>
#include <map>
#include <utility>
#include <set>
#include <memory>
#include <functional>
#include <sstream>
#include <complex>
#include <stack>
#include <queue>

using namespace std;

#define rep(i,b,e) for(int i=b;i<e;++i)
#define mp make_pair
#define pb push_back
#define all(c) (c).begin(),(c).end()

typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> pii;

static const ll Zp = 1000000009;
static const double EPS = 1e-9;

static const char* IMP = "Impossible";

int T;

void printans(vector<string> ans)
{
    for (int i=0; i<ans.size(); ++i) {
        cout<<ans[i]<<endl;
    }
}

void printans2(vector<string> ans)
{
    for (int i=0; i<ans[0].size(); ++i) {
        for (int j=0; j<ans.size(); ++j) {
            cout<<ans[j][i];
        }
        cout<<endl;
    }
}

pair<vector<string>, bool> solve_m0(int r, int c)
{
    vector<string> ans;

    for (int i=0; i<r; ++i) {
        string rs;
        for (int j=0; j<c; ++j) {
            rs.push_back('.');
        }
        ans.push_back(rs);
    }
    ans[0][0] = 'c';
    return make_pair(ans,true) ;
}

pair<vector<string>, bool>  solve_mm(int r, int c)
{
    vector<string> ans;

    for (int i=0; i<r; ++i) {
        string rs;
        for (int j=0; j<c; ++j) {
            rs.push_back('*');
        }
        ans.push_back(rs);
    }
    ans[0][0] = 'c';
    return  make_pair(ans,true) ;
}

pair<vector<string>, bool> solve_rc1(int r, int c, int m)
{
    int l = std::max(r,c);
    string rs;
    for (int i=0; i<(l-m); ++i) {
        rs.push_back('.');
    }
    for (int i=0; i<m; ++i) {
        rs.push_back('*');
    }
    rs[0] = 'c';
    vector<string> ans;
    ans.push_back(rs);
    return make_pair(ans, (r==1));
}

pair<vector<string>, bool> solve_rc2(int r, int c, int m)
{
    if (m==0) return solve_m0(r,c);
    if (m == (r*c-1)) return solve_mm(r,c);

    vector<string> ans;
    if ((m%2) != 0) {
        ans.push_back(IMP);
        return make_pair(ans, true);
    }
    if ((r*c-m) < 4) {
        ans.push_back(IMP);
        return make_pair(ans, true);
    }
    int l = std::max(r,c);
    for (int i=0; i<(l-m/2); ++i) {
        ans.push_back("..");
    }
    for (int i=0; i<m/2; ++i) {
        ans.push_back("**");
    }
    ans[0][0] = 'c';
    return make_pair(ans, (c==2));

}

pair<vector<string>, bool>  solve_rc3(int r, int c, int m)
{
    if (m==0) return solve_m0(r,c);
    if (m == (r*c-1)) return solve_mm(r,c);

    vector<string> ans;
    int l = std::max(r,c);
    if (r == 3 && c == 3 && m == 2) {
        ans.push_back(IMP);
        return make_pair(ans, true);
    }
    if (r==3 && c==5 && m==4) {
        ans.push_back("c...*");
        ans.push_back("....*");
        ans.push_back("...**");
        return make_pair(ans, true);
    }
    if (r==5 && c==3 && m==4) {
        ans.push_back("c..");
        ans.push_back("...");
        ans.push_back("...");
        ans.push_back("..*");
        ans.push_back("***");
        return make_pair(ans, true);
    }
    if ((m%3) == 0) {
        int ml = m/3;
        if (l-ml < 2) {
            ans.push_back(IMP);
            return make_pair(ans, true);
        }
        for (int i=0; i<l-ml; ++i) {
            ans.push_back("...");
        }
        for (int i=0; i<ml; ++i) {
            ans.push_back("***");
        }
        ans[0][0] = 'c';
        return make_pair(ans, (c==3));
    } else if (m >= l) {
        std::pair<vector<string>, bool> ap = solve_rc2(l, 2, m-l);
        if ( (ap.first)[0] == IMP ) return ap;
        for (int i=0; i<l; ++i) {
            (ap.first)[i].push_back('*');
        }
        return make_pair(ap.first, (c==3));
    }
    for (int i=0; i<l; ++i) {
        ans.push_back("...");
    }
    ans[0][0] = 'c';
    ans[l-1][2] = '*';
    if (m==2) ans[l-2][2] = '*';

    return make_pair(ans,(c==3));
}

pair<vector<string>, bool>  solve_rc4(int r, int c, int m)
{
    if (m==0) return solve_m0(r,c);
    if (m == (r*c-1)) return solve_mm(r,c);

    vector<string> ans;
    if (r==4 && c==5 && m==4) {
        ans.push_back("c...");
        ans.push_back("....");
        ans.push_back("....");
        ans.push_back("....");
        ans.push_back("****");
        return make_pair(ans, false);
    }
    if (r==5 && c==4 && m==4) {
        ans.push_back("c...");
        ans.push_back("....");
        ans.push_back("....");
        ans.push_back("....");
        ans.push_back("****");
        return make_pair(ans, true);
    }
    int l = std::max(r,c);
    if (m >= l) {
        std::pair<vector<string>, bool> ap = solve_rc3(l, 3, m-l);
        if ( (ap.first)[0] == IMP ) return ap;
        for (int i=0; i<l; ++i) {
            (ap.first)[i].push_back('*');
        }
        return make_pair(ap.first, (r>4));
    }

    for (int i=0; i<l; ++i) {
        ans.push_back("....");
    }
    ans[0][0] = 'c';
    ans[l-1][3] = '*';
    if (m>=2) ans[l-2][3] = '*';
    if (m>=3) ans[l-1][2] = '*';

    return make_pair(ans,(r>4));
}

pair<vector<string>, bool>  solve_rc5(int r, int c, int m)
{
    if (m==0) return solve_m0(r,c);
    if (m == (r*c-1)) return solve_mm(r,c);
    vector<string> ans;
    int l = std::max(r,c);
    if (m >= l) {
        std::pair<vector<string>, bool> ap = solve_rc4(l, 4, m-l);
        if ( (ap.first)[0] == IMP )return ap;
        for (int i=0; i<l; ++i) {
            (ap.first)[i].push_back('*');
        }
        return make_pair(ap.first, (r>5));
    }

    for (int i=0; i<l; ++i) {
        ans.push_back(".....");
    }
    ans[0][0] = 'c';
    ans[l-1][4] = '*';
    if (m>=2) ans[l-2][4] = '*';
    if (m>=3) ans[l-3][4] = '*';
    if (m>=4) ans[l-1][3] = '*';

    return make_pair(ans,(r>5));
}

int main(int argc, char *argv[]) {
    cin>>T;
    for(int t=1;t<=T;++t) {
        int R,C,M;
        cin >> R >> C >> M;
        cout<<"Case #"<<t<<":"<<endl;

        std::pair<vector<string>, bool> ap;

        if (M==0) ap = solve_m0(R,C);
        else if (M == (R*C-1)) ap = solve_mm(R,C);
        else if(R==1 || C==1) ap = solve_rc1(R,C,M);
        else if(R==2 || C==2) ap = solve_rc2(R,C,M);
        else if(R==3 || C==3) ap = solve_rc3(R,C,M);
        else if(R==4 || C==4) ap = solve_rc4(R,C,M);
        else if(R==5 || C==5) ap = solve_rc5(R,C,M);

        if (ap.second) printans(ap.first);
        else printans2(ap.first);
    }
	return 0;
}
