#include <iostream>

using namespace std;

int main(void)
{
	int qqq = 0;
	cin>>qqq;
	for(int qq=0; qq<qqq; qq++)
	{
		int level = 0;
		cin>>level;

		char peoplec[level+1];
        int people[level+1];
		for(int i = 0; i < level+1; i++)
		{
			cin>>peoplec[i];
			people[i] = (int)(peoplec[i] - '0');
		}

		int sum = people[0];
		int req = (sum==0)?1:0;
		
		for(int i = 1; i<level+1; i++)
		{
			if(sum+req < i)
				req += (i-sum-req);
			sum += people[i];
		}
		cout<<"Case #"<<qq+1<<": "<<req<<endl;
	}

}
