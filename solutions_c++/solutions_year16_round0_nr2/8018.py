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
	int t,len;
	int ans=0;
	string str;
	cin>>t;
	FOR(tt,1,t+1){
		ans=0;
		cin>>str;
		len=str.size();
		char prev=str[0];
		string temp="";
		temp+=str[0];
		FOR(i,1,len){
		   
		   if(str[i]!=prev){
		       temp+=str[i];
		   }
		   prev=str[i];
	   }
	  // cout<<"temp "<<temp<<endl;
		prev=temp[0];
		len=temp.size();
		FOR(i,1,len){
		
		   if(temp[i]!=prev){
			   if(prev=='-'){
				   ans++;
			   }
			   else{
				   ans+=2;
			   }
			   prev='+';
			   continue;
		   }
		prev=temp[i];
	   }
	if(ans==0&&prev=='-'){
		ans++;
	}
		cout<<"Case #"<<tt<<": "<<ans<<"\n";
	}
}


