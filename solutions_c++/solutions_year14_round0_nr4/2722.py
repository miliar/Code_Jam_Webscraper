#include <iostream>
#include <fstream>
#include <algorithm>
#include <iomanip>
using namespace std;
 
int main() {
    ifstream fil;
    ofstream fout;
    fil.open("test.in",ios::in);
    fout.open("fourlarge.txt",ios::out);
	int t;
	fil>>t;
	for(int cs = 1;cs<=t;cs++)
	{
		int n;
		fil>>n;
		double naomi[1000],ken[1000];
		for(int i=0;i<n;i++)
		fil>>setprecision(9)>>naomi[i];
		for(int i=0;i<n;i++)
		fil>>setprecision(9)>>ken[i];
		int win = 0,d_win=0;
		sort(naomi,naomi+n);
		sort(ken,ken+n);
		double naomit[1000],kentt[1000];
		for(int i=0;i<n;i++)
		{
			naomit[i]=naomi[i];
			kentt[i]=ken[i];
		}
		//Normal play
		int destroy = 0;
		for(int i=0;i<n;i++)
		{
			destroy = 0;
			for(int j=0;j<n&&destroy==0;j++)
			{
				if(ken[j]>naomi[i]&&naomi[i]!=-1&&ken[j]!=-1)
				{
					ken[j]=-1;
					naomi[i]=-1;
					destroy = 1;
				}
			}
			if(!destroy)
			{
				win++;
				naomi[i]=-1;
				int found = 0;
				for(int j=0;j<n&&!found;j++)
				{
					if(ken[j]!=-1)
					{
						ken[j]=-1;
						found = 1;
					}
				}
			}
		}
 
		//Points by playing optimally on war is win
		//Deceitful war
 
		for(int i=0;i<n;i++)
		{
			int destroy = 0;
			for(int j=0;j<n&&!destroy;j++)
			{
				if(naomit[j]>kentt[i]&&kentt[i]!=-1)
				{
					d_win++;
					destroy++;
					naomit[j]=-1;
					kentt[i]=-1;
				}
			}
			if(!destroy)
			{
				int found = 0;
				for(int i=0;i<n&&!found;i++)
				{
					if(naomit[i]!=-1)
					{
						found++;
						naomit[i]=-1;
					}
				}
				found = 0;
				for(int j=n-1;j>=0&&!found;j--)
				{
					if(kentt[j]!=-1)
					{
						found++;
						kentt[j]=-1;
					}
				}
			}
		}
		fout<<"Case #"<<cs<<": "<<d_win<<" "<<win<<endl;
 
	}
	fil.close();
	fout.close();
	return 0;
}
