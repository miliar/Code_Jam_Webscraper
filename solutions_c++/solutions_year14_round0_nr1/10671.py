#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <cmath>
#include <iomanip>

using namespace std;

int M1[4][4];
int M2[4][4];

void doCase(int t)
{
	cout<<"Case #"<<t<<": ";

	int r1,r2;

	cin>>r1;
	r1--;

	int i,j;

	for(i=0;i<4;i++)
		for(j=0;j<4;j++)
			cin>>M1[i][j];

	cin>>r2;
	r2--;

	for(i=0;i<4;i++)
		for(j=0;j<4;j++)
			cin>>M2[i][j];

	int num=-1;
	for(i=0;i<4 && num!=-2;i++)
		for(j=0;j<4 && num!=-2;j++)
			if(M1[r1][i]==M2[r2][j])
			{
				if(num>0)
					num=-2;
				else
					num=M1[r1][i];
			}

		if(num==-1)
			cout<<"Volunteer cheated!"<<endl;
		else if(num==-2)
			cout<<"Bad magician!"<<endl;
		else
			cout<<num<<endl;
}

int main()
{
	//freopen("input.txt","r",stdin);
	//freopen("output.txt","w",stdout);

	int T;
	cin>>T;

	for(int i=1;i<=T;i++)
		doCase(i);

}