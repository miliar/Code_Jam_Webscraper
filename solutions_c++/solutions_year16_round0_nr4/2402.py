/*
 * fractiles_easy.cpp
 * 
 * Created by: Ashik <ashik@KAI10>
 * Created on: 2016-04-09
 */


#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

#define mem(list, val) memset(list, (val), sizeof(list))
#define pb push_back

int main()
{
	freopen("D-small-attempt0.in", "r", stdin);
	freopen("output", "w", stdout);
	
	int t, cs = 0;
	scanf("%d", &t);
	while(t--){
		int k,c,s;
		scanf("%d %d %d", &k, &c, &s);
		printf("Case #%d:", ++cs);
		for(int i=1; i<=k; i++) printf(" %d", i);
		puts("");
	}

	return 0;
}

