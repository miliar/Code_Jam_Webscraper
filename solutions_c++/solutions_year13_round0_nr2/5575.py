#include <iostream>
#include <fstream>
using namespace std;

int Grid[105][105];
int sameRow[105];
int sameCol[105];
int Rowmin[105];
int Colmin[105];

int main()
{
	ifstream cin("B-small-attempt0.in");
	ofstream cout("Sevag_lawnmower_small.out");

	int T, N, M;
	cin>>T;

	for (int t=1; t<=T; t++)
	{
		cin>>N>>M;
		for (int i=0; i<N; i++)
			for (int j=0; j<M; j++)
				cin>>Grid[i][j];

		fill(sameCol,sameCol+105,1);
		fill(sameRow,sameRow+105,1);
		
		for (int i=0; i<N; i++){
			bool same=true;
			int mn=Grid[i][0];
			for (int j=1; j<M; j++){
				if (Grid[i][j]!=Grid[i][0]){
					same=false;
					mn=min(mn,Grid[i][j]);
				}
			}
			sameRow[i]=same;
			Rowmin[i]=mn;
		}

		for (int j=0; j<M; j++){
			bool same=true;
			int mn=Grid[0][j];
			for (int i=1; i<N; i++){
				if (Grid[i][j]!=Grid[0][j]){
					same=false;
					mn=min(mn,Grid[i][j]);
				}
			}
			sameCol[j]=same;
			Colmin[j]=mn;
		}

		bool valid=true;
		for (int i=0; i<N; i++){
			for (int j=0; j<M; j++){
				if (Grid[i][j]==Rowmin[i] && Grid[i][j]==Colmin[j])
					if (!sameRow[i] && !sameCol[j])
						valid = false;
			}
		}

		if (valid)	cout<<"Case #"<<t<<": YES"<<endl;
		else	cout<<"Case #"<<t<<": NO"<<endl;

	}

	return 0;
}