#include <iostream>
#include <fstream>
#include <string>
#include <iomanip>

using namespace std;

int main()
{
    
    int n;
     cin>>n;
	 for(int i=0;i<n;i++)
     {
     	double C,F,X;
     	cin>>C>>F>>X;
     	int k=0;
     	double totaltime = 0;
     	while(true)
     	{
     		if((X*F)< (C*(2+F*(k+1)))) 
			{
     			totaltime += (X/(2+F*k));
     			break;
     		}
     		else
     		{
     			totaltime += (C/(2+F*k));
     			k++;
     		}
     	}
     	cout<<setprecision(10)<<"Case #"<<i+1<<": "<<totaltime<<endl;
      }
      
	 return 0;     
}
