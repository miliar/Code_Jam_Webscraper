#include<iostream>
#include<fstream>
using namespace std;
int main ()
{

	ifstream cin;cin.open("A-large.in");
	ofstream cout;cout.open("A-large.out");
	unsigned long long arr[101];
	int i;int cases;
	unsigned long long num;
	cin>>cases;
	unsigned long long j;
	unsigned long long ans=0;
	int k;
	bool a[10];
	for(i = 0;i<cases;i++)
	{
		cin>>arr[i];
	}
	bool flag;
	for(i = 0;i<cases;i++)
	{
		flag= false;
		for(k = 0;k<10;k++){a[k]=false;}
		ans=0;
		cout<<"Case #"<<i+1<<": ";
		int counter=0;
		for(j = 1;j<1001;j++)
		{
			flag= false;
			ans =0;
			num = arr[i]*j;
			while (num>=0)
			{
				a[num%10] = true;
				num/=10;
				if(num==0){break;}
			}
			num=arr[i]*j;
			counter=0;
			for(k = 0;k<10;k++)
			{
				if(a[k]==true){counter++;}
			}

			if(counter==10){ans = num;break;}

		}

		if(ans>0){cout<<ans<<endl;}
		else {cout<<"INSOMNIA\n";}




	}

	return 0;
}