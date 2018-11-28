#include <bits/stdc++.h>

#define li long int
#define lli long long int
#define loop(i, a, b) for(i=a; i<b; i++)
#define loope(i, a, b) for(i=a; i<=b; i++)
#define loopr(i, a, b) for(i=a; i>b; i--)
#define loopre(i, a, b) for(i=a; i>=b; i--)
#define fill(arr, val) memset(arr, val, sizeof(arr))
#define MOD 1000000007
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

ifstream fin ("2015qBi.txt");
ofstream fout ("2015qBo.txt");

int a[10001], cnt[10001];
vi v;

int retmax()
{
	int i, m=0;
	loop(i, 0, 1001)
	{
		if(cnt[i]) m=max(m, i);
	}
	return m;
}

void recur(int m, int val, int ans)
{
	int i;
	v.pb(ans+m);
	if(ans>val) return;
	loope(i, 1, m/2)
	{
		cnt[m-i]++; cnt[i]++;
		cnt[m]--;
		recur(retmax(), val, ans+1);
		cnt[m-i]--; cnt[i]--;
		cnt[m]++;
	}
}
int main()
{
    //ios_base::sync_with_stdio(false); cin.tie(0);
	int i, j, t, n, m, ans, val;
	cin>>t;
	loope(j, 1, t)
	{
		cin>>n;
		fill(a, 0);
		fill(cnt, 0);
		v.clear();
		m=ans=0;
		loop(i, 0, n)
		{
			cin>>a[i];
			cnt[a[i]]++;
			m=max(m, a[i]);
		}
		val=m;
		recur(m, val, ans);
		sort(v.begin(), v.end());
		cout<<"Case #"<<j<<": "<<v[0]<<endl;
	}
	return 0;
}
