#include<iostream>
#include<cmath>
using namespace std;

int main()
{
	int T,start=1;;
	int r,t,r1;
	cin>>T;
	while(T>0)
	{
		int temp,temp_1,temp_2,num=0;
		cin>>r >>t;
		r1=r+1;
		temp_1=(int)pow(r,2);
		temp_2=(int)pow(r1,2);
		temp=temp_2-temp_1;
		while(temp<=t)
		{
			num++;
			r+=2;
			r1+=2;
			t-=temp;
			temp_1=(int)pow(r,2);
			temp_2=(int)pow(r1,2);
			temp=temp_2-temp_1;
		}
		cout<<"Case #"<<start<<": "<<num<<"\n";
		T--;
		start++;
	}
	return 0;
}