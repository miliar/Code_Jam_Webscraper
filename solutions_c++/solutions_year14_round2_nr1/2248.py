#include <stdio.h> 
#include <stdlib.h>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <ctime>
#include <fstream>


using namespace std;
#define FOR(i,a,b) for(int i=(a);i<(b);i++)
#define CLR(a) memset((a), 0 ,sizeof(a))
#define REP(i,n) for(int i = 0; i < (int)(n); ++i)
#define ALL(a)  (a).begin(),(a).end()
#define RALL(a) (a).rbegin(), (a).rend()
#define PB push_back
#define MP make_pair
#define SZ(a) int((a).size())
#define EACH(i,c) for(typeof((c).begin()) i=(c).begin(); i!=(c).end(); ++i)
#define EXIST(s,e) ((s).find(e)!=(s).end())
#define SORT(c) sort((c).begin(),(c).end())

//conversion
//------------------------------------------
inline int toInt(string s) {int v; istringstream sin(s);sin>>v;return v;}
template<class T> inline string toString(T x) {ostringstream sout;sout<<x;return sout.str();}

//typedef
//------------------------------------------
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef pair<int, int> PII;


int main(){
	ifstream ifs( "A-small-attempt0.in" );
	ofstream ofs( "test.txt" );
	int T;
	ifs>>T;
	vector<string>answer;
	REP(k,T){
		int n;
		string str[100];
		string com[100];
		int count[100][100];
		CLR(count);
		ifs>>n;
		REP(i,n)ifs>>str[i];
		char t;
		REP(i,n){
			int c=1;
			REP(j,SZ(str[i])){
				if(j==0){
					t=str[i][j];
					com[i]="";
					continue;
				}
				if(str[i][j]!=t){
					count[i][SZ(com[i])]=c;
					com[i].push_back(t);
					t=str[i][j];
					c=1;
				}else{
					c++;
				}
			}
			com[i].push_back(t);
			count[i][SZ(com[i])]=c;
		}
		int res=0;
		bool flag=false;
		REP(i,n-1){
			flag=false;
			int t1=100000;
			FOR(j,i+1,n){
				//cout<<com[i]<<" "<<com[j]<<endl;
				if(com[i]==com[j]){
					flag=true;
					int t2=0;
					REP(j2,SZ(com[i])+1){
						t2+=abs(count[i][j2]-count[j][j2]);
						//cout<<k<<" "<<count[i][j2]<<" "<<count[j][j2]<<" "<<t2<<endl;
					}
					t1=min(t2,t1);
				}
			}
			cout<<t1<<endl;
			//cout<<k<<" "<<i<<" "<<flag<<endl;
			if(flag==false){
				//cout<<k<<"!"<<endl;
				break;
			}else{
				res+=t1;
			}
		}
		if(flag){
			answer.push_back(toString(res));
		}else{
			answer.push_back("Fegla Won");
		}
	}
	
	REP(i,T){
		ofs<<"Case #"<<i+1<<": "<<answer[i]<<endl;
		cout<<"Case #"<<i+1<<": "<<answer[i]<<endl;
	}
	return 0;
}
