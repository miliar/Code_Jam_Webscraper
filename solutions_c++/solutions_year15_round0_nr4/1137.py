#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <string>
using namespace std;
int compare (const void* a,const void* b)
{
	return (*(int*)b-*(int*)a);
}
int main()
{
	freopen("D-small-attempt0.in","r",stdin);
//	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int T;
	cin>>T;
	for (int t=0;t<T;t++)
	{
		cout<<"Case #"<<t+1<<": ";
		string res="";
		int x,r,c,temp;
		cin>>x>>r>>c;
		if (r>c)
		{
			temp=r;
			r=c;
			c=temp;			
		}
		if (x==1)
			res="GABRIEL";
		else if (x==2)
		{
			if ((r*c)%x!=0)
				res="RICHARD";
			else
				res="GABRIEL";
		}
		else if (x==3)
		{
			if ((r*c)%x!=0)
				res="RICHARD";
			else if (r==1 && c==3)
				res="RICHARD";
			else
				res="GABRIEL";
		}
		else if (x==4)
		{
			if ((r*c)%x!=0)
				res="RICHARD";
			else if ((r==1 && c==4) || (r==2 && c==4) || (r==2 && c==2))
				res="RICHARD";
			else
				res="GABRIEL";
		}
		cout<<res<<endl;
	}
	return 0;
}
