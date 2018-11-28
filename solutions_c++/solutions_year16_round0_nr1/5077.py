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
#define LL long long unsigned int

int nt,N;

void Solve(int k,int N){
	if(N==0){		
		printf("Case #%d: INSOMNIA\n",k);
		return;
	}
	int tN,cnt=0,step=0;
	bool good=false;
	int a[10];
	CLR(a,0);
	FOE(i,1,1000){
		tN=N*i;
		do{
			int j=tN%10;
			tN/=10;
			if(a[j]==0){
				a[j]=1;
				if(++cnt==10){
					step=i;
					good=true;
					break;
				}
			}
		}while(tN>0);
		if(good)break;
	}
	if(good)
		printf("Case #%d: %d\n",k,step*N);
	else
		printf("Case #%d: INSOMNIA\n",k);
}

int main(int argc, char **argv){
	//ios_base::sync_with_stdio(false);
	//const clock_t begin_time = clock();
	scanf("%d",&nt);
	FOE(k,1,nt){
		scanf("%d",&N);
		Solve(k,N);
	}
	//std::cout <<endl<< float( clock () - begin_time ) /  CLOCKS_PER_SEC;
	return 0;
}