/*ckpeteryu*/
#include<iostream>
#include<iomanip>
#include<sstream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cctype>
#include<climits>
#include<cmath>
#include<bitset>
#include<string>
#include<ctime>
#include<typeinfo>
#include<functional>
#include<map>
#include<set>
#include<vector>
#include<stack>
#include<queue>
//#include<regex>
#include<algorithm>
using namespace std;
#define FOR(i,s,e) for(int i=(s);i<(int)(e);i++)
#define FOE(i,s,e) for(int i=(s);i<=(int)(e);i++)
#define FOD(i,s,e) for(int i=(s);i>=(int)(e);i--)
#define FORVEC(i,a) for(int i=0;i<(int)((a).size());i++)
#define pb push_back
#define mp make_pair
#define CLR(s,x) memset(s,x,sizeof(s))
#define LL long long int
#define L unsigned long int

int nt;
int maxDepth,bound;

L powers[11][33];

L GetNonTrivialDivisor(L val){
	if(val<=1)return 0;
	L srVal=(L)ceil(sqrt(val));	
	for(L i=2;i<=srVal;i++){
		if(val%i==0){
			return i;
		}
	}
	return 0;
}

void dfs(int len, string val){
	if(bound > 0){
		if(len>=maxDepth){
			bool good=true;
			vector<L> divisors;
			FOE(k,2,10){
				L r=0;
				FOR(i,0,len){
					r+=powers[k][len-i-1]*(val.at(i)=='1'?1:0);
				}
				L div=GetNonTrivialDivisor(r);				
				if(div == 0){
					good=false;
					break;
				}else{					
					divisors.pb(div);
				}
			}
			if(good){
				printf("%s %ld",val.c_str(),divisors[0]);
				FOR(i,1,9){
					printf(" %ld",divisors[i]);
				}
				printf("\n");
				bound--;
			}
		}else{
			dfs(len+1,val.substr(0,len-1)+"0"+val[len-1]);
			dfs(len+1,val.substr(0,len-1)+"1"+val[len-1]);
		}
	}
}

void precompute(){
	int len=16;
	CLR(powers,0);
	FOE(k,2,10){
		powers[k][0]=1;
		FOR(i,1,len){
			powers[k][i]=powers[k][i-1]*k;			
		}
	}
}

int main(int argc, char **argv){
	//ios_base::sync_with_stdio(false);
	//const clock_t begin_time = clock();
	precompute();
	scanf("%d",&nt);
	FOE(k,1,nt){
		scanf("%d%d",&maxDepth,&bound);
		printf("Case #%d:\n",k);
		dfs(2,"11");
	}
	//std::cout <<endl<< float( clock () - begin_time ) /  CLOCKS_PER_SEC;
	return 0;
}