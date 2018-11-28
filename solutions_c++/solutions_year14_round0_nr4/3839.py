#include<iostream>
#include<algorithm>
#include<vector>
#include<set>
#include<stdio.h>

using namespace std;

int main()
{
	freopen("D-large.in","r",stdin);
	freopen("D-large.out","w",stdout);
	int t,c=1;
	cin >> t;
	while(t)
	{
		set<double> NW,KW,KDW;
		int N,war=0,dwar;
		double X;
		cin >> N;
		dwar = 0;
		for(int i=0;i<N;i++)
		{
			cin >> X;
			NW.insert(X);
		}
		for(int i=0;i<N;i++)
		{
			cin >> X;
			KW.insert(X);
			KDW.insert(X);
		}
		//war
		set<double>::iterator it,kt;
		for(it = NW.begin();it != NW.end(); ++it)
		{
			double chosen_N = *it;
			kt = upper_bound(KW.begin(),KW.end(),chosen_N);
			if(kt==KW.end())
			{
				war = distance(it,NW.end());
				break;
			}
			KW.erase(kt);
		}
		//dwar
		for(kt = KDW.begin(); kt != KDW.end(); ++kt)
		{
			double chosen_K = *kt;
			it = upper_bound(NW.begin(),NW.end(),chosen_K);
			if(it==NW.end())
				break;
			NW.erase(it);
			dwar++;
		}
		cout << "Case #" << c << ": " << dwar << " " << war << endl;
		t--;c++;
	}
	return 0;
}