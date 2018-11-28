#include <iostream>
#include <queue>
#include <string>
#include <map>
#include <set>
#include <iomanip> 
#include <vector>
#include <list>
#include <utility> 
#include <iterator> 
#include <math.h> 
#include <algorithm> 
#include <stdio.h> 
using namespace std;


#define REP(i,T) for(int i=0;i<T;++i)
#define MP make_pair
#define PII pair<int,int>
#define BG begin
#define ND end
#define VI vector<int>
#define VB vector<bool>
#define ALL(i) i.BG(),i.ND()
#define FORI(i,a,b) for(int i=a;i<b;++i)
#define OUT(i) while(!i.empty())
#define GP(a,b) a[b.first][b.second]
#define EX(a,b) (a.find(b)!=a.end())

void judge(){
	int  a;
	scanf("%d",&a);	
	vector<string> ma(4);
	string tmp;
	REP(i,4){
		if(i+1!=a){
			
			REP(j,4){
				cin>>tmp;

			}
		}
		else{
			REP(j,4){
				cin>>ma[j];
			}
		}
	}
	scanf("%d",&a);	
	vector<string> mb(4);
	REP(i,4){
		if(i+1!=a){
			
			REP(j,4){
				cin>>tmp;

			}
		}
		else{
			REP(j,4){
				cin>>mb[j];
			}
		}
	}
	int count=0,ta=0;
	REP(i,4){
		REP(j,4){
			if(ma[i]==mb[j]){count++;ta=i;}
		}
	}
	if(count==0){
		
		printf("Volunteer cheated!");
	}
	else if(count==1){
		
		cout<<ma[ta];
	}
	else{
		
		printf("Bad magician!");
	}

	return;


}
int main(){
	int t;
	scanf("%d",&t);
	REP(tt,t){
		cerr<<tt<<endl;
		printf("Case #%d: ",tt+1);
		judge();
		
		printf("\n");
	}




	return 1;



}