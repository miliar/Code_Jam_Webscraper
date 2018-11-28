//Ominous Omino
#include<iostream>
#include<math.h>
using namespace std;
int main()
{
	int test;
	//cout<<"\nEnter the no. of test cases :";
	cin>>test;
	for(int i=0;i<test;i++)
	{
		int x,r,c,root;
		//cout<<"\nEnter the no. of X :";
		cin>>x;
		root=sqrt(x);
		//cout<<"\nEnter the no. of rows :";
		cin>>r;
		//cout<<"\nEnter the no. of columns :";
		cin>>c;
		if(x<=2)
		{
            if((r*c)%x==0)
            cout<<"Case #"<<i+1<<": GABRIEL"<<endl;
            else
            cout<<"Case #"<<i+1<<": RICHARD"<<endl;
		}
		else
		{
            if((r*c)%x==0 && ((r*c)/x) >= root+1)
            cout<<"Case #"<<i+1<<": GABRIEL"<<endl;
            else
            cout<<"Case #"<<i+1<<": RICHARD"<<endl;
        }
	}
	return 0;
}
