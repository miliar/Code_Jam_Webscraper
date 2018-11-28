#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <climits>
#include <stdlib.h>
#include <stdio.h>
using namespace std;
#define REP(i,n) for(int i=0; i<n; i++)
#define FOR(i,st,end) for(int i=st;i<end;i++)
#define db(x) cout << (#x) << " = " << x << endl;
#define mp make_pair
#define pb push_back
#define mod 1000003
typedef long long int ll;
int main(){
	int t;
	int ans=0;
	ll n,temp,x;
	cin>>t;
	FOR(tt,1,t+1){
        ans=0;
		set<int> digit;
		cin>>n;
		if(n==0){
			cout<<"Case #"<<tt<<": "<<"INSOMNIA\n";
			continue;
		}
		x=n;
		for(;;){
		
			temp=n;
			while(n!=0){
				digit.insert(n%10);
				n/=10;
				if(digit.size()==10){
					cout<<"Case #"<<tt<<": "<<temp<<"\n";
					ans=1;
					break; 
				}
			}
			n=temp;
			if(ans){
				break;
			}
			n+=x;
	    }
	}
	
}

