
// aymos (Somya Mehdiratta , IIIT Hyderabad)

#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<cstdlib>
#include<vector>
#include<map>
#include<climits>
#include<stack>
#include<queue>
#include<algorithm>

using namespace std;

#define PB push_back
#define FOR(i,s,n) for(int i=(s),_n=(n);i<_n;i++)

typedef long long LL;

int main(int argc, char *argv[]){
	int n;
	cin>>n;
	int t= n;
	while(n--){
		cout<<"Case #"<<t-n<<": "; 
		int a[4][4],b[4][4],ta,tb;
		cin>>ta;
		ta = ta-1;
		FOR(i,0,4)
			FOR(j,0,4)
				cin>>a[i][j];
		cin>>tb;
		tb = tb-1;
		FOR(i,0,4)
			FOR(j,0,4)
				cin>>b[i][j];
		int matches = 0 , first = 0;
		FOR(i,0,4)
			FOR(j,0,4)
				if( a[ta][i] == b[tb][j] ){
					++matches;
					first = a[ta][i];
				}

		if(matches == 1)
			cout<<first<<endl;
		else if(matches == 0)
			cout<<"Volunteer cheated!\n";
		else cout<<"Bad magician!\n";



	}
	return 0;
}
