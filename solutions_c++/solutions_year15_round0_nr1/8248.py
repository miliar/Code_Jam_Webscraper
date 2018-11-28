#include<fstream>
using namespace std;
int main()
{
	int t,s,i,ans,c=1,k,f;
	char a[1001];
	ifstream fin;
	ofstream fout;
	fin.open("abc.in");
	fout.open("out.out");
	fin>>t;
	while(t--)
	{
		fin>>s;
		fin>>a;
		ans=0;
		k=0;
		f=0;
		for(i=0;i<=s;i++)
		{
			if(f>1001)
				break;
			if(a[i]=='0')
			{
				if(f<=i)
				{
					ans++;
					f++;
				}
			}
			else
			{
				k=ans;
				f+=a[i]-'0';
			}
		}
		fout<<"Case #"<<c++<<": "<<k<<endl;
	}
	fin.close();
	fout.close();
}
