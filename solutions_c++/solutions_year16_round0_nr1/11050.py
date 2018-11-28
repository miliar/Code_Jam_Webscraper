#include<iostream>
using namespace std;
int main()
{
	int t,i;
	cin>>t;
	for(i=1;i<=t;i++)
	{
		int x, a[10] = {0};
		unsigned long long int num , temp,z;
		cin>>num;
		z = num;
		
		if(num == 0)
		cout<<"Case #"<<i<<":"<<" "<<"INSOMNIA"<<endl;
		else
		{
				while( 1)
		{
			temp = num;
			while(temp!=0) {
			x = temp %10;
			temp = temp / 10;	
			a[x] = 1;
			}
			if((a[0] + a[1] + a[2] + a[3] + a[4]+a[5]+a[6]+a[7]+a[8]+a[9]) == 10)
			break;
			
			num = num + z;
		}
		
		cout<<"Case #"<<i<<":"<<" "<<num<<endl;
		}
		
	}
	return 0;
}
