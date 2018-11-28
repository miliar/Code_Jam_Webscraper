#include<iostream>
#include<algorithm>
#include<math.h>
#include<fstream>
using namespace std;

int main()
{
	long int i=0,r=0,temp,a,b,c,testcases,count=0,j;
	double xp;
	//ofstream myfile;
	//myfile.open("ex.txt");
	cin>>testcases;
	j=testcases;
	while(testcases--)
	{
		a=0,b=0,count=0;
		cin>>a>>b;
		i=a;
		while(i>=a && i<=b)
		{
			xp=0,c=0,r=0;
			temp=i;
			while(temp>0)
			{
				c=temp%10;
				temp=temp/10;
				r=r*10+c;
			}
			if(i==r)
			{
				xp=sqrt((double)i);
				if(i==(xp*xp))
				{
					temp=xp;
					r=0,c=0;
					while(temp>0)
					{
						//cout<<i;
						c=temp%10;
						temp=temp/10;
						r=r*10+c;
					}
					if(xp==r)
					{
						count+=1;

					}

				}

			}

			i++;
		}
		cout<<"Case #"<<(j-testcases)<<":"<<" "<<count<<endl;
		//myfile<<"Case #"<<(j-testcases)<<":"<<" "<<count<<endl;
	}
	//myfile.close();
	return 0; 

}
