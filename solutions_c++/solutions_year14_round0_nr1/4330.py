#include <iostream>
#include <unordered_set>
using namespace std;

int main()
{
	freopen("input.txt", "r", stdin);
    freopen("output.txt","w",stdout);

	int i,j,num;
	cin >> num;
	for(i=0;i<num;i++)
	{
		int r1,r2,res;
		cin >> r1;
		unordered_set<int> can;
		for(j=0;j<4;j++)
		{
			int temp[4];
			cin >> temp[0];
			cin >> temp[1];
			cin >> temp[2];
			cin >> temp[3];
			if(j+1==r1)
			{
				can.insert(temp[0]);
				can.insert(temp[1]);
				can.insert(temp[2]);
				can.insert(temp[3]);
			}
		}
		cin >> r2;
		for(j=0;j<4;j++)
		{
			int temp[4];
			cin >> temp[0];
			cin >> temp[1];
			cin >> temp[2];
			cin >> temp[3];
			if(j+1==r2)
			{
				int match = 0;
				int res;
				if(can.count(temp[0])){match++;res=temp[0];}
				if(can.count(temp[1])){match++;res=temp[1];}
				if(can.count(temp[2])){match++;res=temp[2];}
				if(can.count(temp[3])){match++;res=temp[3];}
				cout << "Case #" << i+1 << ": ";
				if(match>1)
					cout << "Bad magician!" <<endl;
				else if(match==1)
					cout << res <<endl;
				else 
					cout << "Volunteer cheated!" <<endl;
			}
		}
	}
	return 0;
}