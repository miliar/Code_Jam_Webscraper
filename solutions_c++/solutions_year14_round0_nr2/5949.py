#include<iostream>

using namespace std;


void main()
{
	int T;
	cin>>T;
	for(int i = 0; i < T;i++)
	{
		double c,f,x;
		cin >> c>>f>>x;

		double currate = 2;


		double cookiesleft = x;
		double currcookies = 0;
		double constructingtime = 0;
		
		
		double sumttime = 0;

		int flag = 1;

		while(flag)
		{
			double nofarmtime = 0;
			double farmtime = 0;

			nofarmtime = cookiesleft / currate;

			double constrcutingtime = (c - currcookies)/currate;
			double newrate = (currate + f);

			farmtime = constrcutingtime + cookiesleft / newrate; 
		
			if (farmtime >  nofarmtime)
			{
				sumttime += nofarmtime;
				break;
			}
			else
			{
				sumttime += constrcutingtime;
				currate = currate + f;
			}
		}

		cout.precision(10);
		cout<<"Case #"<<(i+1)<<": "<<sumttime<<endl;
	}


}