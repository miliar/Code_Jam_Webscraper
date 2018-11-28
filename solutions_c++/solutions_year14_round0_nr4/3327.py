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
#define EXP 1e7


int main(){
	int T;
	cin>>T;
	for(int x=1;x<=T;x++){
		int N;
		cin>>N;
		long double d;
		vector<int> Na,Ke;
		REP(i,N){
			cin>>d;
			Na.pb(int(d*double(EXP)));
			}
		REP(i,N){
			cin>>d;
			Ke.pb(int(d*double(EXP)));
			}
		sort(all(Na));
		sort(all(Ke));
		/*
		REP(i,N)	cout<<Na[i]<< " ";
		cout<<endl;
		REP(i,N)	cout<<Ke[i]<<" ";
		cout<<endl<<"Iterations"<<endl;
		*/
		int opt=0,noOpt=0;
		int best=-1;
		
		//Cheat
		if(Na[0] > Ke[N-1])	opt = N;
		else{
			int count=0;
			REP(i,N){
				if(Na[i] > Ke[i])	count++;
				}
			best = max(best,count);
			REP(i,N){
				vector<int> Na1(Na),Ke1(Ke);
				Na1.erase(Na1.begin(),Na1.begin()+i+1);
				Ke1.erase(Ke1.begin()+N-i-1,Ke1.begin()+N);
				
				/*
				REP(j,Na1.sz)	cout<<Na1[j]<<" ";
				cout<<endl;
				REP(j,Ke1.sz)	cout<<Ke1[j]<<" ";
				cout<<endl;
				*/
				
				RREP(i,Ke1.sz){
					REP(j,Na1.sz){
						if(Na1[j] > Ke1[i]){
							Na1[j] = -1;
							break;
							}
						}
					}
				count=0;
				REP(i,Na1.sz)	if(Na1[i] == -1)	count++;
				//cout<<count<<endl;
				best = max(best,count);
				}
			opt = best;
		}
		
		//no cheat
		vector<int> Na1(Na),Ke1(Ke);
		REP(i,Na1.sz){
			REP(j,Ke1.sz){
				if(Ke1[j]!=-1 && Na1[i] < Ke1[j]){
					Ke1[j] = -1;
					break;
					}
				}
			}
		int count=0;
		REP(i,Ke1.sz)	if(Ke1[i] == -1)	count++;
		//cout<<count<<endl;
		noOpt = N-count;
		
		cout<<"Case #"<<x<<": ";
		cout<<opt<<" "<<noOpt<<endl;
		}
	return 0;
	}
	
