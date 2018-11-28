#include<iostream>
#include<fstream>
#include<bitset>
#include<vector>
#include<deque>
#include<map>
#include<set>
#include<queue>
#include<string>
#include<algorithm>
#include<cmath>
#include<ctime>
#include<cstdio>
using namespace std;
#if defined wolf
const string ok="OK";
const string kk="	";
ofstream nnew("B-small-attempt.in",ios::app);
ifstream fin("B-small-attempt.in");
#define fout cout
#define Endl endl
#else
ifstream fin("B-small-attempt.in");
ofstream fout("B-small-attempt.out");
#endif
vector<vector<int> >TT;
vector<int> record;
int core(const vector<int> pancake,int h){
	vector<int> record;
	int ttime=0;
	for(int i=0;i!=pancake.size();++i){
		ttime+=(pancake[i]-1)/h;
	}
	return ttime;
}
int main(){
	int T,n=1;;
	fin>>T;
	while(T--){
		int k,ans=999999999,mmax=0;;
		fin>>k;
		vector<int> pancake;
		for(int i=0;i!=k;++i){
			int r;
			fin>>r;
			mmax=max(mmax,r);
			pancake.push_back(r);
		}
		for(int h=1;h!=mmax+1;++h){
			int ttime=core(pancake,h);
			ans=min(ans,h+ttime);
		}
		fout<<"Case #"<<n<<":  "<<ans<<endl;
		++n;
	}
	//-------------------------*/
	#if defined wolf
	cout<<endl<<(double)clock()/CLOCKS_PER_SEC<<'s'<<endl;
	system("pause");
	#endif
	return 0;
}
//Designed by wolf
//Sun Apr 12 2015
