#include<iostream>
#include<map>
#include<string>
#include<vector>
#include<algorithm>
#include<fstream>
using namespace std;

/*problems
*/

/*plans
*/

//classes
typedef pair<int,int> P;

//constants
int INF=INT_MAX/2;

//variables
ifstream fin;
ofstream foot,fout;
int T,N,M,lawn[200][200];

//data structures
int x[200],y[200];

//functions
void solve()
{
	for(int i=0; i<N; i++){
		x[i]=0;
		for(int j=0; j<M; j++)x[i]=max(x[i],lawn[i][j]);
	}

	for(int i=0; i<M; i++){
		y[i]=0;
		for(int j=0; j<N; j++)y[i]=max(y[i],lawn[j][i]);
	}

	for(int i=0; i<N; i++){
		for(int j=0; j<M; j++){
			if(lawn[i][j]!=min(x[i],y[j])){
				fout<<"NO"<<endl;
				return;
			}
		}
	}
	fout<<"YES"<<endl;
}

int main()
{
	fin.open("C:\\Users\\fumi\\Downloads\\B-large.in");
	fout.open("C:\\Users\\fumi\\Downloads\\B-large-answer.txt");
	foot.open("C:\\Users\\fumi\\Downloads\\B-large-sample.txt");

	fin>>T;

	for(int i=0; i<T; i++){
		fin>>N>>M;
		for(int j=0; j<N; j++){
			for(int k=0; k<M; k++)fin>>lawn[j][k];
		}

		fout<<"Case #"<<i+1<<":"<<" ";
		solve();
	}

	fin.close();
	fout.close();
	foot.close();

	system("pause");
	return 0;
}