#include<cstdio>
#include<iostream>
#include<cstring>
#include<string>
#include<cstdlib>
using namespace std;

int main()
{
	int t;
	
	freopen("A-large.in", "r", stdin);
	freopen("alargeout.txt", "w", stdout);
	scanf("%d", &t);

	//cout << t << endl;
	int cse = 1;

	while (t--) {

		int n;
		scanf("%d", &n);

		string str;
		cin >> str;

		int sum = 0;
		int ans=0, k=0;

		for (int i = 0; i < n + 1; i++) {
			//sum += (str[i] - '0');
			if (str[i] - '0' == 0) {
				continue;
			} 
			if (str[i] - '0' > 0 && sum<i) {
				k = i - sum;
				ans+=k;
				sum += k + (str[i] - '0');
				
			}
			else{
				sum += (str[i] - '0');
			}
		}

		printf("Case #%d: %d\n", cse++, ans);
	}
	
	fclose(stdin);
	fclose(stdout);
	return 0;
}