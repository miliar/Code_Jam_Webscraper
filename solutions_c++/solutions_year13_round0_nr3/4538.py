#include<iostream>
#include<cstdio>
#include<queue>
#include<vector>
#include<map>
#include<algorithm>
#include<string>

using namespace std;

int a[10000];
char str[100];
bool ispal(int x)
{
	sprintf(str,"%d",x);
	string s(str);
	string s2 = s;
	reverse(s2.begin(),s2.end());
	return s2 == s;
}
void calc()
{
	for(int i=0;i*i<1001;i++)
	{
		if( ispal(i) && ispal(i*i) )
			a[i*i] = 1;
	}
	for(int i=1;i<1001;i++)
		a[i] += a[i-1];
}
int main()
{
	freopen("in.txt","rt",stdin);
	freopen("out_C.txt","wt",stdout);
	int TC;
	scanf("%d",&TC);
	int kk,x;
	calc();
	int A,B;
	for(int tc =1; tc<=TC;tc++)
	{
		scanf("%d%d",&A,&B);
		printf("Case #%d: %d\n",tc,a[B]-a[A-1]);
	}
	return 0;
}