#include<iostream>
#include <cstdio>
using namespace std;

short a1[4][4],a2[4][4];
short n1,n2;
int main()
	{freopen("output.txt","w",stdout);
	 short n;
	 cin>>n;
	 for(short i=1;i<=n;++i)
		{cin>>n1;
		 for(short j=0;j<4;++j)
			for(short k=0;k<4;++k)
				cin>>a1[j][k];

		 cin>>n2;
		 for(short j=0;j<4;++j)
			for(short k=0;k<4;++k)
				cin>>a2[j][k];
		

	 	 short a=n1-1;
		 short b=n2-1;
		 short count=0,value;
		 for(short j=0;j<4;++j)
			{for(short k=0;k<4;++k)
				{if(a1[a][j]==a2[b][k])
					{value=a1[a][j];
					 count++;
					}
				}
			}
		if(count==0)
			cout<<"Case #"<<i<<": Volunteer cheated!\n";
		else if(count==1)
			cout<<"Case #"<<i<<": "<<value<<"\n";
		else
			cout<<"Case #"<<i<<": Bad magician!\n";
		}			
	 return 0;
	}
