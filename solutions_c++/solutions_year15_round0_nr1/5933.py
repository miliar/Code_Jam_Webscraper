#include<fstream>
using namespace std;

int main()
{
	ifstream fin("inp.txt");
	ofstream fout("out.txt");
	int t,i,n,j,stand,add;
	char shy[1005];
	fin>>t;
	for(i=1;i<=t;i++)
	{
		fin>>n;
		for(j=0;j<=n;j++)
			fin>>shy[j];
		stand=0;
		add=0;
		for(j=0;j<=n;j++)
		{
			if(shy[j]-'0')
			{
				if(stand<j)
				{
					add=add+(j-stand);
					stand=stand+(j-stand);
				}
				stand=stand+(shy[j]-'0');
			}
		}
		fout<<"Case #"<<i<<": "<<add<<"\n";
	}
}