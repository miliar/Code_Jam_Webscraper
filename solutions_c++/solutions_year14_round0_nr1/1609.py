#include <iostream>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <climits>
#include <algorithm>
#include <map>
#include <vector>

using namespace std;


int cnt[20];

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
	int T = 0, Cas = 0, n;
	scanf("%d",&T); 
    while(T--)
    {
      	memset(cnt, 0, sizeof(cnt));
      	scanf("%d",&n);
      	for(int i = 1; i <= 4; i++) {
      		for(int j = 1;j <= 4; j++) {
      			int t;
      			scanf("%d", &t);
      			if(i == n) {
      				cnt[t]++;
      			}
      		}
      	}

      	scanf("%d",&n);
      	for(int i = 1; i <= 4; i++) {
      		for(int j = 1;j <= 4; j++) {
      			int t;
      			scanf("%d", &t);
      			if(i == n) {
      				cnt[t]++;
      			}
      		}
      	}
      	int  num = 0, ans = -1;
      	for(int i = 1; i <= 16; i++) {
      		if(cnt[i] == 2) {
      			num++;
      			ans = i;
      		}
      	}
      	printf("Case #%d: ", ++Cas);
      	if(num == 1) {
      		printf("%d\n", ans);
      	} else {
      		if(ans == -1) {
      			puts("Volunteer cheated!");
      		} else {
      			puts("Bad magician!");
      		}
      	}
    }
      	
}