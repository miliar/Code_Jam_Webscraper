#include "iostream"
#include "cstdio"
#include "algorithm"
#include "math.h"
#include "windows.h"
#include "queue"
#include "map"
#include "stack"
#include "fstream"
#define L(x) (x<<1+1)
#define R(x) (x<<1+2)
#define REP(a,b) for(int a=0;a<b;a++)
#define RREP(a,b) for(int a=b-1;a>=0;a--)
#define ITR(a,b) for(;a!=b;a++)
#define Pause system("pause");
using namespace std;

typedef long long ll;
int Main();
int main(int argc, char const *argv[]){
	Main();
	return 0;
}
int Main(){
	ofstream fout("GCJ_A.txt");
	ifstream fin("GCJ_A");
	int t;
	fin>>t;
	int l1,l2;
	int c,ans;
	int a1[4][4],a2[4][4];
	REP(i,t){
		fin>>l1;
		l1--;
		REP(n,4)REP(m,4)
			fin>>a1[n][m];
		fin>>l2;
		l2--;
		REP(n,4)REP(m,4)
			fin>>a2[n][m];
		c=0;
		/*REP(n,4)fout<<a1[l1][n];
		fout<<endl;
		REP(n,4)fout<<a2[l2][n];
		fout<<endl;*/
		REP(n,4)REP(m,4)
			if(a1[l1][n]==a2[l2][m]){
				ans=a1[l1][n];
				c++;
			}
		fout<<"Case #"<<i+1<<": ";
		if(c==1)fout<<ans<<endl;
		if(c==0)fout<<"Volunteer cheated!"<<endl;
		if(c>1)fout<<"Bad magician!"<<endl;
	}
}