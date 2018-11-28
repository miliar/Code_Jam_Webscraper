#include <bits/stdc++.h>

using namespace std;
typedef unsigned long long int ULLI;
typedef long long int LLI;

int main(int argc, char** argv)
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int n;
	cin >> n;
	for(int i = 0; i<n; i++)
	{
		vector<bool> num(10, false);
		ULLI count = 0;
		string x;
		cin >> x;
		if(x == "0")
		{
			cout << "Case #" << i+1 << ": INSOMNIA" << endl;
			continue;
		}
		LLI x_num = stoll(x);
		while(std::count(num.begin(), num.end(), true) != 10)
		{
			count++;
			LLI t = x_num * count;
			x = to_string(t);
			for(ULLI k=0; k<x.size(); k++)
				num[x[k] - '0'] = true;		
		}
		cout << "Case #" << i+1 << ": " << count*x_num << endl;
	}
	return 0;
}
