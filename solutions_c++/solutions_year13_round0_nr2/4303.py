#include <iostream>
#include <cmath>
#include <vector>
#include <utility>
#include <algorithm>
#include <queue>
#include <stack>
#include <string>
#include <cstring>
#include <map>
#include <list>
#include <cstdio>
#include <cctype>
#include <sstream>
#include <fstream>

using namespace std;

#define ll long long
#define ms1(m) memset((m),-1,sizeof((m)))
#define ms0(m) memset((m),0,sizeof((m)))
#define SORT(v) sort((v).begin(),(v).end())
#define CINFASTER cin.sync_with_stdio(false)
#define sz size()
#define pb(x) push_back(x)
#define mp(a,b) make_pair((a),(b))
#define all(x) (x).begin(),(x).end()


//google codeJam~!
int main (){

	ifstream fin("B-large.in");
	ofstream fout("output.txt");
	int tc; fin>> tc ;
	for(int k=0;k<tc; ++k){
		int H, L ; 
		fin>>H>>L;
		vector<vector<int> > v(H , vector<int>(L,0)) ;
		vector<int> Hmax(H , 0) ;
		vector<int> Lmax(L , 0) ;
		for(int i=0;i<H; ++i){
			for(int j=0;j<L;++j){
				fin>>v[i][j] ;
				Hmax[i] = max(Hmax[i] , v[i][j]) ;
				Lmax[j] = max(Lmax[j] , v[i][j]) ;
			}
		}


		bool brk = false, isPossible = true ;
		for(int i=0;i<H; ++i){
			for(int j=0;j<L;++j){
				//이 칸을 포함한 행과 열 둘다에 나보다 큰놈이 있으면 안됩니다.
				if(v[i][j] < Hmax[i] && v[i][j] < Lmax[j]){
					isPossible = false ;
					brk = true ;
					break ;
				}
			}
			if(brk) break ;
		}
		if(isPossible){
			fout<<"Case #"<<k+1<<": YES"<<endl;
		}
		else{
			fout<<"Case #"<<k+1<<": NO"<<endl;
		}
	}
	
	fin.close() ;
	fout.close();
	return 0;
}