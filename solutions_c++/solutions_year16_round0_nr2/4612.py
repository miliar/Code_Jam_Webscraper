#include<bits/stdc++.h>
#define scan(n) scanf("%d",&n)
#define scanll(n) scanf("%lld",&n)
#define For(i,a,b) for(i=a;i<b;i++)
#define fill(a,b) memset(a,b,sizeof(a))
#define swap(a,b) a=a+b;b=a-b;a=a-b;
#define ll long long int
#define pb push_back
#define MAX 1000000007
#define f_in(st) freopen(st,"r",stdin);
#define f_out(st) freopen(st,"w",stdout);
using namespace std;
char flip(char a)
{
	if(a=='+')
	return '-';
	else
	return'+';
}
int main()
{
	//	f_in("B-large.in");
	//f_out("B-largeout.txt");
	int test;
	scan(test);
	for(int t =1;t<=test;t++)
	{
		string str;
		cin>>str;
		int i=str.length();
		i--;
		int count  = 0;
		for(;i>=0;--i)
		{
			if(str[i]=='+'&&!count)
			{
				continue;
			}
			else if(str[i]=='-'&&!count)
			{
				count++;
			}
			else{
				int odd = count%2;
				if(odd)
				{
					str[i]=flip(str[i]);
					
				}
				if(str[i]=='-')
				count++;
			}
		}
		cout<<"Case #"<<t<<": "<<count<<endl;
	}
 	return 0;
}


