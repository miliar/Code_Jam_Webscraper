#include<iostream>
#include<iomanip>
#include<string>
using namespace std;

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("output.txt","w",stdout);

	int probnum;
	double C,F,X;
	double oldR,newR;
	double oldT,newT;

	cin>>probnum;

	for (int i=0 ; i<probnum ; i++)
	{
		int n=0;			//FarmCount
		cin>>C>>F>>X;
		
		oldT=X/2.0;
		do
		{
			oldR=(n*F)+2.0;
			n++;
			double TotalFarmT=0;
			for (int j=0 ; j<n ; j++)
				TotalFarmT+=C/(2+(j*F));
			newR=(n*F)+2.0;
			newT=(X/newR)+TotalFarmT;
			if (oldT>newT)
				oldT=newT;
		}while(oldT>=newT);
		
		string str = to_string(oldT);

		cout<<"Case #"<<i+1<<": "<<str<<endl;
	}

}