//Common headers
#include<iostream>
#include<vector>
#include<utility>
#include<algorithm>
#include<string>
#include<cstdio>

using namespace std;


#define traverse(container, it) for(typeof(container.begin()) it = container.begin(); it != container.end(); it++)
#define rtraverse(container, it) for(typeof(container.rbegin()) it = container.rbegin(); it != container.rend(); it++)
#define efor(i,a,b)               for(int i=a;i<b;i++)

#define TOLERANCE 10e-5
#define MOD 1000000007

typedef unsigned long long ull;
typedef std::pair< int, int > ipair;

#define _1 1
#define _I 2
#define _J 3
#define _K 4
bool SPECIALCASE = false;

	int justI, justK, UI, KU;
	bool justIb, justKb, UIb, KUb;

int PRODUCT[5][5]= {
					{0,0,0,0,0},
					{0,_1,_I,_J,_K},
					{0,_I,-_1,_K,-_J},
					{0,_J,-_K,-_1,_I},
					{0,_K,_J,-_I,-_1}
				};
	
int PD(int p1,int q1){
	//printf("( PRODUCT OF %d,%d)",p1,q1);
	int p = (p1<0)? -p1:p1;
	int q = (q1<0)? -q1:q1;
	int sign= (p1<0)?-1:1;
	if(q1<0)
		sign*=-1;
	
	return sign*PRODUCT[p][q];
}

int main(){
	//printf("%d",PD(-4,3));	return 1;
	//char TM[5] = {'0','1','i','j','k'};
	ios_base::sync_with_stdio(false);
	int testCases= 0;
	cin>>testCases;
	int L,X;
	string s;
	int u;
	for(int tc=1;tc<=testCases;tc++){
		bool possible =false;
		cin >> L >> X;
		cin >> s;
		int v[L];
		efor(i,0,L){
			v[i] = s[i]-'g';
		}
		int p=1;
		
		for(int i=0;i<L ;i++)
			p = PD(p,v[i]);
		
		int u=p;
		
		if((u==-1 && X%2==1) || (u!=1 && u!=-1 && X%4==2) ){	//Else no use looking
			
			int lookFor[2] = {_I,_K};
			int lf = 0;
			bool stillLooking = true;
			int iLimit = min(8,X);//Just to be safe
			p=1;
			for(int i=0;i<iLimit && stillLooking; i++){
				for(int j=0;j<L && stillLooking;j++){
					p = PD(p,v[j]);
					/*
						if(p<0)
						printf("-%c ,", TM[abs(p)]);
					else
						printf("%c ,", TM[abs(p)]);
					*/
					if(p==lookFor[lf]){
						lf++;
						if(lf>=2){
							possible=true;
							stillLooking = false;
						}
					}
				}
			}
		}
		printf("Case #%d: %s\n",tc, ((possible)?"YES":"NO") );
	}
	
	return 0;
}