#include <bits/stdc++.h>
using namespace std;
bool ar[10];
int main(int argc, char const *argv[])
{
	/* code */
	int t;
	scanf("%d", &t);
	for(int tc = 1; tc <= t; ++tc){
		int n;
		scanf("%d", &n);
		printf("Case #%d: ",tc);
		if(n == 0){
			puts("INSOMNIA");
			continue;
		}	
		memset(ar,0,sizeof ar);
		int cnt = 10;
		int temp = 0;
		while(cnt){
			temp += n;
			int temp2 = temp;
			while(temp2){
				int mod = temp2 % 10;
				if(!ar[mod]){
					ar[mod] = true;
					cnt--;
				}
				temp2 /= 10;
			}
		}
		printf("%d\n", temp);
	}
	return 0;
}