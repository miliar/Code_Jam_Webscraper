#include<iostream>
#include <set>
#include <sstream>
#include<fstream>
using namespace std;
int main()
 {
	freopen("A-small-attempt0.in","r",stdin);
freopen("out234.out","w",stdout);
	int T;
	 int a[4][4]; int b[4][4]; int x,y,n,c,z=1;
	cin>>T;
	while(T!=0)
	{ c=0;
		cin>>x;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
			cin>>a[i][j];
				}
			}
		cin>>y;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
			cin>>b[i][j];
				}
			}
			
			for(int j=0;j<4;j++)
			{
				for(int i=0;i<4;i++)
				{
				if(a[x-1][j]==b[y-1][i])
				{
					c++;
				n=a[x-1][j];	}
				}
			}
if(c==1)
cout<<"Case #"<<z<<": "<<n<<endl;
else if(c>1)
cout<<"Case #"<<z<<": Bad magician!\n";
else
cout<<"Case #"<<z<<": Volunteer cheated!\n";
z++;
	T--;		
		}
	return 0;
}
