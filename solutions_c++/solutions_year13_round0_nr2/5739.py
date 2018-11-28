#include <iostream>
#include <cstring>

using namespace std;

#define INDEX 100

int field[INDEX+1][INDEX+1];
int n,m;

bool col_check(int col, int value)
{
	if (field[INDEX][col] > value) return false;

	int x;
	for(x = 0; x < n; x++)
		if (field[x][col] > value) break;

	if (x == n){
		field[INDEX][col] = value;
		return true;
	}

	return false;
}

int main()
{
	int cases,t,x,y,z,max;
	bool failed;

	cin>>cases;
	for (t = 0; t < cases; t++){
		cout<<"Case #"<<t+1<<": ";
		cin>>n>>m;
			
		for(x = 0; x < n; x++){
			cin>>field[x][0];
			field[x][INDEX] = field[x][0];
			
			for(y = 1; y < m; y++){
				cin>>field[x][y];
				if (field[x][y] > field[x][INDEX]) field[x][INDEX] = field[x][y];
			}
		}

		if ((n == 1)||(m == 1)){
			cout<<"YES\n";
			continue;
		}

		failed = false;
		memset(field[INDEX], -1, INDEX*sizeof(int));

		for(x = 0; x < n && !failed; x++){
			for(y = 0; y < m; y++){
				if (field[x][y] < field[x][INDEX]){
					if (!col_check(y,field[x][y])){
						failed = true;
						break;
					}
				}
			}
		}
 
		if (failed)
			cout<<"NO\n";
		else
			cout<<"YES\n";

	}

	return 0;
}
