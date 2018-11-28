#include<iostream>
using namespace std;

int main()
{
	freopen("A-small-attempt1.in", "r", stdin);
    freopen("firstA.out", "w", stdout);
	int T;
	cin>>T;
	for(int t=1;t<=T;t++)
	{
		int row1,row2;
		int A[4][4],B[4][4];
		cin>>row1;
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				cin>>A[i][j];
		cin>>row2;
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				cin>>B[i][j];

		int test[17]={0};
		for(int i=0;i<4;i++)
		{
			int indexa=A[row1-1][i];
			test[indexa]+=1;
			int indexb=B[row2-1][i];
			test[indexb]+=1;
		}
		int cnt=0;
		int num;
		for(int i=0;i<17;i++)
			if(test[i]==2)
			{
				cnt++;
				num=i;
			}

		if(cnt==0)
			cout<<"Case #"<<t<<": Volunteer cheated!"<<endl;
		else if(cnt==1)
			cout<<"Case #"<<t<<": "<<num<<endl;
		else
			cout<<"Case #"<<t<<": Bad magician!"<<endl;
	}
	return 0;
}