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

bool digits[10];

void countDigits(lli x)
{
	while(x)
	{
		digits[x % 10] = true;
		x = x / 10;
	}
}

int returnDigitCount()
{
	int i, cnt = 0;
	loop(i, 0, 10)
		cnt += digits[i];
	return cnt;
}

int main()
{
    ios_base::sync_with_stdio(false); cin.tie(0);
    lli i, j, k, t, n;
    bool flag;
    cin >> t;
    loope(j, 1, t)
    {
		cin >> n;
		if(n == 0)
		{
			cout << "Case #" << j << ": " << "INSOMNIA\n";
			continue;
		}
		flag = false;
		i = 1; k = n;
		fill(digits, 0);
		while(!flag)
		{
			countDigits(k);
			if(returnDigitCount() == 10) break;
			i++;
			k=i*n;
		}
		cout << "Case #" << j << ": " << k << endl;
	}
	return 0;
}
