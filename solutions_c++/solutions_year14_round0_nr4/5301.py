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
	ifstream fin("GCJ_D.in");
	ofstream fout("GCJ_D.out");
	int T,n;
	fin>>T;
	REP(Case,T){
		fin>>n;
		double a[n],b[n];
		REP(i,n)fin>>a[i];
		REP(i,n)fin>>b[i];
		sort(a,a+n);
		sort(b,b+n);
		fout<<"Case #"<<Case+1<<": ";
		int i=0,j=0,ans=0;
		while((i<n)&&(j<n)){
			while(((i<n)&&(j<n))&&(a[i]<b[j]))i++;
			if((i==n)||(j==n))break;
			i++;
			j++;
			ans++;
		}
		fout<<ans<<' ';
		i=0,j=0,ans=0;
		while((i<n)&&(j<n)){
			while(((i<n)&&(j<n))&&(a[i]>b[j]))j++;
			if((i==n)||(j==n))break;
			i++;
			j++;
			ans++;
		}
		fout<<n-ans<<endl;
		/*fout<<i<<" "<<j<<endl;
		REP(i,n)fout<<a[i]<<' ';
		fout<<endl;
		REP(i,n)fout<<b[i]<<' ';
		fout<<endl;*/
	}
}