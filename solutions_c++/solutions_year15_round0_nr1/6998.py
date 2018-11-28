#include <cstdlib>
#include <iostream>

using namespace std;

int main(int argc, char *argv[])
{
    	int numTC=0;
	//ifstream in("in.txt");
//	ofstream out("o.txt");
	cin>>numTC;
	for(int i=0;i<numTC;i++)
	{
		int smax=0;
		cin>>smax;
		int *shy = new int[smax+1];
		cin.get();
		for(int j=0;j<smax+1;j++)
		{
			char ch;
			ch =cin.get();
			shy[j]=(ch-48);
		}
		int ans=0;
		int sum=shy[0];
		for(int j=1;j<smax+1;j++)
		{
			if(shy[j])
			{
				if(sum >= j)
				{
					sum = sum + shy[j];
				}
				else
				{
					ans=ans + (j-sum);
					sum = sum + ((j-sum)) +shy[j];
				}
			}
			
		}
		cout<<"Case #"<<i+1<<": "<<ans<<endl;
	}
	//in.close();
	//out.close();

    return EXIT_SUCCESS;
}
