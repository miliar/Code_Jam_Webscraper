#include <bits/stdc++.h>
#include <windows.h>

#define f first
#define s second
#define ll long long
#define ld long double
#define pb push_back
#define files1 freopen("input.txt","r",stdin)
#define files2 freopen("output.txt","w",stdout)
#define mp make_pair
#define fast_io ios_base::sync_with_stdio(0);
#define forn() for(int i=0;i<n;i++)
#define vi vector<int>
#define pii pair<int,int>

using namespace std;

const int inf = 2e9;
const double eps = 1e-9;
const int maxn = 1e4 + 5, base = 1e9+7;

void bad(string mes = "NO"){cout << mes;exit(0);}

template<typename T>
string bin(T x){
	string ans = "";
	while (x > 0){
		ans += char('0' + x % 2);
		x /= 2;
	}
	reverse(ans.begin(), ans.end());
	return ans.empty() ? "0" : ans;
}

template<typename T = int >
T input(){
	T ans = 0, m = 1;
	char c = ' ';
	while (c == ' ' || c == '\n')
		c = getchar();
	if (c == '-')
		m = -1,	c = getchar();
	while (c != ' ' && c != '\n')
		ans = ans * 10 + c - '0', c = getchar();
	return ans * m;
}

template<typename T>
T sqr(T x)
{
	return x * x;
}


bool Try(vector<int> & cnt, int x)
{
    if (x == 0){
        if (cnt['Z' - 'A'] && cnt['E' - 'A'] && cnt['R' - 'A'] && cnt['O' - 'A']){
            cnt['Z' - 'A']--;
            cnt['E' - 'A']--;
            cnt['R' - 'A']--;
            cnt['O' - 'A']--;
            return 1;
        } else
        return 0;
    }

    if (x == 1){
        if (cnt['O' - 'A'] && cnt['N' - 'A'] && cnt['E' - 'A']){
            cnt['O' - 'A']--;
            cnt['N' - 'A']--;
            cnt['E' - 'A']--;
            return 1;
        } else
        return 0;
    }
    if (x == 2){
        if (cnt['T' - 'A'] && cnt['W' - 'A'] && cnt['O' - 'A']){
            cnt['T' - 'A']--;
            cnt['W' - 'A']--;
            cnt['O' - 'A']--;
            return 1;
        } else
        return 0;
    }
    if (x == 3){
        if (cnt['T' - 'A'] && cnt['H' - 'A'] && cnt['R' - 'A'] && cnt['E' - 'A'] >= 2){
            cnt['T' - 'A']--;
            cnt['H' - 'A']--;
            cnt['R' - 'A']--;
            cnt['E' - 'A']-=2;
            return 1;
        } else
        return 0;
    }
    if (x == 4){
        if (cnt['F' - 'A'] && cnt['O' - 'A'] && cnt['U' - 'A'] && cnt['R' - 'A']){
            cnt['F' - 'A']--;
            cnt['O' - 'A']--;
            cnt['U' - 'A']--;
            cnt['R' - 'A']--;
            return 1;
        } else
        return 0;
    }
    if (x == 5){
        if (cnt['F' - 'A'] && cnt['I' - 'A'] && cnt['V' - 'A'] && cnt['E' - 'A']){
            cnt['F' - 'A']--;
            cnt['I' - 'A']--;
            cnt['V' - 'A']--;
            cnt['E' - 'A']--;
            return 1;
        } else
        return 0;
    }
    if (x == 6){
        if (cnt['S' - 'A'] && cnt['I' - 'A'] && cnt['X' - 'A']){
            cnt['S' - 'A']--;
            cnt['I' - 'A']--;
            cnt['X' - 'A']--;
            return 1;
        } else
        return 0;
    }
    if (x == 7){
        if (cnt['S' - 'A'] && cnt['N' - 'A'] && cnt['V' - 'A'] && cnt['E' - 'A'] >= 2){
            cnt['S' - 'A']--;
            cnt['V' - 'A']--;
            cnt['N' - 'A']--;
            cnt['E' - 'A']-=2;
            return 1;
        } else
        return 0;
    }
    if (x == 8){
        if (cnt['E' - 'A'] && cnt['I' - 'A'] && cnt['G' - 'A'] && cnt['H' - 'A'] && cnt['T' - 'A']){
            cnt['E' - 'A']--;
            cnt['I' - 'A']--;
            cnt['G' - 'A']--;
            cnt['H' - 'A']--;
            cnt['T' - 'A']--;
            return 1;
        } else
        return 0;
    }
    if (x == 9){
        if (cnt['E' - 'A'] && cnt['I' - 'A'] && cnt['N' - 'A'] >= 2){
            cnt['E' - 'A']--;
            cnt['I' - 'A']--;
            cnt['N' - 'A']-=2;
            return 1;
        } else
        return 0;
    }
}

bool solve1(vector<int> & cnt, int last, string & ans)
{
    if (cnt == vector<int>(26, 0))
        return 1;
    vector<int> save = cnt;
    for (int our = last; our <= 9; our++){
        if (Try(cnt, our) && solve1(cnt, our, ans)){
            ans += (char)(our + '0');
            return 1;
        } else cnt = save;
    }
    return 0;
}
void solve()
{
    string ans = "";
    string s;
    cin >> s;
    vector<int> cnt;
    cnt.assign(26, 0);
    for (int i = 0; i < s.size(); i++){
        cnt[s[i] - 'A']++;
    }

    vector<int> save = cnt;
    for (int f = 0; f <= 9; f++){
        if (Try(cnt, f) && solve1(cnt, f, ans)){
            ans += (char)(f + '0');
            reverse(ans.begin(), ans.end());
            cout << ans << "\n";
            break;
        } else cnt = save;
    }
}
int main()
{
    files1;
    files2;
    int t;
    fast_io;
    cin >> t;

    for (int i = 0; i < t; i++){
        cout << "Case #" << i + 1 << ':' << ' ';
        solve();
    }
}
