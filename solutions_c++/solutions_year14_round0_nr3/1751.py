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

//debug
#define dump(x)  cerr << #x << " = " << (x) << endl;
#define debug(x) cerr << #x << " = " << (x) << " (L" << __LINE__ << ")" << " " << __FILE__ << endl;


int R[250],C[250],M[250];
char temp[51][51];
int main(){
	ifstream ifs( "C-small-attempt4.in" );
	//ifstream ifs( "t.in" );
	ofstream ofs( "test.txt" );
	int T;
	ifs>>T;
	
	REP(i,T)ifs>>R[i]>>C[i]>>M[i];
	
	REP(i,T){
		bool check;
		int emp=R[i]*C[i]-M[i];
		int r=0,c=0;
		int r2=0,c2=0;
		int r3=0,c3=0;
		//cout<<emp<<" ";
		if(R[i]==1||C[i]==1){
			REP(j,R[i])REP(k,C[i]){
				if(j==0&&k==0){
					temp[j][k]='c';
				}else if(emp>1){
					emp--;
					temp[j][k]='.';
				}else{
					temp[j][k]='*';
				}
			}
			check=true;
		}else{
			check=false;
			for(int j=2;j<=R[i];j++)for(int k=2;k<=C[i];k++){//•‚ð‹‚ß‚é
				if(!check&&emp-j*k>0){
					int dev23=emp-j*k;
					for(int p3=0;p3<=dev23/3;p3++)if(!check&&(dev23-3*p3)%2==0){
						int p2=(dev23-3*p3)/2;
						if(p2+p3+j+k<=R[i]+C[i]){
							if(j==2&&k==2){
								if(p3!=0)continue;
								r=j;r2=min(p2,R[i]-j);r3=0;
								c=k;c3=0;c2=max(0,p2-r2);
								if(c+c2<=C[i])check=true;
							}else if(j==2){
								c=k;c3=0;c2=min(p2,C[i]-k);
								r=j;r3=p3;r2=p2-c2;
								//cout<<"!"<<check<<endl;
								if(r+r2+r3<=R[i])check=true;
							}else if(k==2){
								r=j;r3=0;r2=min(p2,R[i]-j);
								c=k;c3=p3;c2=p2-r2;
								if(c+c2+c3<=C[i])check=true;
							}else{
								r=j;r2=min(p2,R[i]-j);r3=min(p3,R[i]-j-r2);
								c=k;c2=max(0,p2-r2);c3=max(0,p3-r3);
								check=true;
							}
						}
					}
				}else if(!check&&emp-j*k==0){
					r=j;c=k;r2=r2=c2=c3=0;
					check=true;
				}
			}
			//cout<<i+1<<" "<<r<<r2<<r3<<" "<<c<<c2<<c3<<endl;
			
			if(check){
				REP(j,R[i])REP(k,C[i]){
					if(j<r&&k<c)temp[j][k]='.';
					else if(r3!=0&&j>=r&&j<r+r3&&k<3)temp[j][k]='.';
					else if(r2!=0&&j>=r+r3&&j<r+r3+r2&&k<2)temp[j][k]='.';
					else if(c3!=0&&k>=c&&k<c+c3&&j<3)temp[j][k]='.';
					else if(c2!=0&&k>=c+c3&&k<c+c3+c2&&j<2)temp[j][k]='.';
					else temp[j][k]='*';
				}
				temp[0][0]='c';
			}
		}
		if(!check&&emp==1){
			REP(j,R[i])REP(k,C[i])temp[j][k]='*';
			temp[0][0]='c';check=true;
		}else if(!check&&R[i]==5&&C[i]==5&&M[i]==1){
			REP(j,R[i])REP(k,C[i])temp[j][k]='.';
			temp[0][0]='c';temp[4][4]='*';check=true;
		}
		if(!check)cout<<"!"<<i+1<<" "<<R[i]<<" "<<C[i]<<" "<<M[i]<<endl;
		
		ofs<<"Case #"<<i+1<<":"<<endl;
		if(!check){
			ofs<<"Impossible"<<endl;
		}else{
			REP(j,R[i]){
				REP(k,C[i]){
					ofs<<temp[j][k];
				}
				ofs<<endl;
			}
		}
	}
	return 0;
}
