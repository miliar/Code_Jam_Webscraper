//*/
#include <cstdio>
#include <iostream>
#include <cstring>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <deque>
#include <set>
#include <map>
#include <list>
#include <limits>
#include <queue>
#include <stdexcept>
#include <iomanip> 
#include <sstream>

using namespace std;
bool Solve();
bool Judge();
void Fill(long long a);
#define TRY
//#define SMALL
#define LARGE

bool flag[10]={false};

long long cnt=0;
void main() 
{
#ifdef TRY
	freopen("1.txt", "rt", stdin);
	//freopen("2.out","wt",stdout);
#endif
#ifdef SMALL
	freopen("A-small-attempt0.in","rt",stdin);
	freopen("A-small.txt","wt",stdout);
#endif
#ifdef LARGE
	freopen("A-large.in","rt",stdin);
	freopen("A-large.txt","wt",stdout);
#endif
	int Numcase;
	cin>>Numcase;
	for(int test=1;test<=Numcase;test++)
	{
		cout<<"Case #"<<test<<": ";
		if(Solve()) cout<<cnt;
		else cout<<"INSOMNIA";
		cout<<endl;
	}
}
bool Solve(){
	for(int i=0;i<10;i++){
		flag[i]=false;
	}			
	long long a,s;
	cin>>a;
	if(a==0) {return false;}
	s=a;
	Fill(s);
	cnt=1;
	while(!Judge()){
		s=s+a;
		Fill(s);
		cnt=s;
	}
	return true;
	
}

void Fill(long long a){
	int dit;
	while(a>0){
		dit = a%10;
		flag[dit]=true;
		a=a/10;
	}
}
bool Judge(){
	for(int i=0;i<10;i++){
		if(flag[i]==false) return false;
	}
	return true;
}
