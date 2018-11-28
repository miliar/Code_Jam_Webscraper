#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <set>
#include <string>
#include <cmath>

using namespace std;

typedef long long ll;
int dx[]={1,0,-1,0};
int dy[]={0,1,0,-1};

#define in(x,y) ( (x)>=0 && (y)>=0 && (x)<n && (y)<m )
#define MOD 1000000007
#define INF 2147483647
#define PI 3.1415926535897932384626433832795
#define all(cont) cont.begin(),cont.end()
#define init(a,val) memset(a,val,sizeof(a))
#define F first
#define S second
#define mp make_pair
#define MAX 12000

string rec(char winner,int lev){
	if(lev==0){
		string ret="";
		//cout<< winner;
		return ret+winner;
	}
	string one,two;
	if(winner=='R')
		one=rec('R',lev-1),two=rec('S',lev-1);
	if(winner=='S')
		one=rec('S',lev-1),two=rec('P',lev-1);
	if(winner=='P')
		one=rec('P',lev-1),two=rec('R',lev-1);

	return min(one,two)+max(one,two);
}

int main()
{
	freopen("a.in","r",stdin);
	//freopen("a.out","w",stdout);
	
	int n,c[150],countt[150],i,j;
	string s[3];
//_______________________________________________
	int test_cases,tesT;

	cin>>test_cases;
	for(tesT=0;tesT<test_cases;tesT++){
		cout<<"Case #"<<tesT+1<<": ";
//_______________________________________________
		cin>>n;
		cin>>c['R']>>c['P']>>c['S'];
		
		s[0]=rec('R',n);
		
		s[1]=rec('P',n);
		
		s[2]=rec('S',n);
		//cerr<<endl<<s[0]<<s[1]<<s[2]<<endl;
		for(i=0;i<3;i++){
			
			for(j=0;j<150;j++)countt[j]=0;
			
			for(j=(1<<n)-1;j>=0;j--){
				//cerr<<j<<endl;
				//cerr<<s[i];
				countt[(int)s[i][j]]++;
			}
			
			if(countt['R']==c['R'] && countt['P']==c['P'] && countt['S']==c['S'] ){
				cout<<s[i];
				goto done;
			}
		}
		cout<<"IMPOSSIBLE";

//_______________________________________________
		done:
		cout<<endl;
	}

	cerr<<endl;
	return 0;
}