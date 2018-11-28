#include <iostream>
#include <fstream>
#include <algorithm>
//#include <string>
//#include <vector>
#include <stdio.h>
#include <stdlib.h>
#include <cmath>

#include <memory.h>


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

typedef long long LL;

const int N=4000;

struct node{
	LL begin;
	LL end;
	LL p;
	bool operator < (const node &x) const{
		if ( this->begin == x.begin ){
			return this->end < x.end;
		}
		return this->begin < x.begin;
	}
};

LL n,m;
node arr[N];

LL pos[N*100];
int num;

node stack[N];

LL MOD = 1000002013;

	void inputing(){
		cin>>n>>m;
		int j=0;
		FOR_I(0,m){
			cin>>arr[i].begin>>arr[i].end>>arr[i].p;
			pos[j++] = arr[i].begin;
			pos[j++] = arr[i].end;
		}

		sort(pos,pos + j);

		//in pos
		LL last = -1;
		num =0;
		FOR_I(0,j){
			if (last != pos[i]){
				pos[num++] = pos[i];
			}
			last = pos[i];
		}
	}

	void cal(LL & result, node & x,LL end,LL q){
		LL w = end - x.begin + 1;
		LL temp = ( w*(w-1)/2 ) % MOD;
		//cout<<x.begin<<" -- "<<end<<"  * "<<q<<endl;//debug


		temp = (temp * q) % MOD;
		result = (result + temp) % MOD;
	}

	LL work2(){
		LL result2 =0 ;
		FOR_I(0,m){
			cal(result2,arr[i],arr[i].end,arr[i].p);
		}
		return result2;
	}

LL result = 0;
	void work(){
		int top = 0;
		result = 0;
		LL result2 = work2();


		FOR_I(0,num){
			//deal incoming
			stack[top].p =0;
			stack[top].begin = pos[i];
			FOR_J(0,m){
				if ( arr[j].begin == pos[i] ){
					stack[top].p += arr[j].p;
				}
			}
			if (stack[top].p!=0){
				top++;
			}


			//deal outcome
			LL sum = 0;
			FOR_J(0,m){
				if ( arr[j].end == pos[i] )
					sum += arr[j].p;
			}
			if ( 0!= sum ){


				if (top <=0 ) cout<<"ERROR!"<<endl;
				while (sum > 0){
					int k = top-1;
					if (k<0) break;
					if ( sum >= stack[k].p ){
						cal(result,stack[k],pos[i],stack[k].p);
						sum -= stack[k].p;
						top--;
					}
					else {
						cal(result,stack[k],pos[i],sum);
						stack[k].p -= sum;
						sum = 0;
					}
				}
			}

		}

		result = (result - result2 + MOD) % MOD;
	}

int main(){
	int cas;
	cin>>cas;
	FOR_I(1,cas+1){
		inputing();
		work();
		cout<<"Case #"<<i<<": "<<result<<endl;
	}


	return 0;
}



