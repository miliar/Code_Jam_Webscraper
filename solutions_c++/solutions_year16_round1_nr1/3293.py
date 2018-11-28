/*
 * A.cpp
 * 
 * Created by: Ashik <ashik@KAI10>
 * Created on: 2016-04-16 
 */


#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

#define mem(list, val) memset(list, (val), sizeof(list))
#define pb push_back

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("output", "w", stdout);
	
	int t, cs = 0;
	scanf("%d", &t);
	while(t--){
		char str[1005];
		scanf("%s", str);
		
		list<char> ans;
		ans.pb(str[0]);
		for(int i=1; str[i]; i++){
			if(str[i] < *ans.begin()) ans.pb(str[i]);
			else ans.push_front(str[i]);
		}
		
		printf("Case #%d: ", ++cs);
		for(list<char>:: iterator it=ans.begin(); it != ans.end(); it++) printf("%c", *it);
		puts("");
	}

	return 0;
}
