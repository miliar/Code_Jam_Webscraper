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
ofstream nnew("A-small-attempt.in",ios::app);
ifstream fin("A-small-attempt.in");
#define fout cout
#define Endl endl
#else
ifstream fin("A-small-attempt.in");
ofstream fout("A-small-attempt.out");
#endif
int main(){
	int T,n=1;
	fin>>T;
	while(T--){
		int r,ans=0,people=0;
		fin>>r;
		char t;
		for(int i=0;i!=r+1;++i){
			fin>>t;
			int u=t-'0';
			if(people>=i){
				people+=u;
			}else{
				ans+=i-people;
				people+=i-people;
				people+=u;
			}
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
