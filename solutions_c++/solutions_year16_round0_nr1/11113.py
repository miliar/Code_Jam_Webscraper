#include <iostream>
#include <fstream>
using namespace std;

int main()
{
   // ifstream cin ("sub-2.in");
    //ofstream cout("sub-2.out");
	int T;
	cin>>T;
	for (int t=1 ; t<=T ; t++)
	{
		int n;
		cin>>n;
		int count=0,i=1;
		int arr[10]= {0};
		int ans,a;
		if (n==0){
		cout<<"Case #"<<t<<": INSOMNIA\n";
		continue;}
		while (count !=10)
		{
			 ans = n*i;
			 a = ans;
			while (a !=0)
			{
				if (!arr[a%10])
				{
					count++;
					arr[a%10]++;
				}
				a=a/10;
			}

			i++;
		}
		cout<<"Case #"<<t<<": "<<ans<<"\n";
	}

	return 0;
}
