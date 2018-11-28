#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
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
 
using namespace std;
 
#define REPEAT(i,a,b) for(int i=a;i<b;++i)
#define REP(i,n) REPEAT(i,0,n)
#define RREP(i,n) for(int i=n-1;i>=0;--i)
#define EACH(it,v) for(typeof(v.begin()) it=v.begin();it!=v.end();++it)
#define pb push_back
#define all(x) (x).begin(),(x).end()
#define CLEAR(x,with) memset(x,with,sizeof(x))
#define sz size()
#define mkp make_pair
typedef long long ll;
#define EPS 1e-12

int main(){
	int T;
	cin>>T;
	for(int x=1;x<=T;x++){
		double C,F,X;
		cin>>C>>F>>X;
		double currFact = 2.00;
		double currCookie = 0.00;
		double currTime,nextTime,totTime=0.00;
		while(1){
			currTime = X/currFact;
			//cout<<currFact<< " "<<currTime<<" ";
			nextTime = C/currFact;
			//cout<<nextTime<<" ";
			nextTime += (X/(currFact+F));
			//cout<<nextTime<<endl;
			
			double mini = min(currTime,nextTime);
			if(currTime-mini <= EPS){
				totTime += currTime;
				break;
				}
			totTime += (C/currFact);
			currFact += F;
			}
		cout<<"Case #"<<x<<": ";
		cout.precision(7);
		cout<<fixed<<totTime<<endl;
		}
	return 0;
	}
	
