#include <bits/stdc++.h>
using namespace std;
#define int long long
int arr[1005]; 
int ceilt (int a, int b)
{
	if (a%b==0) return a/b;
	else return a/b+1; 
}
main()
{
	freopen("in.txt", "r", stdin); 
	freopen("out.txt", "w", stdout); 
	int a; cin >> a;
	for (int g=0; g<a; g++)
	{
		int b; cin >> b;
		int sume=0; 
		for (int y=1; y<=b; y++) {cin >> arr[y]; sume+=arr[y];} 
		int answer=1e9; 
		for (int t=1; t<=1000; t++)
		{
			int check=0;
			for (int z=1; z<=b; z++)
			{
				check+=ceilt(arr[z], t)-1; 
			} 
			if (check+t<answer) answer=check+t; 
		}
		cout << "Case #" << g+1 << ": " << answer << '\n';
	}
	return 0; 
}
