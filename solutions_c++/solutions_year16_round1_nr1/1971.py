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
int main()
{
	f_in("A-large.in");
	f_out("a-large-out.txt");
	int test,t;
	scan(test);
	for(t=1;t<=test;t++)
	{
		string str ;
		cin>>str;
		int length = str.length();
		char res[2*length+1];
		fill(res,'-');
		res[length]=str[0];
		int i,back = length,front=length;
		for(i=1;i<length;i++)
		{
			if(res[back]<=str[i]){
				back--;
				res[back]=str[i];
			}
			else
			{
				front++;
				res[front]=str[i];
			}
		}
		cout<<"Case #"<<t<<": ";
		for(i=0;i<2*length+1;i++)
		{
			if(res[i]!='-')
			{
				cout<<res[i];
			}
		}
		cout<<endl;
	}
 	return 0;
}


