/*
 * pancakes.cpp
 * 
 * Created by: Ashik <ashik@KAI10>
 * Created on: 2016-04-09
 */


#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

#define mem(list, val) memset(list, (val), sizeof(list))
#define pb push_back

char str[105];

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("output", "w", stdout);
	
	int t, cs = 0;
	scanf("%d", &t);
	while(t--){
		scanf("%s", str);
		bool plusOne = false;
		if(str[0] == '-') plusOne = true;
		int strt = 0, count = 0;
		if(plusOne) while(str[strt] == '-') strt++;
		
		for(int i=strt; str[i];){
			if(str[i] == '+') i++;
			else{
				i++;
				count++;
				while(str[i] == '-') i++;
			}
		}
		//cout << count << endl;
		count = (count<<1) + plusOne;
		printf("Case #%d: %d\n", ++cs, count);
	}

	return 0;
}

