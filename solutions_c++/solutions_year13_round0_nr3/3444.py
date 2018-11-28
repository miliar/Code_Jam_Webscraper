#include<iostream>

using namespace std;

int main()
{
	int t=0;
	cin>>t;
	int t_=0;
	int a=0,b=0;
	int himan_arr[5]={1,4,9,121,484};
	int count=0;
	while(t_<t)
	{
		t_++;
		cin>>a>>b;
		count=0;
		for(int i=0;i<5;i++)
			if(himan_arr[i]<=b && himan_arr[i]>=a)count++;

		cout<<"Case #"<<t_<<": "<<count<<endl;

	}
	return 0;
}
