#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <climits>
#include <numeric>
#include <stdlib.h> 
#include <time.h> 
#include <math.h>
#include <string.h>
using namespace std;
int T, n;
int f[10];
int main(){
//	freopen("A-large.in", "r", stdin);
//	freopen("A-small-attempt0.out", "w", stdout);
	cin>>T;
	int cnt = 0;
	while(T--){
		printf("Case #%d: ", ++cnt);
		scanf("%d", &n);
		memset(f, 0, sizeof(f));
		if (!n) {
			cout<<"INSOMNIA"<<endl;
		}
		for(int i=1; i<=100; i++){
			int x = i * n;
			while(x>0){
				f[x%10] = 1;
				x /= 10;		
			}	
			int flag = 1;
			for (int j=0; j<=9; j++){
				if (!f[j]){
					flag = 0;
					break;
				}
			}
			if (flag){
				cout<<i*n<<endl;
				break;
			}
		}
	}
	return 0;
}