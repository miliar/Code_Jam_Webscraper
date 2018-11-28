#include <queue>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>

using namespace std;

typedef long long ll;

#define mem0(x) memset(x, 0, sizeof(x))
#define mem1(x) memset(x, -1, sizeof(x))

int num[30]; 
 
int main(){
	int T, _ = 1;
	scanf("%d", &T);
	int n;
	while(T--){
		scanf("%d", &n);
		int sum = 0;
		for(int i = 0; i < n; i++) scanf("%d", &num[i]), sum+= num[i];
		int now;
		printf("Case #%d:", _++);
		int a, b;
		while(sum>0){
			a = b = -1; 
			for(int i = 0; i < 26; i++){
				if(a==-1 && num[i] && num[i]*2>(sum-1)) a = i, --num[a], --sum;
				if(sum == 0) break;
				if(a!=-1 && num[i] && num[i]*2>(sum-1)) b = i, --num[b], --sum;
				if((a!=-1) && (b!=-1)) break;
			}
			if(a==-1){
				for(int i = 0; i < 26; i++) 
					if(num[i]){
						--num[i];
						--sum;
						a = i;
						break;	
					}
			}
			printf(" %c", a+'A');
			if(b!=-1) printf("%c", b+'A');
//			system("pause");
		}
		printf("\n");
	} 
	return 0;
}
