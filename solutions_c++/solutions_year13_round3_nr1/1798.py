#include<iostream>
#include<cstring>
using namespace std;

int lol(char*a,int b,int c)
{
	int i,sum=0;
	int k[c],l[c];
	for(i=0;i<c;i++)
		{
			if(a[i]=='a' || a[i]=='e' || a[i]=='o' || a[i]=='i' || a[i]=='u')
				k[i]=0;
			else if(i==0)
				k[i]=1;
			else
				k[i]=k[i-1]+1;
		}
	for(i=0;i<c;i++)
		{
			if(i==0 && b==1)
				l[i]=k[i];
			else if(i==0)
				l[i]=0;
			else if(k[i]>=b)
				l[i]=(i+2)-b;
			else
				l[i]=l[i-1];
		}
	for(i=0;i<c;i++)
		sum+=l[i];
	return sum;
}

int main()
{
	int lp=0,cnt,b;
	cin >> cnt;
	char a[1000001];
	for(lp=1;lp<=cnt;lp++)
	{
		cin >> a >> b;
		cout << "Case #" << lp << ": " << lol(a,b,strlen(a)) << endl;
	}
}
