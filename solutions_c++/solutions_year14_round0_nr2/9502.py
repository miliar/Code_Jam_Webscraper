#include<iostream>
#include<iomanip>
#include<fstream>
using namespace std;
int main()
{
	ofstream myfile;
  	myfile.open ("C:\\Users\\jat-wad\\Desktop\\output_second.txt");
	  int t,u=1;
	cin>>t;
	while(t--)
	{
		myfile<<setprecision(7)<<fixed;
		double c,f,x;
		cin>>c>>f>>x;
		int count=1;
		double time_t=x/2;
		int flag=0;
		double t1;
		int k;
		while(flag!=1)
		{
			t1=0;
			//cout<<count<<endl;
			k=count;
			while(k!=0)
			{
				k--;
				t1 += ( (c )/ (2 + (k*f) ));
					
			}
			t1+=(x)/ ( 2 + (count * f));
			if(t1>time_t)
			{
				flag=1;
			}
			else
			{
				time_t=t1;
			}
			count++;	
		}
		myfile << "Case #"<<u<<": ";
		myfile<<time_t<<endl;
		u++;
	}
}
