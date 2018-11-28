#include<fstream>
using namespace std;
int main()
{
	int T;
	int smax;
	string stemp;
	int nc;
	int notobeadded;
	ifstream fin("A-small-attempt1.in");
	ofstream fout("A-small-attempt1.out");
	fin>>T;
	for(int j=1;j<=T;j++)
	{
		fin>>smax;
		fin>>stemp;
		int s[smax+5];
		for(int i=0;i<=smax;i++)
			s[i] = stemp[i] - '0';
		if(smax==0)
			fout<<"Case #"<<j<<": 0"<<endl;
		else
		{
			nc = s[0];
			notobeadded = 0;
			for(int i=1;i<=smax;i++)
			{
				if(nc>=i)
					nc+=s[i];
				else
				{
					if(s[i]!=0)
					{
						notobeadded+=(i - nc);
						nc+=notobeadded;
						nc+=s[i];
					}
				}

			}
			fout<<"Case #"<<j<<": "<<notobeadded<<endl;
		}

	}
	return 0;

}
