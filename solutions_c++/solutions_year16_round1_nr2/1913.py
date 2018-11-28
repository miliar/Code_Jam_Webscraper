#include<iostream>
#include<fstream>
#include<string>
#include<algorithm>

using namespace std;
int main() {
	ifstream fin("B-large.in");
	ofstream fout("output.txt");
	int t;
	fin >> t;
	for(int test=1;test<=t;test++){
		int n,i,j;
		fin >> n;
		int result[n];
		int a[2*n-1][n];
		int seen[2501] = {0};
		
		for(i=0;i<2*n-1;i++){
			for(j=0;j<n;j++){
				fin >> a[i][j];
				seen[a[i][j]]++;
			}
		}
		int cur=0;
		for(i=0;i<2501;i++){
			if(seen[i]%2==1){
				result[cur] = i;
				cout << i << endl;
				cur++;
			}
		}
		
		sort(result,result+n);
		
		fout << "Case #" << test << ": ";
		for(i=0;i<n;i++){
			fout << result[i] << " ";
		}
		fout << endl;
	}
	
	return 0;
}
