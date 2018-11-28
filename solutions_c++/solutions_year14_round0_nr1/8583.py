#include <iostream>
using namespace std;

int main() {
	int t,c,loc=0;
	int x,y;
	int a[16],b[16],ans1,ans2;
	cin>>t;
	int temp=t;
	while(t--)
	{
		c=0;loc=-1;
		cin>>ans1;
		
		for(int i=0;i<16;i++)
			cin>>a[i];
		
		cin>>ans2;
		for(int i=0;i<16;i++)
			cin>>b[i];
		
		
		for(x=(ans1-1)*4;x<((ans1-1)*4)+4;x++)
			for(y=(ans2-1)*4;y<((ans2-1)*4)+4;y++)
				if(a[x]==b[y])
				{ 	
					++c;
					if(c==1)
					loc=x;
				}
		switch(c)
		{
			case 0:	cout<<"Case #"<<temp-t <<": Volunteer cheated!"<<endl;
					break;
			case 1: cout<<"Case #"<<temp-t<<": "<<a[loc]<<endl;
					break;
			default:cout<<"Case #"<<temp-t<<": Bad magician!"<<endl;
					break;
		}
	}
	return 0;
}