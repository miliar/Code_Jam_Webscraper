#include <iostream>
#include <string>
#include <stdio.h>

using namespace std;

int main()
{
	int t,z;
	cin>>t;
	for(z=0;z<t;z++)
	{
		//cout<<"lol";
		int smax,extra=0,total=0,i,ex,dec;
		string s;


	
		cin>>smax>>s;

		for(i=0;i < smax + 1;i++)
		{
			//printf(" %d round \n\n",i);
			if(total >= i)
			{   

				dec = (int)s[i];
				dec = dec - 48;
				//printf("in first if %d\n",dec);
				total = total + dec ;

			}
			else
			{
				ex = i - total;
				extra = extra + ex ;
				dec = (int)s[i];
				dec = dec - 48;
				total = total + ex + dec;

				//cout<<i<<" total: "<<total<<"extra : "<<extra<<endl;

			}

		}

		cout<<"Case #"<<z+1<<": "<<extra<<endl;
		//printf("Case #%d: %d\n",z+1,extra);

		//cout<<smax<<" "<<s<<" s2 : "<<s[2]<<endl; 
		
		
	}
	
	
	return 0;
}


