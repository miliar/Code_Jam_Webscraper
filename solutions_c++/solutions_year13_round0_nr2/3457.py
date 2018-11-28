#include <iostream>
#include <fstream>
#include <cmath>
using namespace std;

int T, m, n;
int grass[110][110];
int flag;
int maxrow[110], maxcol[110];

int main()
{
	ifstream infile("B-large.in");
	ofstream outfile("ans.out");
	//cin >> T;
	infile >> T;
	for(int cnt=1; cnt<=T; cnt++)
	{
		//cin >> n >> m;
		infile >> n >> m;
		flag=0;
		for(int i=0; i<110; i++){
			maxrow[i]=0; maxcol[i]=0;
		}
		for(int i=0 ;i<n; i++)
			for(int j=0; j<m; j++){
				//cin >> grass[i][j];
				infile >> grass[i][j];
				if(maxrow[i]<grass[i][j])
					maxrow[i] = grass[i][j];
				if(maxcol[j]<grass[i][j])
					maxcol[j] = grass[i][j];
			}
		for(int i=0 ;i<n; i++){
			for(int j=0; j<m; j++)
			{
				if(grass[i][j]<maxrow[i] && grass[i][j]<maxcol[j]){
					flag=1;
					break;
				}
			}
		}
		//cout << "Case #" << cnt << ": " ;
		outfile << "Case #" << cnt << ": " ;
		if(flag==0)
			//cout <<  "YES" << endl;
			outfile << "YES" << endl;
		else
			//cout <<  "NO" << endl;
			outfile << "NO" << endl;
	}
	return 0;
}
