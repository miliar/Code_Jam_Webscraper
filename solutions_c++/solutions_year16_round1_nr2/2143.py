#include <bits/stdc++.h>
using namespace std;

int main()
{  //freopen("input1.txt","r",stdin);
//	freopen("output1.txt","w",stdout);
	int t; cin >> t; int ntc=0;
	while(t--)
	{  ntc++;
		int n,x;
		int a[2502]={0};
		cin >> n;
		for(int i=0;i<(2*n -1)*n ;i++)
		{
			cin >> x;
			a[x]++;
		}
		cout << "Case #"<<ntc<<": ";
		for(int i=1;i<=2500;i++)
		{ if(a[i]%2) cout << i << " ";}
		 cout << endl;
	}
	return 0;
}
	
	
