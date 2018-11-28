/*
	In the Name Of GOD
	TRIPLE NARENGIES:)
*/
#include <vector>
#include <map>
#include <cstring>
#include <cmath>
#include <iostream>
#include <algorithm>
#include <sstream>
#include <complex>
#include <queue>
#include <stack>
#include <map>
#include <bitset>
#include <iomanip>
#include <set>
#include <stack>
#include <stdio.h>

using namespace std;
#define N 10020
#define MAXN 60
#define X first
#define Y second
#define CLR(x,a) memset(x,a,sizeof(x))
#define FOR(i,b) for(ll i=0;i<(b);i++)
#define FOR1(i,b) for(ll i=1;i<=(b);i++)
#define FORA(i,a,b) for(ll i=(a);i<=(b);i++)
#define FORB(i,b,a) for(ll i=(b);i>=(a);i--)
#define sh(x) cerr<<(#x)<<" = "<<(x)<<endl
#define EPS 0.00001
#define ull unsigned long long int
#define ll long long 
#define MP make_pair
#define PB push_back
#define ALL(v) (v).begin(),(v).end()
#define sz size()
#define EXIST(a,b) find(ALL(a),(b))!=(a).end()
#define Sort(x) sort(ALL(x))
#define UNIQUE(v) Sort(v); (v).resize(unique(ALL(v)) - (v).begin())
#define timestamp(x) printf("Time : %.3lf s.\n", clock()*1.0/CLOCKS_PER_SEC)
//const double PI = acos(-1);
typedef complex<double> point;
typedef pair<int,int> pii;
typedef pair<int, pii> piii;
typedef vector<int> vi;
typedef vector<vi > vii;
typedef vector<pii> vpii;
typedef vector<piii> vpiii;

int l,x;
string in;
//1 i=2 , j=3 , k = 4
#define I 2
#define J 3
#define K 4


int next(int last , char c){
	if(c=='i'){
		switch(last){
			case -K:return -J;break;
			case -J:return K;break;
			case -I:return 1;break;
			case -1:return -I;break;
			case 1:return I;break;
			case I:return -1;break;
			case J:return -K;break;
			case K:return J;break;
		}
	}	
	if(c=='j'){
		switch(last){
			case -K:return I;break;
			case -J:return 1;break;
			case -I:return -K;break;
			case -1:return -J;break;
			case 1:return J;break;
			case I:return K;break;
			case J:return -1;break;
			case K:return -I;break;
		}
	}	
	if(c=='k'){
		switch(last){
			case -K:return 1;break;
			case -J:return -I;break;
			case -I:return J;break;
			case -1:return -K;break;
			case 1:return K;break;
			case I:return -J;break;
			case J:return I;break;
			case K:return -1;break;
		}
	}	
}



bool solve(){
	int flag = 0;
	int tmp = 1;
	while(flag<in.sz){
		tmp = next(tmp , in[flag]);
		flag++;
	//	sh(tmp);
		if(tmp ==I)
			break;
	}
	tmp =1;
	//sh("here");
	while(flag<in.sz){
		tmp = next(tmp , in[flag]);
	//	sh(tmp);
		flag++;
		if(tmp==J)
			break;
	}
	//sh("here");
	tmp =1;
	while(flag<in.sz){
		tmp = next(tmp , in[flag]);
	//	sh(tmp);
		flag++;
		if(tmp==K && flag==in.sz)
			return true;
	}
	return false;
}


int main()
{
	ios::sync_with_stdio(false);
	int T; cin>>T;
	int test = 0;
	while(T--)
	{
		test++;
		cout<<"Case #"<<test<<": ";
		cin>>l>>x;
		cin>>in;
		string tmp = in;
		FOR(i,x-1){
			in+=tmp;
		}
		cout<<((solve())?"YES":"NO")<<endl;

	}
}
