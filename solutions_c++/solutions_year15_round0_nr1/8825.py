#include<iostream>
#include<cstdio>
#include<string>

using namespace std;

int main() 
{
	int t;
	scanf("%d",&t);
	for(int l = 1 ; l <= t; l++) {
		int max;
		scanf("%d",&max);

		string s;
		cin >> s;
		int req = 0;
		int currTot = 0;
		for (int i = 0 ; i <= max ; i++) {
			int audience = s[i]-'0';
			if(i > currTot) {
				int diff = i - currTot;
				req = req + diff;
				audience = audience + diff;
			}
			currTot = currTot + audience;
		}
		printf("Case #%d: %d\n",l,req);
	}


}