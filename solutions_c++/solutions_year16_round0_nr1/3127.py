#include<iostream>

using namespace std;

long long int countSheep(long long int x)
{
	int record=0,check=1023,i=1,digit;
	long long int temp,ans;
	//cout<<(record&check);
	while((record&check) != check)
	{
		//cout<<record<<" "<<check;
		ans=temp=i*x;
		while(temp>0)
		{
			digit=temp%10;
			record= record | (1<<digit);
			temp/=10;
		}
		i++;
	}
	return ans;
}

int main()
{
	int t,i=1;
	cin>>t;
	while(t-- > 0)
	{
		long long int n,last;
		cin>>n;
		if(n==0)
			cout<<"Case #"<<i<<": INSOMNIA"<<endl;
		else
		{
			last=countSheep(n);
			cout<<"Case #"<<i<<": "<<last<<endl;
		}
		i++;
	}
}

/*
i/p:
5
0
1
2
11
1692
o/p;
INSOMNIA
10
90
110
5076
*/