#include<iostream>
using namespace std;

int main()
{
	int n,t;
	long double c,f,x,time,temp1,temp2,rate;
	cin>>t;
	n=0;
	cout.setf(ios::fixed);
    cout.precision(7);
	while(n++!=t)
	{
		rate=2.0;
		time=0;
		cin>>c>>f>>x;
		temp1 = x/rate;
		temp2 = c/rate + x/(rate+f);
		while(temp2 < temp1)
		{
			time += c/rate;
			rate += f;
			temp1=x/rate;
			temp2= c/rate + x/(rate+f);
		} 
		time += temp1;
		cout<<"Case #"<<n<<": "<<time<<endl;
	}
	return 0;
}
