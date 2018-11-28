#include<fstream>
#include<vector>
#include<string>
#include<string.h>
#include<algorithm>
using namespace std;
void process(std::istream& ip,std::ostream& op)
{
	int tc,w,i,n,minm,j;
	char s[2005],t[10][20]={"ZERO","ONE","TWO","THREE","FOUR","FIVE","SIX","SEVEN","EIGHT","NINE"};
	ip>>tc;
	for(w=1;w<=tc;w++)
	{
		int count[26]={0};
		int ans[10]={0};
		op<<"Case #"<<w<<": ";
		ip>>s;		
		for(i=0;s[i]!='\0';i++)
			count[s[i]-'A']++;
		
		ans[0]=count['Z'-'A'];
		for(j=0;t[0][j]!='\0';j++)
			count[t[0][j]-'A']-=ans[0];

		ans[2]=count['W'-'A'];
		for(j=0;t[2][j]!='\0';j++)
			count[t[2][j]-'A']-=ans[2];

		ans[4]=count['U'-'A'];
		for(j=0;t[4][j]!='\0';j++)
			count[t[4][j]-'A']-=ans[4];

		ans[6]=count['X'-'A'];
		for(j=0;t[6][j]!='\0';j++)
			count[t[6][j]-'A']-=ans[6];

		for(i=1;i<10;i++)
		{
			if(i==2||i==4||i==6)
				continue;
			
			minm=2005;
			for(j=0;t[i][j]!='\0';j++)
				minm=min(minm,count[t[i][j]-'A']);
			
			if(minm==0)
				continue;
			if(i==3||i==7)
			{
				if(count['E'-'A']>=minm*2);
				else
					continue;
			}
			if(i==9)
				if(count['N'-'A']>=minm*2);
				else
					continue;			
			
			ans[i]=minm;
			
			for(j=0;t[i][j]!='\0';j++)
				count[t[i][j]-'A']-=minm;
		}
		for(i=0;i<10;i++)
		{
			for(j=0;j<ans[i];j++)
			{
				op<<i;
			}
		}
		op<<"\n";
	}
}
int main()
{
	ifstream myfile ("A-large.in");
	ofstream file ("output.in");
	process(myfile,file);
}