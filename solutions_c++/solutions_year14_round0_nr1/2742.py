#include <iostream>
#include <cmath>
#include <algorithm>
#include <fstream>
#include <vector>
#include <set>
#include <stack>
#include <iomanip>
#include <queue>
#include <list>
#include <utility>
#include <map>

using namespace std;
ifstream fin;
ofstream fout;
int t,ans1,ans2;
int arr[4][4],ar[4][4];
int k = 0;
int ans3;
int main(){
	std::ios_base::sync_with_stdio(false);
	fin.open("A-small-attempt0.in");
	fout.open("ss.txt");
	fin.tie(NULL);
	fin >> t;
	for(int l = 0; l < t; l++){
		k = 0;
		fin >> ans1;
		for(int i =0; i < 4; i++)
			for(int j = 0; j < 4; j++)
				fin >> arr[i][j];
		fin >> ans2;
		for(int i =0; i < 4; i++)
			for(int j = 0; j < 4; j++)
				fin >> ar[i][j];
		for(int i = 0; i < 4; i++){
			for(int j = 0; j < 4; j++){
				if(arr[ans1-1][i] == ar[ans2-1][j]){
					ans3 = ar[ans2-1][j];
					k++;
				}
			}
		}
		fout << "Case #" << l + 1 << ": ";
		if(k==0)
			fout << "Volunteer cheated!\n";
		else if(k==1)
			fout << ans3 << "\n";
		else fout << "Bad magician!\n";
	}
	return 0;
}