#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <sstream>
#include <vector>
#include <iomanip>
#include <cmath>
#include <set>
#include <map>
#include <queue>
#include <climits>
#include <cassert>
 
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
 
#define pb push_back
#define mp make_pair
#define sz size()
#define ln length()
#define forr(i,a,b) for(int i=a;i<b;i++)
#define rep(i,n) forr(i,0,n)
#define all(v) v.begin(),v.end()
#define uniq(v) sort(all(v));v.erase(unique(all(v)),v.end())
#define clr(a) memset(a,0,sizeof a)
#define debug if(1)
#define debugoff if(0)
 
#define print(x) cerr << x << " ";
#define pn() cerr << endl;
#define trace1(x) cerr << #x << ": " << x << endl;
#define trace2(x, y) cerr << #x << ": " << x << " | " << #y << ": " << y << endl;
#define trace3(x, y, z) cerr << #x << ": " << x << " | " << #y << ": " << y << " | " << #z << ": " << z << endl;
 
#define MAX 100010
#define MOD 1000000007
#define endl '\n'

int arr[2000];
int main(){
	int t,cases,n;
	string str ;

	cin>>cases;
	rep(t,cases){

		cin>>n>>str;
		for(int i=0;i<=n;i++){
			arr[i] = str[i]-'0' ;
		}

		int cnt=0; int frnd = 0 ;

		for(int i=0;i<=n;i++){

			if(cnt<i and arr[i] >0 ){
				frnd += (i-cnt);
				cnt = i;
			}

			if(cnt >= i){
				cnt += arr[i];
			}
			
		}

		cout<<"Case #"<<(t+1)<<": "<<frnd<<endl;
	}
	return 0;
}


























