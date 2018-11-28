#include <bits/stdc++.h>
using namespace std;
int arr[10];
void doIt(int n,int &cnt)
{
	while(n){
		int rem=n%10;
		if(arr[rem]==0){
			arr[rem]=1;
			cnt++;
		}
		n/=10;
	}
}
int main()
{
	//ifstream cin("input.txt");
	int test;
	cin>>test;
	int Case=1;
	while(test--)
	{
		memset(arr,0,sizeof arr);
		int cnt=0;
		long long n,temp;
		cin>>n;
		temp=n;
		if(n==0)
			printf("Case #%d: INSOMNIA\n",Case++);
		else
		{
			while(cnt!=10)
			{
				doIt(temp,cnt);
				temp+=n;
			}
			printf("Case #%d: %lld\n",Case++,temp-n);
		}
	}
}