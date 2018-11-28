#include <iostream>
#include <fstream>
/* run this program using the console pauser or add your own getch, system("pause") or input loop */
using namespace std;

int main(int argc, char *argv[]) {
/*
ifstream cin("gcj2_prac.in");
    ofstream cout("file.out");
	  cout.precision(7);
    cout.setf(ios::fixed);
*/
	std::cout.precision(7);
	std::cout.setf( std::ios::fixed, std:: ios::floatfield );
int cnt,no=0;
double c,f,x,r,t,t1,t2;
cin	>>cnt;
while(cnt--)
{
	no++;
	
	cin>>c>>f>>x;
	cout<<"Case #"<<no <<": ";
	t=0;
	r=2;
	
	while(1)
	{
		t1=x/r;
		t2=c/r;
		if(t1<t2)
		{
			t=t+t1;
			cout<<t;
			break;
		}
		else
		{
			t=t+t2;
		}
		t1=(x-c)/r;
		t2=x/(r+f);
		if(t2>=t1)
		{
			t=t+t1;
			cout<<t;
			break;
		}
		else
		{
			r=r+f;
		}
		
	}
	cout<<endl;
}
	return 0;
}