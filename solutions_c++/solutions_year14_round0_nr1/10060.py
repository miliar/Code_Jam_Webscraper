#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <set>

using namespace std;

int main(int argc, char const *argv[])
{
	int cases;
	scanf("%d",&cases);
	vector<int> v1[4];
	vector<int> v2[4];
	set<int>::iterator it;
	pair<set<int>::iterator,bool> ret;
	for(int cas=1; cas <= cases; cas++)
	{
		int count = 0, ans=0;
		for(int i=0; i<4; i++)
		{
			v1[i].clear();
			v2[i].clear();
		}
		int guess1, guess2, tmp=0;
		scanf("%d",&guess1);
		for(int j=0; j<4; j++)
		{	
			for(int i=0; i<4 ;i++)
			{
				scanf("%d",&tmp);
				v1[j].push_back(tmp);
			}
		}
		scanf("%d",&guess2);
		for(int j=0; j<4; j++)
		{	
			for(int i=0; i<4 ;i++)
			{
				scanf("%d",&tmp);
				v2[j].push_back(tmp);
			}
		}
		for(int i=0; i<4; i++)
		{
			for(int j=0; j<4 ;j++)
			{
				//cout << v1[guess1-1][i] << " " << v2[guess2-1][j] << endl;
				if(v1[guess1-1][i] == v2[guess2-1][j])
				{
					count++;
					ans = v1[guess1-1][i];
					break;
				}
			}
		}
		if(count==0)
			cout << "Case #" << cas << ": Volunteer cheated!" << endl;
		else if(count==1)
			cout << "Case #" << cas << ": " << ans << endl;
		else
			cout << "Case #" << cas << ": Bad magician!" << endl;
	}
	return 0;
}