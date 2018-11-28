#include <iostream>
#include <iomanip>
using namespace std;

int main() {
	//C F X
	float rate;
	float time1;
	float C,F,X,t1,t2;
	int t;
	cin>>t;
	int temp=t;
	while(t--)
	{
		cin>>C>>F>>X;
		rate=2.0;
		time1=0.0;
		while(1)
		{
			t1=X/rate;
			//cout<<t1<<" ";
			t2=(C/rate)+(X/(rate+F));
			//cout<<t2<<endl;
			if(t1>t2)
			{
			//	cout<<time1<<endl;
				time1+=C/rate;
				rate+=F;
			}
			else
			{
				time1+=t1;
				break;
			}
		}
		cout<<"Case #"<<temp-t<<": "<<setprecision(8)<<time1<<endl;
	}
		return 0;
}