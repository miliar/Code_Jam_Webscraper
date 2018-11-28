#include <cmath>
#include <climits>
#include <queue>
#include <vector>
#include <map>
#include <cstdlib>
#include <fstream>
#include <iomanip>   
#include <iostream>  
#include <sstream>  // istringstream buffer(myString);
#include <stack>
#include <algorithm>
#include <cstring>
#include <cassert>
#include<bits/stdc++.h>

using namespace std;

#define bit(x,i) 					(x&(1<<i))  		//select the bit of position i of x
#define lowbit(x) 					((x)&((x)^((x)-1))) //get the lowest bit of x
//#define hBit(msb,n) 				asm("bsrl %1,%0" : "=r"(msb) : "r"(n)) //get the highest bit of x, maybe the fastest
#define max(a,b) 					(a<b?b:a)
#define f(i,L,R) 					for (int i = L; i < R; i++) //next four are for "for loops"
#define f1(i,L,R) 					for (int i = L; i <= R; i++)
#define fd(i,L,R) 					for (int i = L; i > R; i--)
#define fd1(i,L,R) 					for (int i = L; i >= R; i--)
#define si(a) 						scanf("%d", &a) 	
#define sl(a) 						scanf("%lld", &a)
#define sc(a) 						scanf("%c", &a)
#define ss(a) 						scanf("%s",a)
#define clr(a,x) 					memset(a,x,sizeof(a)) //set elements of array to some value
#define sz(x) 						((int)(x).size())
#define each(i,t) 					for (typeof(t.begin()) i=t.begin(); i!=t.end(); i++) // traverse an STL data structure
#define ALL(c) 						(c).begin(),(c).end() //handy for function like "sort()"
#define PRESENT(c,x) 				((c).find(x) != (c).end()) 
#define CPRESENT(c,x) 				(find(ALL(c),x) != (c).end()) 
#define ll 							long long
#define boost 						ios_base::sync_with_stdio(false); //to synchronize the input of cin and scanf
#define fileio 						freopen("in.txt","r",stdin); freopen("out.txt","w",stdout);
#define trace1(x)                	cerr << #x << ": " << x << endl;
#define trace2(x, y)             	cerr << #x << ": " << x << " | " << #y << ": " << y << endl;
#define trace3(x, y, z)          	cerr << #x << ": " << x << " | " << #y << ": " << y << " | " << #z << ": " << z << endl;

//for map, pair
#define mp make_pair
#define fi first
#define se second

#define MAXN 	10000
const long long mod=1000000007 ;
#define inf 	0x7fffffff
#define PI 		3.1415926535897932384626

//for vectors
#define pb push_back
typedef vector<int> vi; 
typedef vector<vi> vvi; 
typedef pair<int,int> pp; 
typedef vector<pp> vpp ;
typedef vector<ll> VI ;
typedef vector<VI> VVI; 
typedef pair<ll,ll>  PP;
typedef vector<PP>  VPP ;

// directions
const int fx[4][2] = {{0,1}, {0,-1}, {1,0}, {-1,0}};
const int fxx[8][2] = {{0,1}, {0,-1}, {1,0}, {-1,0}, {1,1}, {1,-1}, {-1,1}, {-1,-1}};

int powmod(ll a,int b) {ll res=1;if(a>=mod)a%=mod;for(;b;b>>=1){if(b&1)res=res*a;if(res>=mod)res%=mod;a=a*a;if(a>=mod)a%=mod;}return res;}
ll gcd(ll a , ll b){return b==0?a:gcd(b,a%b); }

int main(){
	ifstream fin;
	ofstream fout;
	fin.open("in.txt");
	fout.open("out.txt");
	int t,i,j,n,x,y,z,k;
	char s[2001];
	int a[26],b[10];
	fin>>t;
	f1(i,1,t){
		f(j,0,26){
			a[j]=0;
		}
		f(j,0,10){
			b[j]=0;
		}
		fin>>s;
		k=strlen(s);
		f(j,0,k){
			a[s[j]-'A']++;
		}
		b[0]=a['Z'-'A'];
		a['E'-'A']-=b[0];
		a['R'-'A']-=b[0];
		a['O'-'A']-=b[0];
		a['Z'-'A']=0;

		b[2]=a['W'-'A'];
		a['T'-'A']-=b[2];
		a['O'-'A']-=b[2];
		a['W'-'A']=0;

		b[4]=a['U'-'A'];
		a['F'-'A']-=b[4];
		a['O'-'A']-=b[4];
		a['R'-'A']-=b[4];
		a['U'-'A']=0;

		b[5]=a['F'-'A'];
		a['V'-'A']-=b[5];
		a['I'-'A']-=b[5];
		a['E'-'A']-=b[5];
		a['F'-'A']=0;

		b[6]=a['X'-'A'];
		a['I'-'A']-=b[6];
		a['S'-'A']-=b[6];
		a['X'-'A']=0;

		b[7]=a['S'-'A'];
		a['E'-'A']-=(2*b[7]);
		a['V'-'A']-=b[7];
		a['N'-'A']-=b[7];
		a['S'-'A']=0;

		b[8]=a['G'-'A'];
		a['E'-'A']-=b[8];
		a['I'-'A']-=b[8];
		a['H'-'A']-=b[8];
		a['T'-'A']-=b[8];
		a['G'-'A']=0;

		b[3]=a['H'-'A'];
		a['T'-'A']-=b[3];
		a['R'-'A']-=b[3];
		a['E'-'A']-=(2*b[3]);
		a['H'-'A']=0;

		b[1]=a['O'-'A'];
		a['N'-'A']-=b[1];
		a['E'-'A']-=b[1];
		a['O'-'A']=0;

		b[9]=a['E'-'A'];
		a['N'-'A']-=(2*b[9]);
		a['I'-'A']-=b[9];
		a['E'-'A']=0;
		fout<<"Case #"<<i<<": ";
		f(j,0,10){
			while(b[j]){
				fout<<j;
				b[j]--;
			}
		}
		fout<<endl;
	}
	return 0;
}