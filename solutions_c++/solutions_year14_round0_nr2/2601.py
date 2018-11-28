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
	freopen("B-big-inp.txt","r",stdin);
	freopen("B-bigansout.txt","w",stdout);
	
	int t;
	cin>>t;
	
	int count=1;
	
	while(t-->0)
	{
		double valueyet=2.0,total=0.0,timeyet=0.0,timefarm=0.0,producedfarm,farmcost,cookies;

		cin>>farmcost>>producedfarm>>cookies;

		while(true)
		{
			timeyet=cookies/valueyet;
			timefarm=farmcost/valueyet + cookies/(producedfarm+valueyet);
			//cout<<timeyet<<" -> "<<timefarm<<endl;
			if (timeyet>timefarm)
			{
				total=total+ farmcost/valueyet;
				valueyet= valueyet + producedfarm;
			}
			else
			{
				total=total +timeyet;
				break;
			}
		}
		cout<<"Case #"<<count<<": ";
		printf("%.7f",total);
		
		cout<<endl;
		count++;
	}
 
 
 
 
}

