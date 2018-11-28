//author:- viper_yash
#include <iostream>
#include <cstdio>
#include <vector>
#include <map>
#include <iterator>
#include <set>
#include <algorithm>
#include <cmath>
#include <cstring>
#include <string>
#include <queue>
#include <stack>
#include <sstream>
#include <ctype.h>
#include <utility>
#include <cstdlib>

using namespace std;

#define ll long long
#define md1 1000000007ll
#define md2 10000007ll
#define linf 998877665544332211ll
#define inf 987654321ll
#define fillchar(a,i) memset(a,i,sizeof(a))
#define rev(s) string(s.rbegin(),s.rend())
#define read(f) freopen(f, "r", stdin)
#define write(f) freopen(f, "w", stdout)
#define unq(v) unique(v.begin(),v.end(),v.end())
#define maxe(v) max_element(v.begin(),v.end())
#define mine(v) min_element(v.begin(),v.end())
#define rep(i,n) for(int i=0;i<n;i++)
#define per(i,n) for(int i=n-1;i>=0;i--)
#define fnd(v,val) find(v.begin(), v.end(),val)
#define cont(v,val) count (v.begin(),v.end(),val)
#define revrse(v) reverse(v.begin(),v.end())
#define replce(v,x,y) replace (v.begin(), v.end(), x, y)
#define remv(v,val) remove(v.begin(), v.end(),val)
#define acc(v) accumulate(v.begin(),v.end(), 0)
int gcd(int a,int b) {return b?gcd(b,a%b):a;}


struct node{
	int x;
	int y;
	double z;
	string ss;

};
typedef struct node yash;

bool my_fun(yash a,yash b){
    if(a.x<b.x)
        return 1;
    else if(a.x==b.x){
        return (a.y<b.y);
    }
    else
        return 0;
}
int main(){
	int t;
	cin>>t;
	for(int f=1;f<=t;f++){
		int l,m;
		cin>>l>>m;
		vector<vector<int> >grid(l,vector<int> (m));
		vector<int>raw(l);
		vector<int>cl(m);
		for(int i = 0;i < l;i++){
			int mx = 0;
			for(int j = 0;j < m;j++){
				cin>>grid[i][j];
				if(grid[i][j] > mx)
					mx = grid[i][j];
			}
			raw[i] = mx;
		}
		for(int j = 0;j < m;j++){
			int mx = 0;
			for(int i = 0;i < l;i++){
				if(grid[i][j] > mx)
					mx = grid[i][j];
			}
			cl[j] = mx;
		}
		bool flag = 0;
		for(int i = 0;i < l;i++){
			for(int j = 0;j < m;j++){
				if(grid[i][j] < raw[i] && grid[i][j] < cl[j])
					flag = 1;
				if(flag == 1)
					break;
			}
			if(flag == 1)
				break;
		}
		if(flag == 0)
			cout<<"Case #"<<f<<": YES"<<endl;
		else
			cout<<"Case #"<<f<<": NO"<<endl;
	}
	return 0;
}