#include<iostream>

using namespace std;

int main()
{
	int testCases,x,r,c,caseCount;

	ios::sync_with_stdio(false);

	cin>>testCases;
	for(caseCount = 1; caseCount<=testCases; caseCount++)
	{
		cin>>x>>r>>c;

		if(x==1)
		{
			cout<<"Case #"<<caseCount<<": GABRIEL"<<endl;
			continue;
		}
		
		if(x==2)
		{
			if((r*c)%2==0)
				cout<<"Case #"<<caseCount<<": GABRIEL"<<endl;
			else
				cout<<"Case #"<<caseCount<<": RICHARD"<<endl;
			continue;
		}

		if(x==3)
		{
			if((r*c) == 6 || (r*c) == 9||(r*c) == 12)
				cout<<"Case #"<<caseCount<<": GABRIEL"<<endl;
			else
				cout<<"Case #"<<caseCount<<": RICHARD"<<endl;
			continue;
		}

		if(x==4)
		{
			if((r*c) == 12||(r*c) == 16)
				cout<<"Case #"<<caseCount<<": GABRIEL"<<endl;
			else
				cout<<"Case #"<<caseCount<<": RICHARD"<<endl;
			continue;
		}
	}
	
	return 0;
}






