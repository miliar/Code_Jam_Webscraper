/*
* abdurak
* Google CodeJam 2014 - Round 2
* Problem A
* Game after game after game...
*/
#include <iostream>
#include <fstream>
#include <cmath>
#include <algorithm>
#include <iomanip>
#include <vector>
#include <utility>

#define pi pair<int,int>
#define vpi vector<pair<int,int> >

#define forn(i,n) for(int i=0;i<n;i++)
#define forr(i,a,b) for(int i=a;i<=b;i++)
#define forn2(i,ni,j,nj) forn(i,ni) forn(j,nj)

//DEBUGGING
#define _s cout<<
#define _d <<" "<<
#define _e <<endl;
long long INF=100000000000LL;

//(int *)calloc(1000000,sizeof(int));
//(int *)malloc(1000000*sizeof(int));

using namespace std; 
ifstream fin ("A.in");
ofstream fout ("A.out");

int main(){
    int T;
    fin>>T;
    forr(iT,1,T){
        fout<<"Case #"<<iT<<": ";
        int N,X;
        fin>>N>>X;
        int s[10000];
        forn(i,N){
            fin>>s[i];
        }
        int sp=0,ep=N-1;
        int disk=0;
        sort(s,s+N);
        cout<<N<<" ";
        while(sp<ep){
            if(s[sp]+s[ep]<=X){
                sp++;
                ep--;
            }else{
                ep--;
            }
            disk++;
        }
        if(sp==ep)  disk++;
        _s disk _d sp _d ep _e
        fout<<disk;
        fout<<endl;
    }
    system("pause");
	return 0;
}
