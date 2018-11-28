#include<iostream>
#include<fstream>
#include<vector>
#include<algorithm>
using namespace std;
int main()
{
	int T,i,j,n,m,v=0;
	ifstream fin("in4.txt");
	ofstream fout("out4.txt");
	fin>>T;
	while(T--)
	{
		fin>>n;
		vector<double>s1(n);
		vector<double>s2(n);
		for(i=0;i<n;i++)
			fin>>s1[i];
		for(i=0;i<n;i++)
			fin>>s2[i];
		sort(s1.begin(),s1.end());
		sort(s2.begin(),s2.end());
		int i1=0,i2=0,j1=n-1,j2=n-1,ans=0;
		fout<<"Case #"<<++v<<": ";
		while(j2>=0)
		{
			if(s1[j1]>s2[j2])
			{
				j1--;
				ans++;
			}
			else
				i1++;
			j2--;
		}
		fout<<ans<<' ';
		ans=i1=i2=0;
		j1=j2=n-1;
		while(j1>=0)
		{
			if(s2[j2]>s1[j1])
			{
				j2--;
				ans++;
			}
			else
				i2++;
			j1--;
		}
		fout<<n-ans<<endl;
	}
	fin.close();
	fout.close();
	return 0;
}