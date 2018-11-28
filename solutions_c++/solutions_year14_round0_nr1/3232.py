#include <iostream>
#include <stdio.h>
#include <string>
#include <algorithm>
#include <string.h>
#include <stdlib.h>
#include <ctime>
#define MAXN 300
using namespace std;

int main()
{
	freopen("A-small-attempt7.in", "r", stdin);
	freopen("A.txt", "w", stdout);
    int T, it=1;
    cin>>T;
    while(T--){
		int a, b, ga[MAXN][MAXN], gb[MAXN][MAXN];
		cin >> a;
		for(int i=0; i<4; i++)
			for(int j=0; j<4; j++)
				cin>>ga[i][j];
		cin >> b;
		for(int i=0; i<4; i++)
			for(int j=0; j<4; j++)
				cin>>gb[i][j];
		int cnt=0, ans;
		for(int i=0; i<4; i++)
			for(int j=0; j<4; j++)
				if(ga[a-1][i] == gb[b-1][j])
					cnt ++, ans = ga[a-1][i];
		printf("Case #%d: ", it++);
		if(cnt == 0)
			puts("Volunteer cheated!");
		else if(cnt > 1)
			puts("Bad magician!");
		else
			printf("%d\n", ans);	
	}
    
    return 0;
}

