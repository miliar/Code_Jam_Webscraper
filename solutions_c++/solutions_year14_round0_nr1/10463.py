#include <iostream>
using namespace std;

int main() {
	int T;
	cin>>T;
	
	int a1, a2;
	int s1[4][4], s2[4][4];
	int c, n;
	for(int t=1; t<=T; t++)
	{
		c=0;
		
		cin>>a1;
		for(int i=0;i<4;i++)	
			for(int j=0;j<4;j++)	
				cin>>s1[i][j];
		cin>>a2;
		for(int i=0;i<4;i++)	
			for(int j=0;j<4;j++)	
				cin>>s2[i][j];
		
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				if (s1[a1-1][i]==s2[a2-1][j])
				{
					c++;
					n=s1[a1-1][i];
				}
		
		if (c==1)
			cout<<"Case #"<<t<<": "<<n<<endl;
		else if (c==0)
			cout<<"Case #"<<t<<": Volunteer cheated!\n";
		else
			cout<<"Case #"<<t<<": Bad magician!\n";
		
	}
	
	return 0;
}