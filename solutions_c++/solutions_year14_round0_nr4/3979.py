#include<iostream>
#include<cstdio>
#include<algorithm>

using namespace std;
double inp1[1005];
double inp2[1005];
int n;
int str1()
{
	int i,j=0;
	for(i=0;i<n;i++)
	{
		while(j<n && inp2[j]<inp1[i])
			j++;
		if(j == n) return n-i;
		j++;
	}
	return 0;
}
int str2()
{
	int b1=0,b2=0,e1=n-1,e2=n-1;
	int res =0;
	while(b1<=e1)
	{
		if(inp1[b1]>inp2[b2]) {
			b1++,b2++;
			res++;
		}
		else {
			b1++,e2--;
		}
	}
	return res;
}
int main()
{
	int i,t;
	cin>>t;
	for(int tcase = 1;tcase <=t; tcase++)
	{
		cin>>n;
		for(i=0;i<n;i++)
			cin>>inp1[i];
		for(i=0;i<n;i++)
			cin>>inp2[i];
		sort(inp1,inp1+n);
		sort(inp2,inp2+n);
		/*for(i=0;i<n;i++)
			cout<<inp1[i]<<"\t";
		cout<<endl;
		for(i=0;i<n;i++)
			cout<<inp2[i]<<"\t";
		cout<<endl;*/
		printf("Case #%d: %d %d\n",tcase,str2(),str1());
	}
	return 0;
}
