//standing ovation
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <cstring>
using namespace std;


typedef struct {
	int need;
	int have;
	int people;
	int invite;
} DP;

int main() {
	int t, s;
	string str;
	
	scanf("%d",&t);
	for (int k=0; k<t; k++) {
		scanf("%d",&s);
		cin >> str;
		int len = str.length();
		
		int DP[len];
		DP[0] = str[0]-'0';
		/*for (int i=1; i<len; i++) {
			arr[i].need = i;
			arr[i].people = str[i]-'0';
			
			if (arr[i].people > 0) {
				arr[i].have = arr[i-1].have + arr[i-1].invite;
				if (arr[i].have < arr[i].need)
					arr[i].invite = arr[i].need - arr[i].have;
				else 
					arr[i].invite = arr[i-1].invite;
			}
			else {
				arr[i].invite = arr[i-1].invite;
				arr[i].have = arr[i-1].have;
			}
			
			arr[i].have += arr[i].people;
			
			//printf("%d %d %d %d\n", arr[i].need, arr[i].people, arr[i].have, arr[i].invite);
		}*/
		
		int invite = 0;
		
		for (int i=1; i<len; i++) {
			DP[i] = DP[i-1] + str[i]-'0';
		}
		
		for (int i=1; i<len; i++) {
			if (DP[i-1]+invite < i) {
				invite += (i-(DP[i-1]+invite));
			}
			//printf("%d %d\n",DP[i], invite);
		}
		
		printf("Case #%d: %d\n",k+1, invite);
	}
	return 0;
}
