#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pii;
typedef pair<double,double> pdd;
typedef pair<int, double> pid;
typedef unsigned long long ull;
typedef vector<pii> vpii;
typedef vector<pid> vpid;

#define FO(i,s,e,p) for(int i=(s);i<(e);i+=p)
#define FOD(i,s,e,p) for(int i=(s);i>(e);i-=p)


#define FOR(i,s,e) FO(i,s,e,1)
#define FORE(i,s,e) FOR(i,s,e+1)
#define FORD(i,s,e) FOD(i,s,e,1)
#define FORDE(i,s,e) FORD(i,s,e-1)

#define REP(i,n) FOR(i,0,n)
#define SORT(v) sort((v).begin(),(v).end())
#define UN(v) sort((v).begin(),(v).end()),v.erase(unique(v.begin(),v.end()),v.end())
#define CL(a,b) memset(a,b,sizeof(a))
#define pb push_back
#define mp make_pair

int main() {
	int T, counter = 1;
	cin>>T;
	while(T--){
		int N, M;
		cin>>N>>M;
		vector<vector<int> > arr;
		arr.resize(N);
		REP(i,N) arr[i].resize(M);
		REP(i,N) REP(j,M) cin>>arr[i][j];
		while(true){
	        		int k = 0;
	        		while(k < arr.size()){
	        			if (arr[k].size() == 0){
	        				arr.erase(arr.begin()+k);
	        				continue;
	        			}
	        			k++;
	        		}

	        		if(arr.size() == 0)
	        			break;
						int min = 110;
	        		int minr = 0,minc = 0;
	        		for(int r = 0; r < arr.size(); r++){
		        		for(int c = 0; c < arr[0].size(); c++){
		        			if (min > arr[r][c]){
		        				minr = r;
		        				minc = c;
		        				min = arr[r][c];
		        			}
		        		}
		        	}

		        	int numc = 0, numr = 0;
		        	bool rb = true, cb = true;
		        	for(int j = 0; j < arr[minr].size(); j++)
		        		if (arr[minr][j] == min)
		        			numr++;

		        	if (numr != arr[minr].size())
		        		rb = false;

		        	for(int j = 0; j < arr.size(); j++)
		        		if (arr[j][minc] == min)
		        			numc++;
		        	if (numc != arr.size())
		        		cb = false;

		        	if((cb == false) && (rb == false)){
		        		cout<<"Case #"<<counter++<<": NO"<<endl;
		        		break;
		        	}
		        	if (cb){
		        		for(int j = 0; j < arr.size(); j++)
			        		arr[j].erase(arr[j].begin()+minc);
		        		continue;
		        	}
		        	// clean the the row that is good
		        	else if(rb){
			        	arr.erase(arr.begin() + minr);
		        		continue;
		        	}
	        	}
	        	if(arr.size() !=0)	continue;
	        	cout<<"Case #"<<counter++<<": YES"<<endl;
	}
	
	return 0;
}
