#include<iostream>
#include<vector>
#include<climits>
using namespace std;
#define LL long long

int T;
int main(void)
{
	cin >> T;
	for(int t=0;t<T;t++)
	{
		int canbe[16];
		for(int i=0;i<16;i++)
			canbe[i]=1;
		for(int z=0;z<2;z++)
		{
			int row;
			cin >> row;
			for(int r=1;r<=4;r++)
				for(int k=0;k<4;k++)
				{
					int num;
					cin >> num;
					if(r!=row)
						canbe[num-1]=0;
				}
		}
		int howm=0, sol;
		for(int i=0;i<16;i++)
			if(canbe[i]==1)
				howm++, sol=i;
		cout << "Case #"<<(t+1)<<": ";
		if(howm==1)
			cout << sol+1;
		if(howm==0)
			cout << "Volunteer cheated!";
		if(howm>1)
			cout << "Bad magician!";
		cout << endl;
	}

	
}
