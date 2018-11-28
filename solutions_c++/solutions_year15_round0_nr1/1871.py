#include<iostream>
#include<cstdio>
#include<fstream>
using namespace std;
int main()
{
	fstream file1,file2;
	file1.open("a.in",ios::in);
	file2.open("b.txt",ios::out);
	int a,ans,t,x,k=0,n;
	char s[2010];
	file1>>a; //scanf("%d",&a);
	while(a--)
	{
		k++;
		ans=t=0;
		file1>>n; //scanf("%d",&n);
		file1>>s; //scanf("%s",s);
		for(int q=0;q<=n;++q)
		{
			x=s[q]-'0';
			if(t<q)
			{
				ans+=q-t;
				t=q;	
			}
			t+=x;
		}
		file2<<"Case #"<<k<<": "<<ans<<"\n"; //printf("Case #%d: %d\n",k,ans);
	}
 	return 0;
}

