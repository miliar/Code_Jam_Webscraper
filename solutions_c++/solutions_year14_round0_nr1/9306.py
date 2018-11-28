#include <string>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <bitset>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <fstream>
#include <math.h>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>
#include <valarray>
#include <memory.h>
#include <sstream>
#include <string>

using namespace std;

#define all(n) (n).begin(),(n).end()
#define rall(n) (n).rbegin(),(n).rend()
#define mp make_pair
#define pb push_back
#define sz size()
#define F first
#define S second
#define FO(i,x) for(int i=0;i<x;i++)

#define READ(s) freopen(s, "r", stdin)
#define WRITE(s) freopen(s, "w", stdout)
//  int dx[]={-2,-2,-1,-1,1,1,2,2}; int dy[]={-1,1,-2,2,-2,2,-1,1}; // Knight Dir
//  int dx[]={-1,-1,-1,0,1,1,1,0}; int dy[]={-1,0,1,1,1,0,-1,-1};  // 8 Dir
//  int dx[]={0,1,-1,0}; int dy[]={1,0,0,-1}; // 4 Dir
int arr[5][5];
int main(){
     READ("A-small-attempt0.in");
      WRITE("A-small-attempt0.out");
	 int t,x,a=1;
	 cin>>t;
	 while(t--){
	 	  cin>>x;
	 	  x--;
	 	  map <int,bool> m;
		  FO(i,4) 
		  FO(j,4) {
		  	  cin>>arr[i][j];
		  	  if(i==x) m[arr[i][j]]=1;
		  }
		  cin>>x;
		  x--;
	 	  vector <int> v;
	 	  FO(i,4) 
	 	  FO(j,4) {
		  	  cin>>arr[i][j];
		  	  if(i==x) {
		  	  	 if(m.find(arr[i][j])!=m.end()) v.pb(arr[i][j]);
		  	  } 
		  }
		  if(v.sz==0) cout<<"Case #"<<a++<<": Volunteer cheated!"<<endl;
		  else if(v.sz>1) cout<<"Case #"<<a++<<": Bad magician!"<<endl;
		  else cout<<"Case #"<<a++<<": "<<v[0]<<endl;
	 }
	 return 0;
}
