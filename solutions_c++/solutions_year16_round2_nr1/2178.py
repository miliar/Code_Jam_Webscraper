#include <bits/stdc++.h>

using namespace std;

#define ll				long long int
#define vi				vector<int>
#define vl				vector<ll>
#define pii				pair<int,int>
#define pil				pair<int, ll>
#define pll				pair<ll, ll>
#define pli				pair<ll, int>
#define pb				push_back
#define mp				make_pair
#define MOD				1000000007
#define F				first
#define S				second

ll pow_mod(ll a, ll b) {
	ll res = 1;
	while(b) {
		if(b & 1)
			res = (res * a);
		a = (a * a);
		b >>= 1;
	}
	return res;
}

int main(){

	ios_base::sync_with_stdio(0);

	int t;
	cin >> t;

	for(int c = 1;c<=t;c++){

		string s;
		cin >> s;
		int n = (int)s.length();

		int count[26];
		for(int i = 0;i<26;i++)
			count[i] = 0;

		for(int i = 0;i<n;i++)
			count[s[i] - 'A'] += 1;

		int ans[10];
		for(int i=0;i<10;i++)ans[i] = 0;
		//Handle zeroes
		ans[0] += count[25];
		count['E' - 'A']-= ans[0];
		count['R' - 'A']-= ans[0];
		count['O' - 'A']-= ans[0];
		count['Z' - 'A'] = ans[0];

		//Handle twos
		ans[2] += count['W' - 'A'];
		count['T' - 'A'] -= ans[2];
		count['W' - 'A'] -= ans[2];
		count['O' - 'A'] -= ans[2];

		//Handle fours
		ans[4] += count['U' - 'A'];
		count['F' - 'A'] -= ans[4];
		count['O' - 'A'] -= ans[4];
		count['U' - 'A'] -= ans[4];
		count['R' - 'A'] -= ans[4];
		//Handle fives
		ans[5] += count['F' - 'A'];
		count['F' - 'A'] -= ans[5];
		count['I' - 'A'] -= ans[5];
		count['V' - 'A'] -= ans[5];
		count['E' - 'A'] -= ans[5];

		//Handle six
		ans[6] += count['X' - 'A'];
		count['S' - 'A'] -= ans[6];
		count['I' - 'A'] -= ans[6];
		count['X' - 'A'] -= ans[6];

		//Handle seven
		ans[7] += count['V' - 'A'];
		count['S' - 'A'] -= ans[7];
		count['E' - 'A'] -= ans[7];
		count['V' - 'A'] -= ans[7];
		count['E' - 'A'] -= ans[7];
		count['N' - 'A'] -= ans[7];

		//Handle eight
		ans[8] += count['G' - 'A'];
		count['E' - 'A'] -= ans[8];
		count['I' - 'A'] -= ans[8];
		count['G' - 'A'] -= ans[8];
		count['H' - 'A'] -= ans[8];
		count['T' - 'A'] -= ans[8];

		//Nine
		ans[9] += count['I' - 'A'];
		count['N' - 'A'] -= ans[9];
		count['I' - 'A'] -= ans[9];
		count['N' - 'A'] -= ans[9];
		count['E' - 'A'] -= ans[9];

		//Three
		ans[3] += count['H' - 'A'];
		count['T' - 'A'] -= ans[3];
		count['H' - 'A'] -= ans[3];
		count['R' - 'A'] -= ans[3];
		count['E' - 'A'] -= ans[3];
		count['E' - 'A'] -= ans[3];

		//One
		ans[1] += count['O' - 'A'];
		count['O' - 'A'] -= ans[1];
		count['N' - 'A'] -= ans[1];
		count['E' - 'A'] -= ans[1];


		cout << "Case #" << c << ": ";
		for(int i=0;i<10;i++){
			while(ans[i]--)
				cout << i;
		}
		cout << "\n";

	}


	return 0;
}
