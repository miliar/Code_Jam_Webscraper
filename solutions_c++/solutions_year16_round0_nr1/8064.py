#include<bits/stdc++.h>
using namespace std;
int a[10], n;
bool cal()
{
	for(int i=0;i<10;i++)
		if(a[i]==0)
			return false;
	return true;
}
int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for(int p=1;p<=t;p++){
		printf("Case #%d: ", p);
		memset(a, 0, sizeof(a));
		scanf("%d", &n);
		int cnt=n;
		if(n==0)
			printf("INSOMNIA\n");
		else{
			while(1){
				int temp=n;
				while(temp){
					a[temp%10]=1;
					temp/=10;
				}
				if(cal())
					break;
				n+=cnt;
			}
			printf("%d\n", n);
		}
	}

}