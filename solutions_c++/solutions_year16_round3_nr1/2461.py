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
	boost
	fileio
	int t,i,j,n,x,y,z,k,yi,zi;
	//char s[2001];
	int a[27],b[10];
	cin>>t;
	//cout<<t;
	f1(i,1,t){
	    cin>>n;
	    x=0;
		f(j,0,n){
			cin>>a[j];
			x+=a[j];
		}
		cout<<"Case #"<<i<<": ";
		//cout<<x<<" ";

		while(x>3){
            y=-1;
            f(j,0,n){
                if(a[j]>y){
//                        z=y;
                        y=a[j];
//                        zi=yi;
                        yi=j;
                }
            }
            z=-1;
            f(j,0,n){
                if(j!=yi && a[j]>z){
                    z=a[j];
                    zi=j;
                }
            }
            //cout<<y<<" "<<z<<" ";
            if(y<x/2){
                if(y>=2){
                    a[yi]-=2;x-=2;
                    cout<<char('A'+yi)<<char('A'+yi)<<" ";
                }
                else if(y==1){
                    a[yi]--;a[zi]--;x-=2;
                    cout<<char('A'+yi)<<char('A'+zi)<<" ";
                }
            }
            else if(y==x/2 && z<y){
                if(y>=2){
                    a[yi]-=2;x-=2;
                    cout<<char('A'+yi)<<char('A'+yi)<<" ";
                }
                else if(y==1){
                    a[yi]--;a[zi]--;x-=2;
                    cout<<char('A'+yi)<<char('A'+zi)<<" ";
                }
            }
            else if(y==x/2 && z==y){
                    a[yi]--;a[zi]--;x-=2;
                    cout<<char('A'+yi)<<char('A'+zi)<<" ";
            }

            //x--;
		}
		if(x==3){
            f(j,0,n){
                if(a[j]==1){
                        cout<<char('A'+j)<<" ";
                        a[j]--;
                        x--;
                        break;
                }
            }
		}
		if(x==2){
            k=0;
            f(j,0,n){
                if(k==0 && a[j]==1){
                    cout<<char('A'+j);
                    k=1;
                    a[j]--;
                    x--;
                } else if(a[j]==1){
                    a[j]--;
                    cout<<char('A'+j)<<" ";
                    x--;
                }
            }
		}

		cout<<endl;
	}

	return 0;
}
