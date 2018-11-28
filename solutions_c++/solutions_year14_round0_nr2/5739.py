#include "iostream"
#include "cstdio"
#include "algorithm"
#include "math.h"
#include "windows.h"
#include "queue"
#include "map"
#include "stack"
#include "fstream"
#include <iomanip>
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
	ifstream fin("GCJ_B.in");
	freopen("GCJ_B.out","w",stdout);
	int T;
	fin>>T;
	REP(Case,T){
		double c,f,x;
		fin>>c>>f>>x;
		double t=0,r=2;
		while((x-c)/r>x/(r+f)){
			t+=c/r;
			r+=f;
		}
		t+=x/r;
		printf("Case #%d: %.7lf\n",Case+1,t);
	}

}