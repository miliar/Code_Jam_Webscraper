#include <iostream>
using namespace std;

int main(int argc, char const *argv[])
{
	int T,even,odd,i,temp1,count,mul,M=1;
	long long n,temp,org;
	cin>>T;
	while(M<=T)
	{
		int arr[10] = {0};
		cin>>n;
		org = n;
		i = count = 0;
		mul = 1;
		while(n<10  && n!=0)
		{
			arr[n] = 1;
			count++;
			mul++;
			n = org*mul;
			i++;
		}
		while(count<10 && i < 1000 && n>0)
		{
			while(n!=0)
			{
				temp1 = n%10;
				n/=10;
				if(arr[temp1]!=1) count++;
				arr[temp1] = 1;
			}
			i++;
			mul++;
			n = org*mul;
		}
		n = org*(mul-1);
		if(count == 10)
			cout<<"Case #"<<M<<": "<<n<<endl;
		else
			cout<<"Case #"<<M<<": "<<"INSOMNIA"<<endl;
		M++;
	}
	return 0;
}