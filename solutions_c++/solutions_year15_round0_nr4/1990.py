#include<iostream>
using namespace std;
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<vector>
#include<map>
#include<queue>
#include<algorithm>
#include<cmath>
#include<set>
#include<ctime>
#include<stack>
#include<list>
typedef  pair<int,int> pii;
#define rep(i,j,n) for(i=j;i<n;i++)
#define pb push_back
#define sz(a) a.size()
#define ff first
#define ss second 
#define lli long long int

int main() {
		
	ios::sync_with_stdio(false);
	freopen ("inp.txt","r",stdin);
	freopen ("out.txt","w",stdout);
	int t;
	
	cin>>t;
	int x,r,c,ca=0;
	while(t--){
		ca++;
		cin>>x>>r>>c;
		
		if(r<c)	swap(r,c);
		
		if(x==1)	cout<<"Case #"<<ca<<": GABRIEL\n";
		else if (x == 2){
			if((r*c)%2 == 0)
			cout<<"Case #"<<ca<<": GABRIEL\n";
			else
			cout<<"Case #"<<ca<<": RICHARD\n";
		}
		else if(x == 4){
			if((r == 4 and c == 3)||(r == 4 and c == 4))	cout<<"Case #"<<ca<<": GABRIEL\n";
			else 											cout<<"Case #"<<ca<<": RICHARD\n";
		}
		else if(x == 3){
			if(r<3)	cout<<"Case #"<<ca<<": RICHARD\n";
			else{
				if(r == 3){
					if(c == 1)				cout<<"Case #"<<ca<<": RICHARD\n";
					else 					cout<<"Case #"<<ca<<": GABRIEL\n";
				}
				if(r == 4){
					if(c == 3) 				cout<<"Case #"<<ca<<": GABRIEL\n";
					else 					cout<<"Case #"<<ca<<": RICHARD\n";
				}
			}
		}
		
	}
	
	return 0;
}
