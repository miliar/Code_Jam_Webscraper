#include <iostream>
#include <iomanip>
using namespace std;
int main()
{
	int N;
	cin>>N;

	float C,F,X,rate=2.000000,t1,t2,t3,t4;
	for(int i=0;i<N;i++)
	{
		cin>>C>>F>>X;
		rate=2.000000;
		t1=t2=t3=t4=0.000000;
		while(t4<=t3)
		{
			t3=t2+X/rate;
			t4=t2+(C/rate)+(X/(rate+F));
			t1=C/rate;
			t2+=t1;
			rate+=F;
		}
		std::cout.setf( std::ios::fixed, std:: ios::floatfield );
		cout<<"Case #"<<i+1<<": "<<t3<<endl;
	}
	return 0;
}
