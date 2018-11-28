#include<iostream>
#include<stdio.h>
#include<algorithm>
#include<string.h>
#include<math.h>
#include<queue>
#define S(x) scanf("%d",&x);
#define SL(x) scanf("%lld",&x);
#define SS(x) scanf("%s",&x);
#define ll long long
#define ii int
char arr[4][4];
ll check_row(ll i,char ch)
{
	ll j,k,l,m;
	char check;
	if(ch=='T')
		check=arr[i][1];
	else
		check=ch;
	if(check=='.')
		return 0;
	for(j=1;j<4;j++)
	{
		if(arr[i][j]=='.')
			return 0;
		else if(arr[i][j]=='T')
			continue;
		else if(arr[i][j]==check)
			continue;
		else return -1;
	}
	return 1;
}
ll check_column(ll j,char ch)
{
	ll i,k,m;
	char check;
	if(ch=='T')
		check=arr[1][j];
	else
		check=ch;
	if(check=='.')
		return 0;
	for(i=1;i<4;i++)
	{
		if(arr[i][j]=='.')
			return 0;
		else if(arr[i][j]=='T')
			continue;
		else if(arr[i][j]==check)
			continue;
		else return -1;
	}
	return 1;
}
ll check_diagnol(ll j,ll go,char ch)
{
	char check;
	ll i=0;
	if(ch=='T')
		check=arr[i+1][j+go];
	else
		check=ch;
	if(check=='.')
		return 0;
//	cout<<check<<" sdafkh "<<endl;
	if(go==1)
		j=0;
	else j=3;
	for(i=1;i<4;i++)
	{
		j+=go;
		if(arr[i][j]=='.')
			return 0;
		else if(arr[i][j]=='T')
			continue;
		else if(arr[i][j]==check)
			continue;
		else return -1;
	}
	return 1;
}
using namespace std;
int main()
{
	freopen("E:\\in.in","r",stdin);
	freopen("E:\\out.txt","w",stdout);
	ll t,i,j,k,n,m;
	SL(t);
	k=1;
	char a[3];
	while(k<=t)
	{
		ll dot_count=0;
		for(i=0;i<4;i++)
		{
			gets(a);
			for(j=0;j<4;j++)
			{
//				cout<<i<<" "<<j<<endl;
				scanf("%c",&arr[i][j]);
				if(arr[i][j]=='.')
					dot_count++;
			}
		}
		gets(a);
		ll ans;
		char prnt='D';
		for(i=0;i<4;i++)
		{
			ans=check_row(i,arr[i][0]);
			if(ans==1)
			{
				prnt=arr[i][0];
				goto end;
			}
		}
		for(j=0;j<4;j++)
		{
			ans=check_column(j,arr[0][j]);
			if(ans==1)
			{
				prnt=arr[0][j];
				goto end;
			}
		}
		ans=check_diagnol(0,1,arr[0][0]);
		if(ans==1)
		{
			prnt=arr[0][0];
//			cout<<prnt<<" "<<0<<endl;
			goto end;
		}
		ans=check_diagnol(0,-1,arr[0][3]);
		if(ans==1)
		{
			prnt=arr[0][3];
//			cout<<prnt<<" "<<3<<endl;
			goto end;
		}
		end:
		if(prnt=='D')
		{
			if(dot_count)
				printf("Case #%lld: Game has not completed",k);
			else
				printf("Case #%lld: Draw",k);
		}
		else
		{
			printf("Case #%lld: %c won",k,prnt);
		}
		printf("\n");
		k++;
	}
	return 0;
}
