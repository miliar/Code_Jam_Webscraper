#include<stdio.h>
#include<fstream>
using namespace std;
int main()
{
	ifstream fin;
	fin.open("A-large.in");
	ofstream fout;
	fout.open("resa.in");
	int t,mno,i,sum,val,ans,tno;
	char str[1001];
	//scanf("%d",&t);
	fin>>t;
	for(tno=1;tno<=t;tno++)
	{
		//scanf("%d",&mno);
		fin>>mno;
		//scanf("%s",str);
		fin>>str;
		sum=0;
		ans=0;
		val=str[0]-'0';
		sum=val;
		for(i=1;i<=mno;i++)	
		{
			val=str[i]-'0';
			if(sum<i)
			{
				ans++;
				sum++;
			}
			sum+=val;
		}
		//printf("Case #%d: %d\n",tno,ans);
		fout<<"Case #"<<tno<<": "<<ans<<"\n";
	}
}
