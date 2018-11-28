#include<iostream>
using namespace std;

int main()
{
	int times;
	cin>>times;
	int times_ori=times;

	long long int i;
	long long int n;
	long long int sum, temp_sum;
	bool digits[10];
	
	while(times--)
	{
		cin>>n;
		if(n==0)
		{
			cout<<"Case #"<<times_ori-times<<": INSOMNIA"<<endl;
			continue;
		}

		sum=0;
		for(i=0;i<10;i++) digits[i]=false;
		while(digits[0]==false || digits[1]==false || digits[2]==false || digits[3]==false || digits[4]==false || digits[5]==false || digits[6]==false || digits[7]==false || digits[8]==false || digits[9]==false)
		{
			sum+=n;
			temp_sum=sum;
			while(temp_sum!=0)
			{
				digits[temp_sum%10]=true;
				temp_sum/=10;
			}
		}
		cout<<"Case #"<<times_ori-times<<": "<<sum<<endl;
	}
	return 0;
}
