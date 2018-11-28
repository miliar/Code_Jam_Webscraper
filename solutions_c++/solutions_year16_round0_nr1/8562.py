#include<iostream>
#define ll long long
using namespace std;


int che[10];

bool check()
{
	for (int i = 0; i < 10; i++)
	{
		if (che[i] == 0) return false;
	}
	return true;

}


ll calc(ll N)
{
	if (N == 0) return -1;
	else
	{
		ll count = 0;
		do
		{
			count++;
			ll h=N*count;
			while (h!=0)
			{
				ll temp = h % 10;
				h/= 10;
				che[temp] = 1;
				
				
			}
		} while (!check());

		return count*N;
	}

}


int main() {
	ll T;
	cin >> T;
	for (ll z = 0; z < T;z++)
	{
		for (int i = 0; i < 10; i++) che[i] = 0;
		ll N;
		cin >> N;
		ll output = calc(N);
		cout << "Case #" << z + 1 << ": ";
		if (output!=-1) cout << output << endl;
		else cout << "INSOMNIA" << endl;
	}

	return 0;
}
