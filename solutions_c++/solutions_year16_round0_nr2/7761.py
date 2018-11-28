#include <bits/stdc++.h>

#define li long int
#define lli long long int
#define loop(i, a, b) for(i=a; i<b; i++)
#define loope(i, a, b) for(i=a; i<=b; i++)
#define loopr(i, a, b) for(i=a; i>b; i--)
#define loopre(i, a, b) for(i=a; i>=b; i--)
#define loopit(i, a) for(i=a.begin(); i!=a.end(); i++)
#define fill(arr, val) memset(arr, val, sizeof(arr))
#define MOD 1000000007
#define eps 0.0000001
#define vi vector<int>
#define vpi vector< pair<int, int> >
#define pi pair<int, int>
#define pb push_back
#define mp make_pair
#define ff first
#define ss second
#define endl '\n'
#define cin fin
#define cout fout

using namespace std;

ifstream fin ("input.in");
ofstream fout ("output.txt");

int main()
{
    ios_base::sync_with_stdio(false); cin.tie(0);
    int i, j, cnt, t;
    string s;
    cin >> t;
    loope(j, 1, t)
    {
		cin >> s;
		if(s[0] == '+') cnt = 0;
		else cnt = 1;
		
		loop(i, 1, s.size())
		{
			if(s[i] == '-' && s[i-1] == '+') cnt++;
		}
		cout << "Case #" << j << ": ";
		if(s[0] == '+')  cout<< 2*cnt << endl;
		else cout<< 2*cnt-1 << endl;
	}
	return 0;
}
