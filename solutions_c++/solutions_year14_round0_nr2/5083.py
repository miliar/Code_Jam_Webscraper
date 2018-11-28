#include<iostream>

#include<algorithm>


using namespace std;

int main()

{

	int t;

	cin >> t;

	cout<<"t="<<t<<endl;

	for(int i=1;i<=t;i++)

	{

	double c,f,x;

	cin>>c>>f>>x;

	double k = 2.0;

	double d = 0.0;

	while( (x-c)/k * f > c)

	{

		//cout<<"c/k="<<c/k<<endl;

		d += c/k;

		k += f;

	}

	d += x/k;

	printf("Case #%d: %.7f\n",i,d);

	}

}