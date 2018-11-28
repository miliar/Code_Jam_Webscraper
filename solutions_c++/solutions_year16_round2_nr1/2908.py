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

//*
#define TRY
//	#define SMALL
		#define LARGE

typedef long long ll;
#define N 1000000007


//A. Dynamic Grid
void Solve();

int r,c;
bool b[102][102];
bool f[102][102]={false};
int fx[4]={0,1,0,-1};
int fy[4]={1,0,-1,0};

void main() 
{
#ifdef TRY
	freopen("1.txt", "rt", stdin);
	//freopen("C-large.txt","wt",stdout);
	//freopen("2.out","wt",stdout);
#endif
#ifdef SMALL
	freopen("A-small-attempt2.in","rt",stdin);
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

		Solve();
	}
}


void Solve(){
	string a;
	cin>>a;
	int t[26]={0};
	int ans[10]={0};
	int len = a.length();
	for(int i=0;i<len;i++){
		t[a[i]-'A']++;
	}
	int m =t[25];
	ans[0]=m;
	t[4] -= m;t[13] -= m; t[14] -= m;//0

	m=t[23];ans[6]=m;t[18]-=m;t[8]-=m;t[23]-=m;//6

	m=t[18];ans[7]=m;t[18]-=m;t[4]-=2*m;t[13]-=m;t[21]-=m;//7

	m=t[21];ans[5]=m;t[8]-=m;t[21]-=m;t[4]-=m;t[5]-=m;//5

	m=t[5];ans[4]=m;t[5]-=m;t[17]-=m;t[14]-=m;t[20]-=m;//4

	m=t[22];ans[2]=m;t[14]-=m;t[19]-=m;t[22]-=m;//2

	m=t[6];ans[8]=m;t[4]-=m;t[6]-=m;t[8]-=m;t[7]-=m;t[19]-=m;//8

	m=t[14];ans[1]=m;t[4]-=m;t[13]-=m;t[14]-=m;

	m=t[8];ans[9]=m;

	ans[3]=t[19];

	for(int i=0;i<10;i++){
		int p=ans[i];
		while(p>0) {cout<<i;p--;}
	}
	cout<<endl;
	
}
