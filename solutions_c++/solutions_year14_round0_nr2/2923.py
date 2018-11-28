#include<iostream>
#include <fstream>
#include <iomanip>
using namespace std;
int main()
{
	ifstream cin;
    ofstream cout;
    cin.open ("B-large.in");
    cout.open("output.txt");
	int t,i,j;
	double c,f,x,z,p,a,s;
	cin>>t;
	for(i=1;i<=t;i++)
	{
		cin>>c>>f>>x;
		z=2.0;
		a=x/z;
		p=c/z;
		s=(c/z)+(x/(z+f));
		while(a>s)
		{
			z=z+f;
			a=s;
			s=p+(c/z)+(x/(z+f));
			p=p+(c/z);
		}
		cout.precision(7);
		cout<<"Case #"<<i<<":"<<" ";
        cout << fixed;
       cout << setprecision(7) <<a<<endl;
	}
}
