#include<iostream>
#include<cstring>
#include<string>
#include<cstdio>
#include<fstream>

using namespace std;

int main()
{
fstream cin("D-small-attempt2.in",ios::in);
fstream cout("D-small-attempt2.out",ios::out);
int t;
cin>>t;int q=1;
while(t--)
{  
	int x,r,c;
	cin>>x>>r>>c;
  bool p=false;
  if (x==1) p=true;
  if (x==2&&(c*r)%2==0) p=true;
  if (x==3&&((r==3&&c==3)||(r==2&&c==3)||(r==3&&c==2)||(r==3&&c==4)||(r==4&&c==3)))
   p=true;
  if (x==4&&(c==4&&r==4||(c==3&&r==4)||(c==4&&r==3))) p=true;
  if (p)	cout<<"Case #"<<q++<<": "<<"GABRIEL"<<endl;
	else cout<<"Case #"<<q++<<": "<<"RICHARD"<<endl;	
}	
return 0;	
}
