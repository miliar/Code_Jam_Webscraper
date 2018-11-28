#include<iostream>

using namespace std;

int main()
{
	int T;
	cin>>T;
	for(int i = 1 ; i <= T ; i ++)
	{
		int a,b;
		cin>>a>>b;
		int ans = 0;
		for(int j = a ; j <= b ; j++)
			if(j == 1 || j == 4 || j == 9 || j == 121 || j == 484)
				ans++;
		cout << "Case #" << i << ": " << ans << endl;
	}
}
