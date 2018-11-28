#include<iostream>
#include<map>
#include<vector>
#include<string>
#include<cstring>
#include<algorithm>
#include<cmath>
#include<fstream>
#include<iomanip>
#include<set>
#include<cstdio>
using namespace std;
//pandey
int main()
{
	//ios_base::sync_with_stdio(false);
	freopen("C-inp.txt","r",stdin);
	freopen("C-out.txt","w",stdout);
	
	int t;
	cin>>t;
	
	int count=1;
	
	while(t-->0)
	{
		
		int n;
		cin>>n;

		double naomi[n],ken[n];

		for(int i=0;i<n;i++)
		{
			cin>>naomi[i];

		}
		for(int i=0;i<n;i++)
		{
			cin>>ken[i];

		}
		sort(naomi,naomi+n);
		sort(ken,ken+n);
		
		int checknaomi[n],checkken[n];
		
		memset(checknaomi,0,sizeof(checknaomi));
		memset(checknaomi,0,sizeof(checkken));
		
		int deceitans=0,warans=0;
		int j=n-1;
		for(int i=n-1;i>=0&&j>=0;)
		{
			if(naomi[i]>ken[j])
				{
					deceitans++;
					i--;
					j--;
				}
			else
			{
				j--;
			}
		}
		
	int  kentop=0,kenbottom=n-1;
		 for(int i=n-1;i>=0&&kenbottom>=kentop;)
		 {
		 	if(naomi[i]>ken[kenbottom])
		 	{
		 		warans++;
		 		i--;
		 		kentop++;
		 	}
		 	else
		 	{
		 		i--;
		 		kenbottom--;

		 	}

		 }


		cout<<"Case #"<<count<<": ";
		
		cout<<deceitans<<" "<<warans;
		cout<<endl;
		count++;
	}
 
 
 
 
}

