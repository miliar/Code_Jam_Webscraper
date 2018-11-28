#include <bits/stdc++.h>
using namespace std;

char equiv[] = "PRS";
long long arr[15][3][3];
char buffer[1<<15];

string f(int n, int k)
{
	if(n==0)
	{
		string ret;
		ret += equiv[k];
		return ret;
	}

	string a = f(n-1,k);
	string b = f(n-1,(k+1)%3);
	if(a>b)
		swap(a,b);
	return a+b;
}

int main()
{
	for(int i=0; i<3; i++)
		for(int j=0; j<3; j++)
			arr[0][i][j] = i==j?1:0;
	for(int i=1; i<=14; i++)
		for(int j=0; j<3; j++)
			for(int k=0; k<3; k++)
				arr[i][j][k] = arr[i-1][j][k]+arr[i-1][(j+1)%3][k];

	int t;
	cin >> t;

	for(int cn=1; cn<=t; cn++)
	{
		int n,r,p,s;
		cin >> n >> r >> p >> s;

		int supp[3] = {p,r,s};
		int valid = -1;
		for(int i=0; i<3; i++)
		{
			bool check = true;
			for(int j=0; j<3; j++)
				if(arr[n][i][j]!=supp[j])
				{
					check = false;
					break;
				}

			if(check)
			{
				valid = i;
				break;
			}
		}
		if(valid==-1)
		{
			cout << "Case #" << cn << ": IMPOSSIBLE" << endl;
			continue;
		}

		cout << "Case #" << cn << ": " << f(n,valid) << endl;
	}

	return 0;
}