#include<iostream>
#include<cmath>
#include <iomanip>
#include<vector>
#include<algorithm>
using namespace std;

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	
	double temp;
	long r,i,j,h,p;
	long count=1,cases;
	vector<double> nvalues, kvalues;
	cin>>cases;
	while(cases--)
	{
		cin>>r;
		
		nvalues.clear();
		for(i=0;i<r;i++)
		{
			cin >> temp;
			nvalues.push_back(temp);
		}
		
		kvalues.clear();
		for(i=0;i<r;i++)
		{
			cin >> temp;
			kvalues.push_back(temp);
		}

		sort(nvalues.begin(), nvalues.end());
		sort(kvalues.begin(), kvalues.end());
		
		h=0;
		
		for(j=r-1,i=r-1;j>=0&&i>=0;j--)
		{
			if(kvalues[i]>nvalues[j])
			{
				h++;i--;
			}
		}
		h = r-h;

		p=0;
		for(i=0;i<r;i++)
		{
			if(nvalues[i]>kvalues[i])
				p++;
			else if(nvalues[i]<kvalues[i])
			{
				kvalues[r-1] = -1;
				sort(kvalues.begin(), kvalues.end());
			}
		}

		
		cout<<"Case #"<<count<<": "<<p<<" "<<h<<endl;
		count++;
	}
	return 0;
}