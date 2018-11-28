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
//#define mp make_pair
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
 
#define MAX 10010
#define MOD 1000000007
#define endl '\n'

int mp[5][5] = {{0,0,0,0,0,},{0,1,2,3,4},{0,2,-1,4,-3},{0,3,-4,-1,2},{0,4,3,-2,-1}};
int pro(int a, int b){

	int sign = 1;
	if(a<0){
		sign *= -1 ; a*= -1;
	}
	if(b<0){
		sign *= -1 ; b*= -1 ;
	}

	return (mp[a][b]*sign);

}
char s[MAX];
int cumi[MAX];
int cumk[MAX];
int arr[MAX];
int main(){

	/*for(int i=0;i<=4;i++){
		for(int j=0;j<=4;j++){
			cout<<mp[i][j]<<"\t";
		}
		cout<<endl;
	}*/
	
	int t,cases,l,x ;
	string str ;
	cin>>cases;
	rep(t,cases){

		cin>>l>>x;
		cin>>str ;
		for(int i=0;i<l*x;i++)
			s[i] = str[i%l];

		for(int i=0;i<l*x;i++){
			if(s[i] == 'i')arr[i]=2;
			else if(s[i] == 'j')arr[i]=3;
			else
				arr[i]=4;
		}
		
		cumi[0]=arr[0];
		for(int i=1;i<l*x;i++)
			cumi[i] = pro(cumi[i-1],arr[i]);

		cumk[l*x-1 ] =arr[l*x-1];
		for(int i=l*x-2;i>=0;i--)
			cumk[i] = pro(arr[i],cumk[i+1]);

		/*for(int i=0;i<l*x;i++)
			cout<<cumi[i]<<"\t";
		cout<<endl;
		for(int i=0;i<l*x;i++)
			cout<<cumk[i]<<"\t";
		cout<<endl;   */

		bool iexists = false;bool b = false;
		for(int i=0;i<l*x-1;i++){
			if(!iexists and (cumi[i] == 2))iexists = true;

			if(iexists and (cumi[i] == 4) and (cumk[i+1] == 4)){
				b = true;
				break;
			}
		}
		if(b)
			cout<<"Case #"<<(t+1)<<": YES"<<endl;
		else
			cout<<"Case #"<<(t+1)<<": NO"<<endl;
	}
	return 0;
}

			































