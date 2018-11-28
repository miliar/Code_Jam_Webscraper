#include <iostream>
#include <queue>
#include <map>
#include <set>
#include <utility>
#include <stack>
#include <vector>
#include <fstream>
#include <string>
#include <cstring>

using namespace std;

string cs = "Case #";

int main(int argc, char* argv[])
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	cin >> t;
	for(int l=1;l<=t;l++)
	{
		int p,q;
		cin >> p;
		p--;
		int a[4][4];
		int b[4][4];
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				cin >> a[i][j];
		cin >> q;
		q--;
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				cin >> b[i][j];
		int k=0;
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				if (a[p][i]==b[q][j])
				{
					k++;
				}
		if (k==0)
		{
			cout << cs << l << ": Volunteer cheated!" << endl; 
		} else
			if(k>1)
			{
				cout << cs << l << ": Bad magician!" << endl; 
			} else
			{
				cout << cs << l << ": ";
				for(int i=0;i<4;i++)
					for(int j=0;j<4;j++)
						if (a[p][i]==b[q][j])
						{
							cout << a[p][i] << endl;
							break;
						}
			}
	}
	return 0;
}
