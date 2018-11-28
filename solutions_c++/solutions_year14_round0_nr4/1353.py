#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int main()
{
	int t; cin >> t;
	
	for(int i=1; i<=t; i++)
	{
		int n; cin >> n;
		vector <double> c1(n); for(int j=0; j<n; j++) cin >> c1.at(j);
		vector <double> cc1(n); for(int j=0; j<n; j++) cc1.at(j) = c1.at(j);
		vector <double> c2(n); for(int j=0; j<n; j++) cin >> c2.at(j);
		
		//neako skopirovat vector do cc1
		
		sort(c1.begin(), c1.begin()+n);
		sort(c2.begin(), c2.begin()+n);
		
		int deceitfulWar=0;
		for(int j=n-1, k=n-1; k>=0; j--, k--)
		{
			if(c1.at(j) > c2.at(k)) deceitfulWar++;
			else j++;
		}
		
		int war=0;
		for(int k=0 ; k<n; k++)
		{
			if(cc1.at(k) > c2.at(c2.size()-1))
			{
				c2.erase(c2.begin());  // netreba asi ani mazat, ci?
			}
			else	//vyber najblizsie vecie
			{
				unsigned l;
				for( l=0; l<c2.size(); l++)
					if(cc1.at(k) < c2.at(l)) break;
					
				c2.erase(c2.begin()+l); 
				war++;
			}
		}



		
		cout << "Case #" << i << ": " << deceitfulWar << " " << n-war << endl;		
	}
	
	return 0;	
}





