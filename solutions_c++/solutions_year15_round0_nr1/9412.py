#include<fstream>
using namespace std;
int main()
{
		fstream fin, fout;
		fin.open("A-large.in");
		fout.open("out.txt");
		int t;
		fin>>t;
		for(int k=0;k<t;k++)
		{
            int n;
            long long int ans=0;
            long long int c=0;
            string s;
            fin>>n;
			fin>>s;
            int a[n+1];
			for(int i=0;i<=n;i++)
				a[i]=int(s[i])-48;
			ans=a[0];c=0;
			for(int i=1;i<=n;i++)
			{
				if(ans>=i)
                    ans+=a[i];
				else
				{
					c+=(i-ans);
					ans+=(i-ans);
					ans+=a[i];
				}
			}
				fout<<"Case #"<<k+1<<": "<<c<<"\n";
		}
        fin.close();
        fout.close();
		return 0;
	}
