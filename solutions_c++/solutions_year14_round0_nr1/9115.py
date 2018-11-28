#include<iostream>
#include<vector>
#include<cstdlib>

using namespace std;



int main()
{
	int t,tc,a1,a2,i,j,m1[4][4],m2[4][4],cnt,index;
	bool v[20];
	cin>>tc;
	t=0;
	while(t++ < tc){

		cnt = 0;

		for(i=0;i<=16;i++)
			v[i] = false;

		cin>>a1;

		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				cin>>m1[i][j];
			}

		}

		cin>>a2;

		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				cin>>m2[i][j];
			}

		}


		for(i=0;i<4;i++)
		{
			v[m1[a1-1][i]] = true;
		}


		for(i=0;i<4;i++)
		{
			if(v[m2[a2-1][i]] == true){
				cnt++;
				index = m2[a2-1][i];
			}
		}

		cout<<"Case #"<<t<<": ";

		if(cnt == 1){
			cout<<index;
		}
		else if(cnt == 0)
		{
			cout<<"Volunteer cheated!";
		}
		else {
			cout<<"Bad magician!";
		}
	}

	return 0;
}