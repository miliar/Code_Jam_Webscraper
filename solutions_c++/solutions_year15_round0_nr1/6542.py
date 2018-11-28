//============================================================================
// Name        : .cpp
// Author      : Moaz
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <cstring>
#include <string.h>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>
#include <limits.h>

using namespace std;

#define all(v) v.begin(),v.end()
#define rep(i,m) for(int i=0;i<(int)(m);i++)
#define rep2(i,n,m) for(int i=n;i<(int)(m);i++)
#define clr(v,val) memset(v,val,sizeof(v))
#define  ll long long


typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<bool> vb;

string alpha = "abcdefghijklmnopqrstuvwxyz";
string alphC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";


int main() {

    freopen ("A-large.in","r",stdin);
    freopen ("output.txt","w",stdout);

	int t,n;
	cin >> t;
	char shinyess[1009];
	rep2(ii,1,t+1){
		int res = 0;
		cin >> n >> shinyess;
//		rep(kk,n+1){
//			cout<< shinyess[kk];
//		}
//		cout<<endl;
		int count = 0;
		rep(jj,n+1){

			if( ((int)(shinyess[jj]-'0')) >= 1){
	//			cout << "here\n" << endl;
				res+= max((jj-count),0);
				count+=max((jj-count),0);
			}
			count+=(shinyess[jj]-'0');
//			cout << count <<" "<<res <<  endl;
		}
		printf("Case #%d: %d\n",ii,res);
	}


	return 0;
}
