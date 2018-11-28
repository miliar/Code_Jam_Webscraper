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
using namespace std;

typedef long long ll;
int Main();
int main(int argc, char const *argv[]){
	Main();
	return 0;
}
int s[10000];
bool tr[10000];
int Main(){
	ofstream fout("1.out");
	ifstream fin("1.in");
	int t;
	int n,x;
	fin>>t;
	REP(cases,t){
		int ct=0;
		fin>>n>>x;
		REP(i,n)fin>>s[i];
		REP(i,n)tr[i]=false;
		sort(s,s+n);
		for(int i=n-1;i>=0;i--){
			if(tr[i])continue;
			tr[i]=true;
			for(int j=n-1;j>=0;j--){
				if(tr[j])continue;
				if(s[i]+s[j]<=x){
					tr[j]=true;
					ct++;
					break;
				}
			}
		}
		fout<<"Case #"<<cases+1<<": "<<n-ct<<endl;
	}
}