#include<bits/stdc++.h>
using namespace std;
int arr[100]={NULL};
int len=0;
map<int,int>check;
int counter = 0;
void array_num(long long int n);
long long int check_product();
int main()
{
//freopen("input.in","r",stdin);
//freopen("output.in","w",stdout);
int t,n,test;
scanf("%d",&test);
t=test;
while(test--)
{
	check.clear();
	counter = 0;
	memset(arr,0,sizeof(arr));
	scanf("%d",&n);
	if(n==0)
	printf("Case #%d: INSOMNIA\n",t-test);
	else {
	long long int i = 0;
	while(counter != 10){
		i++;
	array_num(n*i);
	}
	printf("Case #%d: %lld\n",t-test,n*i);
	}
}
return 0;
}
void array_num(long long int n)
{
	int i=0,r;
	while(n!=0)
	{
		r=n%10;
		arr[i++]=r;
		n=n/10;
		if(check[r] != 1)
		{
			counter++;
			check[r] = 1;
		}
	}
}
