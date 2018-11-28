#include <iostream>
#include <string>
using namespace std;
int a[10][10][10];
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	string s[3];
	s[1]="GABRIEL";
	s[2]="RICHARD";
	//size=1
	for(int i=1;i<=4;++i)
		for(int j=1;j<=4;++j)
			a[1][i][j]=1;
	a[1][1][1]=1;
	a[2][1][1]=a[2][1][3]=2;
	a[2][1][2]=1;

	a[2][1][4]=a[2][2][2]=a[2][2][3]=a[2][2][4]=1;
	a[2][3][3]=2;
	a[2][3][4]=1;
	a[2][4][4]=1;

	a[3][1][1]=a[3][1][2]=a[3][1][3]=a[3][1][4]=a[3][2][2]=2;
	a[3][2][3]=1;
	a[3][2][4]=2;
	a[3][3][3]=1;
	a[3][3][4]=1;
	a[3][4][4]=2;

	a[4][1][1]=a[4][1][2]=a[4][1][3]=a[4][1][4]=a[4][2][2]=a[4][2][3]=a[4][2][4]=2;
	a[4][3][3]=2;
	a[4][3][4]=1;
	a[4][4][4]=1;


	cin>>t;
	for(int k=1;k<=t;++k)
	{
		int aa,b,c;
		cin>>aa>>b>>c;
		if(b>c)
			swap(b,c);
		cout<<"Case #"<<k<<": "<<s[a[aa][b][c]]<<endl;
	}
}