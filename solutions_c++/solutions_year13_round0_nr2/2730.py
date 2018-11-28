#include <iostream>
#include <fstream>
#include <algorithm>
//#include <string>
//#include <vector>
#include <cstdio>
#include <cstdlib>
#include <cmath>

//#include <memory.h>


#define PI acos(-1)
#define eps 1e-9

#define out(x) (cout<<#x<<":"<<x<<" ")
#define outln(x) (cout<<#x<<":"<<x<<endl)
#define outs(x) (cout<<x)
#define outline (cout<<endl)
#define mssleep(time) usleep((time)*(10*1000))

#define FOR_I(begin,end) for (int i=begin;i<end;i++)
#define FOR_J(begin,end) for (int j=begin;j<end;j++)
#define FOR_K(begin,end) for (int k=begin;k<end;k++)
#define FOR_I_J(B1,E1,B2,E2) FOR_I(B1,E1) FOR_J(B2,E2)
#define FOR_I_J_K(B1,E1,B2,E2,B3,E3) FOR_I_J(B1,E1,B2,E2) FOR_K(B3,E3)
#define FOR(begin,end) FOR_I(begin,end)
#define FORN(end) FOR_I(0,end)

using namespace std;

	template <typename T>
	void debug_a(T * data,int begin,int end){
		for (int i=begin;i<end;i++) cout<<"["<<i<<"]: "<<data[i]<<"\t";cout<<endl;
	}
	template <typename T>
	void debug_a(T * data,int end){
		debug_a(data,0,end);
	}
	template <typename T>
	void debug_a2(T * data,int end1,int end2){
		for (int i=0;i<end1;i++){cout<<"row "<<i<<endl; for (int j=0;j<end2;j++) cout<<"["<<i<<","<<j<<"] "<<data[i][j]<<"\t";cout<<endl;} 
	}
	template <typename T>
	T checkmin(T & data,T value){
		data = min(data,value);
		return data;
	}
	
	inline double rand_double(double range){
		return  ((double)rand()/(double)RAND_MAX)*range;
	}

const int N = 500;

int G[N][N];
int n,m;

	bool work(){
		FOR_I_J(0,n,0,m){
			int me = G[i][j];
			bool rx = true;
			FOR_K(0,n){
				if ( G[k][j] > me ){

					rx = false;
					break;
				}
			}
			bool cx = true;
			FOR_K(0,m){
				if ( G[i][k] > me ){
					cx = false;
					break;
				}
			}
			if (!rx && !cx){
				//printf("Wrong at %d %d\n",i,j);
				return false;
			}
		}
		return true;
	}

	void inputing(){
		scanf("%d %d",&n,&m);
		FOR_I_J(0,n,0,m){
			scanf("%d",&G[i][j]);
		}
	}

int main(){
	int cases;
	scanf("%d",&cases);
	FOR_I(0,cases){
		inputing();
		bool result = work();
		if (result){
			printf("Case #%d: YES\n",i+1);
		}
		else {
			printf("Case #%d: NO\n",i+1);
		}
	}
	return 0;
}







