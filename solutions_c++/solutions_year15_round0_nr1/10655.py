#include <stdio.h>
#include <iostream>
#include <string.h>


using namespace std;

int main()
{

	int test;
	int n,i,j,k,sit,invite,max;
	char shyness[1001];

	freopen("A-small-attempt0.in","r",stdin);
	freopen("problem_a_out.txt","w",stdout);

	cin>>test;
	for(n=1;n<=test;++n)
	{
        cin>>max;
		cin>>shyness;
		i=strlen(shyness);
		invite = 0;
		sit = 0;
		for(j=0;j<i && j<=max;++j)
		{
			k = shyness[j] - '0';

            if(sit>=j)
			{
				sit+=k;
			}
			else
			{
				sit+=k+1;
				invite+=1;
			}

		}

		cout<<"Case #"<<n<<": "<<invite<<endl;

	}


	return 0;
}
