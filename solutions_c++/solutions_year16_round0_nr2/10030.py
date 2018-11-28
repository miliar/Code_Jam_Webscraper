#include<fstream>
#include <string.h>
using namespace std;
int main()
{
	int t,k=1;
	ifstream fin;
	ofstream fout;
	fin.open("abc.in");
	fout.open("out.out");
	fin>>t;
	while(t--)
	{
		char ch[10];
		fin>>ch;
		int l=strlen(ch);
		int i,flip = 0, ans=0;
		for(i=l-1;i>=0;i--)
		{
			if(flip%2==1)
			{
				if(ch[i]=='+')
				{
					ans+=1;
					flip++;
				}
			}
			else
			{
				if(ch[i]=='-')
				{
					ans+=1;
					flip++;
				}
			}
		}
		fout<<"Case #"<<k++<<": "<<ans<<endl;
	}
}
