#include <iostream>

using namespace std;

int main()
{
	int t=0;
	int s_max=0;
	int testcase=0;
	char a[1001]={0};
	int i=0;
	int standing=0;
	int needed=0;
	FILE *in;
	cin>>t;
	testcase=t;

	while (testcase>0)
	{
		needed=0;
		standing=0;

		cin>>s_max;
		cin>>a;
		//cout<<int(a[0])-48;
		standing=int(a[0])-48;
		for(i=1;i<=s_max;i++)
		{
			if(int((a[i])-48)>0)
			if(i>(standing+needed))
			{
				needed+=i-(standing+needed);
			}
			standing+=int(a[i])-48;
		}

		cout<<"case #"<<t-testcase+1<<": "<<needed<<"\n";


		testcase--;
	}
	return 0;
}

