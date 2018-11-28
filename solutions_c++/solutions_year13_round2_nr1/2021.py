#include <iostream>
#include <fstream>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <ctime>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <set>
#include <stack>
#include <map>

#define FOR(i,n) for(int i=0,_n=n;i<_n;i++)
#define FORD(i,n) for(int i=n;i>=0;i--)
#define FORR(i,s,n) for(int i=s,_n=n;i<_n;i++)
#define FORRD(i,n,s) for(int i=n;i>=s;i--)
#define mp make_pair
#define pb push_back
#define pii pair<int,int>
#define pli pair<ll,int>
#define fs first
#define sec second

#define maxn 100000
using namespace std;
typedef long long ll;

int arr[maxn];
int main(){
	int t,a,n;
	cin>>t;
	FORR(ttt,1,t + 1){
		cin>>a>>n;
		FOR(i,n) cin>>arr[i];
		sort(arr,arr + n);
	
		int c=0;
		while(c < n && arr[c] < a) a+=arr[c++];
		
		int tochg=n - c; // remove all next
		
		int tmp=0;
		while(c < n){
			if(arr[c] >= a && a == 1) break;
			while(arr[c] >= a){ a+=(a - 1); tmp++; }
			a+=arr[c];
			c++;
			tochg=min(tochg,tmp + n - c);
		}
		
		cout<<"Case #"<<ttt<<": "<<tochg<<"\n";
	}
	return 0;
}
