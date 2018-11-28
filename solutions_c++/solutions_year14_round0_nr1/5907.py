#include <iostream>
#include <set>
#include <stdio.h>
using namespace std;
class Magic
{
	public:
		Magic(){}
		~Magic(){}
		void Input(int idx);
		int Judge();
		int Ans;
	private:
		int matrix[2][4][4];
		int row[2];
};
void Magic::Input(int idx)
{
	cin>>row[idx];
	for(int i = 0; i < 4; i++)
	{
		for(int j = 0; j < 4; j++)
		{
			cin>>matrix[idx][i][j];
		}
	}
}
int Magic::Judge()
{
	int count = 0 ;
	set<int> setPick;
	for(int i = 0; i < 4; i++)
	{
		int rowNum = row[0] - 1;
		setPick.insert( matrix[0][rowNum][i] );
	}
	for(int i = 0; i < 4; i++)
	{
		int rowNum = row[1] - 1;
		if(setPick.find( matrix[1][rowNum][i] ) != setPick.end())
        {
            this->Ans = matrix[1][rowNum][i];
			count++;
        }
	}
	return count;
}
int main()
{
  //  freopen("A-small-attempt0.in","r",stdin);
  //  freopen("A-small-attempt0.out","w",stdout);
	int cas;
	cin>>cas;
	for(int i = 1; i <= cas; i++)
	{
		Magic magic;
		magic.Input(0);
		magic.Input(1);
		int ans = magic.Judge();
		cout<<"Case #"<<i<<": ";
		if( ans == 0 )
		{
			cout<<"Volunteer cheated!"<<endl;
		}
		else if( ans == 1 )
		{
			cout<<magic.Ans<<endl;
		}
		else if( ans >= 2 )
		{
			cout<<"Bad magician!"<<endl;
		}
	}
}
