#include <bits/stdc++.h>
#define mp make_pair
#define pb push_back

using namespace std;

typedef long long ll;
typedef pair<int,int> pii;
typedef long double ld;
typedef map<ll,ll>::iterator mapit;
typedef set<pii>::iterator setit;
const int maxn = 3e5 + 5;
const int maxlog = 20;
const int inf = 2e9 + 4;
bool a[maxn];
int main()
{
	ios_base::sync_with_stdio(false) , cin.tie(0) , cout.tie(0); cout.precision(20);
	ifstream fin("B-large.in");
	ofstream fout("a.txt");
	int t ; fin >> t;
	for(int test = 1 ; test <= t ; test ++ ){
        string s;
        fin >> s;
        int ans = 0;
        for(int i = 1 ; i < s.size() ; i ++ )
            if(s[i] == '-' && s[i - 1] == '+')
                ans += 2;
        if(s[0] == '-')
            ans ++ ;
        fout << "Case #" << test << ": " << ans << endl;
	}
	return 0;
}
