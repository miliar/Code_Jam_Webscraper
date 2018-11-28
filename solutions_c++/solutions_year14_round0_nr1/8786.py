//SKimov gJam Magic Trick
#include <iostream>
#include <vector>
using namespace std;
struct set
{
	int set1[4];
	int set2[4];
};
int main()
{
	int inputcount = 0;
	cin>>inputcount;
	vector<set> sets;
	for(int i = 0; i < inputcount;i++)
	{
		set current;
		int row;
		cin >> row;
		for(int j=0; j< 4;j++)
		{
			
			int unused[4];
			if(j+1 == row){
				cin >> current.set1[0] >> current.set1[1]>>current.set1[2]>>current.set1[3];
			}else{
				cin >> unused[0] >> unused[1]>>unused[2]>>unused[3];
			}
		}
		cin >> row;
		for(int j=0; j< 4;j++)
		{
			int unused[4];
			if(j+1 == row){
				cin >> current.set2[0] >> current.set2[1]>>current.set2[2]>>current.set2[3];
			}else{
				cin >> unused[0] >> unused[1]>>unused[2]>>unused[3];
			}
		}
		sets.push_back(current);
	}
	for (int i = 0; i < sets.size();i++)
	{
		cout <<"Case #"<<i+1<<": ";
		int count = 0;
		int answer = 0;
		for(int j = 0; j< 4;j++)
		{
			for(int k =0; k < 4;k++)
			{
				if(sets[i].set1[j] == sets[i].set2[k])
				{
					count++;
					answer = sets[i].set1[j];
				} 
			}
		}
		if(count == 0)
		{
			cout << "Volunteer cheated!"<<endl;
		}
		if(count == 1)
		{
			cout << answer<<endl;
		}
		if(count > 1)
		{
			cout << "Bad magician!"<<endl;
		}
	}
	return 0;
}