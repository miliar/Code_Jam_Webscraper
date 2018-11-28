#include <iostream>
#include <string>
using namespace std;

int main()
{
	int t=0;

	cin>>t;
	for(int i=0;i<t;i++)
	{
		int y=1, l;
		string cakes;
		//if(i==0)
			cin.ignore();
		//getline (cin, cakes);
		cin>>cakes;
		l=cakes.length();
		//cout<<"cakes is"<<cakes<<" and is "<<cakes.length()<<" long."<<endl;
		for(int j=1; j<l; j++)
		{
			if(cakes[j]!=cakes[j-1])
			{
				//cout<<"cakes[j]="<<cakes[j]<<" and cakes[j=1]="<<cakes[j-1]<<endl;
				y=y+1;
			}
		}	
			//cout<<"cakes ends in"<<cakes[l-1]<<endl;
		if(cakes[l-1]=='+')
		{	
			y--;
			
		} 	
		cout<<"Case #"<<i+1<<": "<<y<<endl;
	}
	
	
		return 0;
}		