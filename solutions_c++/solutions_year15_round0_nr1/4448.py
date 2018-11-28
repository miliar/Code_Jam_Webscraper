#include <iostream>
#include <string>
#include <vector>

using namespace std;


int main()
{
	    freopen("input.txt","r",stdin);
        freopen("output.txt","w",stdout);

	int T; cin>>T;
	for(int j=1 ; j<=T ; j++)
	{
	int smax; cin>>smax;
	string s; cin>>s;
	vector<int> shy;

	for(int i=0; i<smax+1; i++)
	{
		shy.push_back(s[i]-48);

	}

	int standing=shy[0];
	int total=0;
	int friends=0;

		
	for(int i=1 ; i<smax+1 ; i++)
	{
		if(standing>=i)
		{
			standing+=shy[i];	
		}

		else
		{
			if(shy[i]!=0)
			{
			friends+=i-standing;
			standing+=shy[i]+i-standing;
			}
		}
	}
	
	cout<<"Case #"<<j<<": "<<friends<<endl;
	
	}
	return 0;

}