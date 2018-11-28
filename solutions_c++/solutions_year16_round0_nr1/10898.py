#include <bits/stdc++.h>

using namespace std;
int counter[10];

bool ischeckall()
{
	for(int i=0;i<10;i++)
		if(counter[i]==0)	return false;

	return true;
}

int main()
{	
	//ofstream fout ("test.out");
    //ifstream fin ("test.in");
	long long tc,n;
	cin>>tc;
	for(long long k=1;k<=tc;k++)
	{
		cin>>n;
		for(long long i=0;i<10;i++)	counter[i]=0;
		long long cnt=1;
		if(n==0)
		{
			cout<<"Case #"<<k<<": INSOMNIA"<<endl;
			continue;
		}
		long long temp= n;
		while(true)
		{	
			long long temp2 = temp;		
			while(temp2)
			{
				counter[temp2%10]++;
				temp2 /= 10;
			}
			cnt++;
			if(ischeckall())
			{
				cout<<"Case #"<<k<<": "<<temp<<endl;
				break;
			}
			else
			{
				temp = cnt*n;
			}
		}
	}
	return 0;
}