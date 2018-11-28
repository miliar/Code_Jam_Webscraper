#include <bits/stdc++.h>
#define gc getchar
using namespace std;
typedef long long int lli;
void scanint(int &x)
{
    register int c = gc();
    x = 0;
    for(;(c<48 || c>57);c = gc());
    for(;c>47 && c<58;c = gc()) {x = (x<<1) + (x<<3) + c - 48;}
}

int main()
{
	ofstream file;
	file.open("file.txt");
	int t,i,smax,total,ans,j;
	char s[1000];
	scanint(t);
	for(j=1;j<=t;j++)
	{
		scanint(smax);
		scanf("%s",s);
		total=0;
		ans=0;
		for(i=0;i<=smax;i++)
		{
			if(s[i]=='0') continue;
			if(total>=i) total+=s[i]-'0';
			else 
			{
				ans+=i-total;
				total=i+(s[i]-'0');
			}
		}
		file<<"Case #"<<j<<": "<<ans<<endl;
		//printf("Case #%d: %d\n",j,ans);
	}
}