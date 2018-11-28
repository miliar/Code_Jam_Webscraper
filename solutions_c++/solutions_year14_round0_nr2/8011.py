#include<iostream>
#include<iomanip>
using namespace std;

float cal(float c,float f,float x)
{
	float r = 2.0;
	float tt=0.0f,tt1=0.0f,ct2=0.0f,xt=0.0f;
	xt =x/r;
	ct2 = c/r;
	r = r+f;
	tt = ct2 +(x/r);
	if(xt<tt)
		{return (float)xt;}
	else
	{
		do
		{
		tt1 = tt;
		ct2 = ct2 + c/r;
		r = r + f;
		
		tt = ct2 + x/r;

		}while(tt1>tt);
		return tt1;
	}
	
	
}

int main()
{
int n;
float a[100];
float c,x,f;
cin>>n;//To take number of test cases
for(int i=0;i<n;i++)
{
cin>>c;
cin>>f;
cin>>x;

a[i] = cal(c,f,x);
}

for(int i=0;i<n;i++)
{
	cout.precision(10);
	cout<<"Case #"<<i+1<<": "<<fixed<<((double)a[i])<<"\n";;
	
}

return 0;	
}