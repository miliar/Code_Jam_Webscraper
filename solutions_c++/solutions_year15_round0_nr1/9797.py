#include <iostream>
#include <cmath>
using namespace std;
int main()
{
	int test,ans[100];
	cin>>test;
	for(int a=0;a<test;a++)
	{
	
				int tlev;
				char peplev[100];
				int pep[100];
				cin>>tlev;
				cin>>peplev;
					for(int i=0;i<tlev+1;i++)
					{
						pep[i]=((int)peplev[i])-48;
						
					}
				int sum=0,max=0;
					for(int i=0;i<tlev+1;i++)
					{
						if((i-sum)>max && i>sum)
						{
							max=i-sum;
						}
						sum+=pep[i];
						
					}
				ans[a]=max;
    }
    for(int i=0;i<test;i++)
    {
    	cout<<"Case #"<<i+1<<": "<<ans[i]<<endl;
	}
	return 0;
}
