#include<iostream>
#include<fstream>
#include<iomanip>
using namespace std;
int main()
{
	ifstream cin;
	ofstream cout;
	int t;
	cin.open("C:\\Users\\Admin\\Downloads\\B-large.in");
	cout.open("C:\\Users\\Admin\\Downloads\\out.txt");
	cin>>t;
	int y=1;
	while(t--)
	{
		long double c,f,x,time=0;
			cin.precision(14);
		cout.precision(19);
		cin>>c>>f>>x;
		long double r=2;
		while(c/(r) + x/(r+f) < x/r )
		{
			time+=c/(r);
			r+=f;
		}
		time+=x/r;
		cout<< "Case #" << y << ": " << time<<endl;
        y++;
	}
	cin.close();
	cout.close();
	return 0;
}
