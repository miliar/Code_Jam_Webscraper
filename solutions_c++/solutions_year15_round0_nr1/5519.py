#include <bits/stdc++.h>


using namespace std;

int main(){
	int T;
	cin >> T;
	for (int i = 1; i <= T; ++i)
	{
		int SM;
		cin >> SM;
		char s[SM+10];
		scanf("%s", s);
		int ans = 0;
		int num = (s[0] - '0');
		for (int j = 1; j <= SM; ++j)
		{
			if(num < j){
				ans += (j - num);
				num += (j - num);
			}
			num += (s[j] - '0');
		}
		printf("case #%d: %d\n", i, ans);

	}


}

