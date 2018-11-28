#include<iostream>
using namespace std;

typedef __int64 I;

const int N= 1000002;

char str[N];

bool con[N];

I a[N];
I dp[N], res[N];

int main(){
	freopen("A.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for(int cas= 1; cas <= t; cas++){
		int n;
		scanf("%s%d", str+1, &n);
		int len= strlen(str+1);
		for(int i= 1; i <= len; i++){
			if(str[i] == 'a' || str[i] == 'e' || str[i] == 'i' || str[i] == 'o' || str[i] == 'u')
				con[i]= false;
			else 
				con[i]= true;
		}
		a[0]= 0;
		for(int i= 1; i <= len; i++)
			if(con[i] == false)
				a[i]= 0;
			else
				a[i]= a[i-1]+1;
		for(int i= 1; i <= len; i++){
			if(a[i] < n)
				dp[i]= 0;
			else 
				dp[i]= i-(n-1);
		}
		res[0]= 0;
		for(int i= 1; i <= len; i++){
			if(a[i] < n)
				res[i]= res[i-1];
			else
				res[i]= dp[i];
		}
		I ans= 0;
		for(int i= 1; i <= len; i++){
			ans+= res[i];
		}
		printf("Case #%d: %I64d\n", cas, ans);
	}
	return 0;
}