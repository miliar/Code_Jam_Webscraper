#include <iostream>
using namespace std;
int b[10]={'0'};
long long fun(long long n)
{   long long c,e;
    c=n;int d;int y=2;
	int count=0;
	while(count!=10)
	{    e=c;
		while(c)
	{   
		d=c%10;
		if(b[d]==0)
		{b[d]++;count++;}
		c=c/10;
		
	}
	c=n*y;y++;
	
	}
	return e;
	
}

int main() {
  freopen("A-large.in","r",stdin);
  freopen("outputgcj_l1.out","w",stdout);
   int t,y;long long n,a;
    y=1;
    cin>>t;
   while(y<=t)
   {
   	cin>>n;
   	if(n==0)
   	cout<<"Case #"<<y<<": INSOMNIA"<<endl;
   	else
   	{  for(int i=0;i<10;i++)
   	     b[i]=0;
   	     a=fun(n);
   		cout<<"Case #"<<y<<": "<<a<<endl;
   	}
   	y++;
   }
	return 0;
}
