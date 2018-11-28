#include <iostream>
#include <stdio.h>

using namespace std;

int main()
{
	freopen("A-small-attempt2.in","r",stdin);
	freopen("output.txt","w",stdout);

	int T;
	cin>>T;
	int t=1;

	int c,d; // choices
	int a[4][4],b[4][4]; // array
	int flag,br;
	int ri,rj;

	while (t<=T)
	{
		cin>>c;
		c--;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				cin>>a[i][j];
			}
		}

		cin>>d;
		d--;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				cin>>b[i][j];
			}
		}

		cout<<"case #"<<t<<": ";
		flag=0;
		br=0;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				if(a[c][i]==b[d][j])
				{
					if(flag==1)
					{
						
							cout<<"Bad magician!\n";
							br=1;
							break;
						
					}
					else
					{
						flag=1;
						ri=c;
						rj=i;
					}
				}
			}
			if(br==1)
				break;

		}

			if(flag==0&&(!br))
				cout<<"Volunteer cheated!\n";
			else if(flag==1&&(!br))
			{
				cout<<a[ri][rj];
				cout<<endl;
			}
		t++;
	}


}