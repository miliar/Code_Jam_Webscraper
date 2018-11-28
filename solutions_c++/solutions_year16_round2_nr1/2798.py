#include <bits/stdc++.h>
using namespace std;

#define R(i,a,b) for(int i=a;i<b;i++)
#define RE(i,a,b) for(int i=a;i<=b;i++)
#define RR(i,a,b) for(int i=a;i>b;i--)
#define RRE(i,a,b) for(int i=a;i>=b;i--)
#define F(i,n) for(int i=0;i<n;i++)
#define FE(i,n) for(int i=0;i<=n;i++)
#define FR(i,n) for(int i=n;i>0;i--)
#define FRE(i,n) for(int i=n;i>=0;i--)
#define mp(a,b) make_pair(a,b)
#define pii pair <int, int>
#define pb push_back
#define ft first
#define sd second
#define LL long long
#define gc getchar_unlocked
#define pc putchar_unlocked

inline void get(int &x)
{
    register int c = gc();
    x = 0;
    int neg = 0;
    for(;((c<48 || c>57) && c != '-');c = gc());
    if(c=='-') {neg=1;c=gc();}
    for(;c>47 && c<58;c = gc()) {x = (x<<1) + (x<<3) + c - 48;}
    if(neg) x=-x;
}

int num[12];
int freq[30];

int main()
{
	int T;
	get(T);
	for (int __rep = 1; __rep <=T; __rep++)
	{
		cout << "Case #" << __rep << ": ";
		string s;
		cin >> s;
		int n = s.length();

		memset(freq, 0, sizeof(freq));
		memset(num, 0, sizeof(num));
		F(i,n)
			freq[s[i]-'A']++;

		// Zeros
			num[0] = freq['Z'-'A'];
			freq['Z'-'A'] -= num[0];
			freq['E'-'A'] -= num[0];
			freq['R'-'A'] -= num[0];
			freq['O'-'A'] -= num[0];

		// Twos
			num[2] = freq['W'-'A'];
			freq['W'-'A'] -= num[2];
			freq['T'-'A'] -= num[2];
			freq['O'-'A'] -= num[2];

		// Six
			num[6] = freq['X'-'A'];
			freq['S'-'A'] -= num[6];
			freq['I'-'A'] -= num[6];
			freq['X'-'A'] -= num[6];

		// Eight
			num[8] = freq['G'-'A'];
			freq['E'-'A'] -= num[8];
			freq['I'-'A'] -= num[8];
			freq['G'-'A'] -= num[8];
			freq['H'-'A'] -= num[8];
			freq['T'-'A'] -= num[8];

		// Three
			num[3] = freq['T'-'A'];
			freq['T'-'A'] -= num[3];
			freq['H'-'A'] -= num[3];
			freq['R'-'A'] -= num[3];
			freq['E'-'A'] -= num[3];
			freq['E'-'A'] -= num[3];

		// Four
			num[4] = freq['R'-'A'];
			freq['F'-'A'] -= num[4];
			freq['O'-'A'] -= num[4];
			freq['U'-'A'] -= num[4];
			freq['R'-'A'] -= num[4];

		// Seven
			num[7] = freq['S'-'A'];
			freq['S'-'A'] -= num[7];
			freq['E'-'A'] -= num[7];
			freq['V'-'A'] -= num[7];
			freq['E'-'A'] -= num[7];
			freq['N'-'A'] -= num[7];

		// Five
			num[5] = freq['F'-'A'];
			freq['F'-'A'] -= num[5];
			freq['I'-'A'] -= num[5];
			freq['V'-'A'] -= num[5];
			freq['E'-'A'] -= num[5];

		// One
			num[1] = freq['O'-'A'];
			freq['O'-'A'] -= num[1];
			freq['N'-'A'] -= num[1];
			freq['E'-'A'] -= num[1];

		// Nine
			num[9] = freq['I'-'A'];
			freq['N'-'A'] -= num[9];
			freq['I'-'A'] -= num[9];
			freq['N'-'A'] -= num[9];
			freq['E'-'A'] -= num[9];

		for (int i=0; i<=9; i++)
		{
			for (int j=0; j<num[i]; j++)
				cout << i;
		}
		cout << endl;

	}
	return 0;
}