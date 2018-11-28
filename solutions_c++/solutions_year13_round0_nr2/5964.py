#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int N,M;
int T;
int a[200][200];

bool all_one_row(int i)
{
	for (int j = 0 ; j < M ; ++j)
		if (a[i][j] != 1){
//			cout << "row" << i << " " << j << endl;
			return false;
		}
	return true;
}

bool all_one_column(int j)
{
    for (int i = 0 ; i < N ; ++i)
        if (a[i][j] != 1){
//			cout << "col" << i << " " << j << endl;
            return false;
		}
    return true;
}

bool solve()
{
	int covered = 0;
	for (int i = 0 ; i < N ; ++i)
		for (int j = 0 ; j < M ; ++j){
			if (a[i][j] == 1 && !all_one_row(i) && !all_one_column(j)){
//						cout << i << " " << j << endl;
						return false;			
			}
		}
	return true;
}


int main()
{
	ifstream input("in.txt");
	input >> T;
	for (int k = 0 ; k < T ; ++k){
		input >> N >> M;
		for (int i = 0 ; i < N ; ++i)
			for (int j = 0 ; j < M ; ++j)
				input >> a[i][j];
		bool ans = solve();
		string ans_str = ans?"YES":"NO";
		cout << "Case #" << k+1 << ": " << ans_str << endl;		
	 
	}
	return 0;
}
