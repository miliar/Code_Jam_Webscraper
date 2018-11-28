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


long long gcd(long long a,long long b){
	long long tmp;
	while(b!=0){
		tmp=b;
		b=a%b;
		a=tmp;
	}
	return a;
}

int nodecount(vector<string> p){
	set<string> ex;
	int n=p.size();
	ex.insert("");
	for(int i=0;i<n;++i){
		for(int j=1;j<=p[i].size();++j){
			ex.insert(p[i].substr(0,j));
		}
	}
	return ex.size();
}
void judge(){
	int m,n;
	cin>>m>>n;
	vector<string> x(m);
	REP(i,m){
		cin>>x[i];
	}
	vector<int> nums(1<<m,0);
	for(int i=1;i<(1<<m);++i){
		vector<string> td;
		int j=0,hh=i;
		while(hh>0){
			if(hh&1)td.push_back(x[j]);
			hh>>=1;
			++j;
		}
		nums[i]=nodecount(td);
	}
	int max=0,count=0;
	if(n==1){
		max=nums[(1<<m)-1];
		count=1;
	}
	else if(n==2){
		for(int i=1;i<(1<<m);++i){			
			for(int j=i+1;j<(1<<m);++j){
				if((i&j)==0&&(i|j)==(1<<m)-1){
					if(nums[i]+nums[j]==max)count++;					
					if(nums[i]+nums[j]>max){max=nums[i]+nums[j];count=1;}
				}
			}
		}
		count*=2;
	}
	else if(n==3){
		
		for(int i=1;i<(1<<m);++i){			
			for(int j=i+1;j<(1<<m);++j){	
				for(int k=j+1;k<(1<<m);++k){
					if((i&j)==0&&(i&k)==0&&(j&k)==0&&(i|j|k)==(1<<m)-1){
						int t=nums[i]+nums[j]+nums[k];
						if(t==max)count++;					
						if(t>max){max=t;count=1;}
					}
				}
			}
		}
		count*=6;
	}
	else {
		
		for(int i=1;i<(1<<m);++i){			
			for(int j=i+1;j<(1<<m);++j){	
				for(int k=j+1;k<(1<<m);++k){
					for(int l=k+1;l<(1<<m);++l){
						if((i&j)==0&&(i&k)==0&&(j&k)==0&&(j&l)==0&&(l&k)==0&&(l&i)==0&&(i|j|k|l)==(1<<m)-1){
							int t=nums[i]+nums[j]+nums[k]+nums[l];
							if(t==max)count++;					
							if(t>max){max=t;count=1;}
						}
					}
				}
			}
		}
		
		count*=24;
	}
	cout<<max<<" "<<count;
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