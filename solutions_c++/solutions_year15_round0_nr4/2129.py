#include <iostream>
#include <list>
#include <vector>
using namespace std;



int main()
{
	freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
int T; cin>>T;
for(int j=1; j<=T; j++)
{
cout<<"Case #"<<j<<": ";
int X,R,C; cin>>X>>R>>C;
   
if(R==1 && C==1)
{
	if(X==1)
	cout<<"GABRIEL"<<endl;
	else
	cout<<"RICHARD"<<endl;
		
}
if(R==1 && C==2  || R==2 && C==1)
{
	if(X==1 || X==2) cout<<"GABRIEL"<<endl;
		
	else cout<<"RICHARD"<<endl;

}
if(R==1 && C==3 || R==3 && C==1)
{
	if(X==1) cout<<"GABRIEL"<<endl;
	else cout<<"RICHARD"<<endl;		
}

if(R==1 && C==4 || R==4 && C==1)
{
	if(X==1 || X==2) 
		cout<<"GABRIEL"<<endl;
    else 
	 cout<<"RICHARD"<<endl;
}

if(R==2 && C==2)
{
	if(X==1 || X==2) cout<<"GABRIEL"<<endl;
    else cout<<"RICHARD"<<endl;

}
if(R==2 && C==3 || R==3 && C==2)
{

	if(X==1 || X==2 || X==3) 
		cout<<"GABRIEL"<<endl;
    else
		cout<<"RICHARD"<<endl;

}
if(R==2 && C==4 || R==4 && C==2)
{
	if(X==1 || X==2) 
		cout<<"GABRIEL"<<endl;
    else
	 cout<<"RICHARD"<<endl;
}

if(R==3 && C==3)
{
	if(X==1 || X==3)
	cout<<"GABRIEL"<<endl;
	else
	cout<<"RICHARD"<<endl;

	

}
if(R==3 && C==4 || R==4 && C==3)
{
	  if(X==1 || X==2 || X==3 || X==4 )
	  cout<<"GABRIEL"<<endl;
	  else
      cout<<"RICHARD"<<endl;
	

}
if(R==4 && C==4)

{
	if(X==1 || X==2 || X==4)
	cout<<"GABRIEL"<<endl;
	else
	cout<<"RICHARD"<<endl;

}
}
	return 0;

}
