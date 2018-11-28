#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <climits>
#include <numeric>
#include <stdlib.h> 
#include <time.h> 
#include <math.h>
#include <string>
using namespace std;
string str1;
int main(){
freopen("B-small-attempt0.in", "r", stdin);
freopen("b-small-attempt0.out", "w", stdout);
	int T, i, j, n;
	long long ans, x;
	long long a[1000];
	double flag=1;
	cin>>T;
	for(int I=0; I<T; I++){
		cin>>n;
		for(i=1; i<=n; i++){
			cin>>a[i];
		}
		sort(a+1, a+n+1);
		ans = a[n];
		for(i=1; i<=1000; i++){
			x=0;
			for(j=1; j<=n; j++){
				x+=ceil(flag*a[j]/i)-1;
			}
			x+=i;
			if (ans>x)	ans = x;
		}
		cout<<"Case #"<<I+1<<": "<<ans<<endl;
	}
		//fclose(stdin);
		//fclose(stdout);
			return 0;
}