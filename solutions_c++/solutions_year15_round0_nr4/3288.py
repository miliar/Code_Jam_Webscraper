#include <iostream>
using namespace std;

int main() 
{
int t;
cin>>t;
for(int q=0;q<t;q++)
{
int x,r,c,flag=0;
cin>>x>>r>>c;
int person=1;
if(x==1) person=1;
else 
if(x==2)
{ if((r*c) % x !=0) person=2; else person=1;}
else
if(x==3)
{ if( (r*c) % x !=0 || r==1 || c==1) person=2; else person=1;}
else
if(x==4)
{if( (r*c) % x !=0 || r==1 || c==1 ||(r<4&&c<4) || r==2 ||c==2) person=2; else person=1;}

cout<<"Case #"<<q+1<<": ";
if(person==1) cout<<"GABRIEL"<<endl; else cout<<"RICHARD"<<endl;
}
	return 0;
}

//minute details are necessary for the intimation of the processing system of the batch for the server. genral purpose batches are being served on remote locator
//Multi purpose servers are being offered to perform special functions of the resource locator
