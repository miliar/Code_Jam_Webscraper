#include <iostream>
using namespace std;


		int q[20];
		bool r[50];
		int d,v;
		
void go(int x,int y)
{
	if (x>v)
	return;
	r[x]=1;
	if (y==d)
		return;
	go(x,y+1);
	go(x+q[y],y+1);
}

int main() {
	// t c d v
	
	int t,c;
	cin>>t;
	for (int i=1;i<=t;i++)
	{
		cout<<"Case #"<<i<<": ";
		cin>>c>>d>>v;
		
		for (int j=0;j<d;j++)
		cin>>q[j];
		for (int j=0;j<50;j++)
		r[j]=0;
		
		//cout<<"RRRR"<<v<<endl;
		go(0,0);
		//cout<<"RRRR"<<v<<endl;
		//for (int j=0;j<=v;j++)
		//cout<<j<<':'<<r[j]<<' ';
		//cout<<endl;
		int a=0;
		bool qq=0;
		do {
			qq=0;
		
		for (int j=0;j<=v;j++)
		if (r[j]==0)
		{
			qq=1;
			a++;
			q[d]=j;
			for (int j=0;j<50;j++)
		r[j]=0;
			d++;
			go(0,0);
			j=99999;
		}
		} while (qq);
		cout<<a<<endl;
	}
	return 0;
}