#include <cstdio>
#include <iostream>

using namespace std;

int n,m,d,x,y,t;
int a[1001]; 

int main()
{
	freopen("Q4.in","r",stdin);
	freopen("Q4.out","w",stdout);
	cin>>m;
	for (int Case=1;Case<=m;Case++){
		cin>>d>>x>>y;
		if (x>y){t=x;x=y;y=t;}
		if (d>=7) cout<<"Case #"<<Case<<": RICHARD"<<endl;else
		if (d==1) cout<<"Case #"<<Case<<": GABRIEL"<<endl;else
		if (d==2){
			if ((x*y)%2==1) 
				cout<<"Case #"<<Case<<": RICHARD"<<endl;else
				cout<<"Case #"<<Case<<": GABRIEL"<<endl;
		}else
		if (d==3){
			if (x>=2 && (x*y)%3==0)
				cout<<"Case #"<<Case<<": GABRIEL"<<endl;else
				cout<<"Case #"<<Case<<": RICHARD"<<endl;
		}else
		if (d==4){
			if (x>=3 && y>=4 && (x*y)%4==0)
				cout<<"Case #"<<Case<<": GABRIEL"<<endl;else
				cout<<"Case #"<<Case<<": RICHARD"<<endl;
		}else
		if (d==5){
			if (x>=3 && y>=5 && (x*y)%5==0)
				cout<<"Case #"<<Case<<": GABRIEL"<<endl;else
				cout<<"Case #"<<Case<<": RICHARD"<<endl;
		}else
		if (d==6){
			if (x>=4 && y>=6  && (x*y)%6==0)
				cout<<"Case #"<<Case<<": GABRIEL"<<endl;else
				cout<<"Case #"<<Case<<": RICHARD"<<endl;
		}
	}
}
