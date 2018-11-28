#include<iostream>
#include<string.h>
using namespace std;
int main(){
	freopen("A-large.in","r",stdin);
     freopen("gcj1.out","w",stdout);
	int t; char s[3002],ch,a[2001];
	cin>>t;
	int b=1;
	while(b<=t)
	{
		cin>>a;
		int y=1000,z;
		z=strlen(a);
		s[y]=a[0];
		for(int i=1;i<z;i++)
		{
			ch=a[i];
			if(s[y]>ch)
			s[y+i]=ch;
			else {
			s[y-1]=ch; y=y-1;}
			
		}
		cout<<"Case #"<<b<<": ";
		for(int i=y;i<y+z;i++)
		 cout<<s[i];
		cout<<endl;
		b++;
	}
	return 0;
}
