#include <bits/stdc++.h>

#define ll long long
#define ff first
#define ss second
#define mp make_pair

using namespace std;

typedef pair < ll , ll > pie;
int num[16];
ll numb[11];
ll div_[11];
void pp()
{
	num[0] += 2;
	for(int i = 0; i < 15; i++)
		if(num[i] >= 2)
		{
			num[i] -= 2;
			num[i+1] ++;
		}
	return;
}
ll fprm(ll tmp)
{
	for(ll i = 2; i <= sqrt(tmp); i++)
		if(tmp % i == 0)
			return i;
	return tmp;
}
void set_numb()
{
	for(int i = 2; i < 11; i++)
	{
		ll t = 0;
		for(int j = 15; j >= 0; j--)
			t = t * i + num[j];
		numb[i] = t;
		div_[i] = fprm(numb[i]);
	}
	return;
}
int main()
{
	ios_base::sync_with_stdio(false);
	string a1,a2,a3;
	cin >> a1 >> a2 >> a3;
	num[15] = num[0] = 1;
	cout << "Case #1:\n";
	int wtf = 0;
	ll ship = 0;
	while(wtf < 50)
	{
		cerr << ship <<" ";
		ship ++; 
		set_numb();
		bool shit = false;
		for(int i = 2; i < 11; i++)
			if(div_[i] == numb[i])
				shit = true;
		if(!shit)
		{
			for(int i = 15; i >= 0; i--)
				cout << num[i];
			for(int i = 2; i < 11; i++)
				cout << " " << div_[i];
			cout << endl;
			wtf++;
		}
		pp();
	}
	cerr << endl;
	return 0;
}