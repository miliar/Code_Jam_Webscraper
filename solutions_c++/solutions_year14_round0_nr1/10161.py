#include <iostream>
#include <set>
#include <conio.h>
#include <fstream>




#define cin fin
#define cout fout

using namespace std;

ifstream fin ("in.txt");
ofstream fout ("out.txt");

int main()
{
	int t;
	cin >> t;
	for(int o = 0 ; o < t ; ++o)
	{
		int r;
		cin >> r;
		int a[5][5];
		int b[5][5];
		int x[5] = {0};
		int y[5] = {0};
		for(int i = 0 ; i < 4 ; ++i)
			for(int j = 0 ; j < 4 ;++j)
				cin >> a[i][j];
		
		for(int i = 0 ; i < 4 ; ++i) x[i] = a[r - 1][i];
		
		cin >> r;
		for(int i = 0 ; i < 4 ; ++i)
			for(int j = 0 ; j < 4 ;++j)
				cin >> a[i][j];
		
		for(int i = 0 ; i < 4 ; ++i) y[i] = a[r - 1][i];
		
		set<int> ans;
		
		for(int i = 0 ; i < 4 ; ++i)
		{
			for(int j = 0 ; j < 4 ; ++j)
			{
				if(x[i] == y[j])
				{
					ans.insert(x[i]);
				}
			}
		}
		
		cout << "Case #" << o + 1 << ": "; 
		
		if(ans.size() == 0) 
		{
			cout << "Volunteer cheated!" << endl;
		}
		else if(ans.size() == 1) cout << *ans.begin() << endl;
		else cout << "Bad magician!" << endl;
				
	}
	
 	getch();
 	return 0;	
}
