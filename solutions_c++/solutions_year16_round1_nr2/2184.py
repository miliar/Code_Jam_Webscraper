#include <bits/stdc++.h>
using namespace std;

#define MOD 1000000007

typedef long long ll;
typedef pair<int,int> pii;
typedef vector<int> vi;
typedef long long ll; 
typedef unsigned long long ull;
typedef pair<ll,ll> pll;
typedef pair<int,int> pii;
typedef vector<int> vi;
typedef vector<long long> vll;
ifstream fin("B-large.in");
ofstream fout("B-large.out");
#define cin fin
#define cout fout
map<int,int> myMap;
vector<int> myList;
int main(){
	int t;
	cin>>t;
	for(ll iter=1;iter<=t;iter++){
		myMap.clear();
		myList.clear();
		cout<<"Case #"<<iter<<": ";
		int n,temp;
		cin>>n;
		for(int i=0;i<n;i++){
			for(int j=0;j<2*n-1;j++){
				cin>>temp;
				// cout<<"reading"<<temp<<endl;
				myMap[temp]++;
			}
		}
		for(map<int,int>::iterator it=myMap.begin();it!=myMap.end();it++){
			// cout<<it->first<<" "<<it->second<<endl;
			if(it->second%2){
				myList.push_back(it->first);
			}
		}
		sort(myList.begin(),myList.end());
		for(int i=0;i<myList.size();i++){
			cout<<myList[i]<<" ";
		}cout<<endl;
		

	}

	return 0;
}
