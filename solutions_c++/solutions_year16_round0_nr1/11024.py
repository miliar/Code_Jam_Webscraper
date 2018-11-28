#include <iostream>
#include<fstream>
using namespace std;

ifstream inFile;
ofstream outFile;
int main()
{

inFile.open("A-large.in");
outFile.open("output.txt");
int i,j,k,l,r,o,T;
long long int m,N[100];
inFile>>T;
	for(i=0;i<T;i++)
	{inFile>>N[i];}
for(j=0;j<T;j++)
	{
	int a[10]={0,1,2,3,4,5,6,7,8,9};
	o=10;
	m=N[j];
		for(i=2	;i<100;i++)
			{
				while(m!=0)
				{
				r=m%10;
				m=m/10;
					for(k=0;k<o;k++)
					{
					if(a[k]==r)
						{ o--;
						  for(l=k;l<o;l++)
							{
							a[l]=a[l+1];

							}

						}

					}

				}
			 if(o==0)
			 {      outFile<<"Case #"<<j+1<<": "<<(N[j]*(i-1))<<"\n";
				break;}
			 m=N[j]*i;

			}
		  if(o!=0)
		  {
		  outFile<<"Case #"<<j+1<<": INSOMNIA\n";
		  }



	}

inFile.close();
outFile.close();

    return 0;
}
