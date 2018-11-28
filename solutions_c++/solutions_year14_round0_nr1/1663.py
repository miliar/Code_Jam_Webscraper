#include <iostream>
#include <fstream>


using namespace std;

int main()
{
	int t,n,m;
	int a[4][4],b[4][4];
	int i,j,k,ans,ansn;
	ofstream f2("output1.txt");
	ifstream f1("A-small-attempt0.in");
	f1>>t;
	for (i = 0; i < t; i++)
	{
		f1>>n;
		for (j = 0; j < 4; j++)
			for (k = 0; k < 4; k++){
				f1>>a[j][k];
			}
		f1>>m;
		for (j = 0; j < 4; j++)
			for (k = 0; k < 4; k++){
				f1>>b[j][k];
			}
		ansn = 0;
		for (j = 0; j < 4; j++)
			for (k = 0; k < 4; k++)
				if (a[n-1][j] == b[m-1][k]){
					ansn++;
					ans = a[n-1][j];
				}
		
		if (ansn == 0)
			f2<<"Case #"<<i+1<<": "<<"Volunteer cheated!"<<endl;
		else if (ansn == 1)
			f2<<"Case #"<<i+1<<": "<<ans<<endl;
		else
			f2<<"Case #"<<i+1<<": "<<"Bad magician!"<<endl;
	}
	
	
}
