#include <bits/stdc++.h>
using namespace std;

#define forn(i,n) for(int i=0;i<int(n);i++)
#define forsn(i,s,n) for(int i=(int)(s);i<(int)(n);i++)
#define dforsn(i,s,n) for(int i=(int)(n-1);i>=int(s);i--)
#define si(a) ((int)(a).size())
#define pb push_back
#define mp make_pair
#define endl '\n'
#define all(a) a.begin(),a.end()
typedef vector<int> vi;
typedef pair<int,int> pii;
typedef long long int tint;

vi res;
string numb[] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
map<char,int> lett;
int r;

bool calc(int dig, map<char,int> remain){
    if(dig == 9){
        int maxam = r/si(numb[dig]);
        set<char>ch;
        forn(i,si(numb[dig])){
            int half = 1;
            if(ch.find(numb[dig][i])!=ch.end())half=2;
            maxam = min(maxam,remain[numb[dig][i]]/half);
            ch.insert(numb[dig][i]);
        }
        if(si(numb[dig])*maxam==r){
            forn(i,maxam)res.pb(dig);
            return true;
        }
        return false;
    }
    int maxam = r/si(numb[dig]);
    forn(i,si(numb[dig])){
        maxam = min(maxam,remain[numb[dig][i]]);
    }

    if(si(numb[dig])*maxam==r){
            forn(i,maxam)res.pb(dig);
            return true;
    }
    int auxr = r;
    forn(i,maxam+1){
        if(calc(dig+1,remain))return true;
        if(i == maxam)continue;
        res.pb(dig);
        forn(j,si(numb[dig])){
            remain[numb[dig][j]]--;
            r--;
        }
        if(r==0)return true;
    }

    r= auxr;
    forn(j,maxam){
            res.pop_back();
        }
    return false;
}

int main() {
	ios_base::sync_with_stdio(false); cin.tie(0);
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);

	int t;
	string s;
	cin >> t;

	forn(k,t){
	    res.clear();
	    lett.clear();
        cin >> s;
        forn(i,si(s)){
            lett[s[i]]++;
        }
        r=si(s);
        bool a =calc(0,lett);
        sort(all(res));
        cout << "Case #" << k+1 << ": ";
        forn(i,si(res))cout << res[i];
        cout << endl;
	}


	return 0;
}
