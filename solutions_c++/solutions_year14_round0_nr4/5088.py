#include<iostream>
#include<vector>
#include<algorithm>
#include<fstream>

using namespace std;

int main()
{
	int t;
	ifstream fin("ds.in");
	ofstream fout("d_small1.out");
	fin>>t;
	
	for(int e=1; e<=t; e++)
	{
		int n;
		fin>>n;
		int minn=0, maxn=n, mink=0, maxk=n;
		vector <double> na(n);
		vector <double> k(n);
		int dcount=0, count=n;
		
		for(int i=0; i<n; i++)
		{
			fin>>na[i];
		}
		for(int i=0; i<n; i++)
		{
			fin>>k[i];
		}
		sort(na.begin(), na.end());
		sort(k.begin(), k.end());
		
		while(minn<maxn && mink<maxk)
		{
			if(na[minn]<k[mink])
			{
				maxk--;
				minn++;
			}
			else
			{
				minn++;
				mink++;
				dcount++;
			}
		}
		
		minn=-1;
		maxn=n;
		mink=-1;
		maxk=n;
		
		int j=0;
		while(minn<n && mink<n)
		{
			minn++;
			mink++;
			while(k[mink]<na[minn])
			{
				mink++;
				if(mink>=n)
					break;
			}
		}
		count=n-minn;	
		fout<<"Case #"<<e<<": "<<dcount<<" "<<count<<endl;
		
	}
	return 0;
}
		
		
		
