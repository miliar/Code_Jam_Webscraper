#include<iostream>
#include<fstream>
#include<sstream>
#include<conio.h>
#include<iomanip>
using namespace std;

int main()
{
	ifstream in("B-large.in");
	ofstream out("B-large.out");
	string s;
	getline(in,s);
	istringstream sin(s);
	int T;
	double C,F,X;
	sin>>T;
	for(int i=0;i<T;i++)
	{
		getline(in,s);
		istringstream sin(s);
		sin>>C;sin>>F;sin>>X;
		double S=2.0,time=0,cookie=0;
		for(;;)
		{
			if(C>=X-cookie){
				time+=(X-cookie)/S;
				break;
			}
			if((X-cookie)/S>((X-cookie)/(S+F))+C/S){
				/*cout<<"S:"<<S<<endl;
				cout<<"O_T:"<<(X-cookie)/S<<endl;
				cout<<"A_T:"<<(X-cookie-C)/(S+F)+C/S<<endl;*/
				time+=C/S;
				S+=F;
				//getche();
			}
			else{
				time+=(X-cookie)/S;
				break;
			}
		}
		out<<"Case #"<<1+i<<": "<<setiosflags(ios::fixed)<<setprecision(7)<<time<<endl;

	}
	system("pause");
}