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

int main() {
	ios_base::sync_with_stdio(false); cin.tie(0);
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);

    int t;
    string s;
	cin >> t;

	forn(j,t){
        cin >> s;
        string word; word += s[0];

        forsn(i,1,si(s)){
            if(s[i]+word >= word+s[i]){
                word=s[i]+word;
                continue;
            }
            word=word+s[i];
        }

        cout << "Case #" << j+1 << ": " << word << endl;
	}

	return 0;
}
