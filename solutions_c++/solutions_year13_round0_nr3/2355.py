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
     long long int t,pos=0,sm1,sm2;
     long long int j,n,m;
     long long int grid[] = {1, 4, 9, 121, 484, 10201, 12321, 14641, 40804, 44944, 1002001, 1234321, 4008004, 100020001, 102030201, 104060401, 121242121, 123454321, 125686521, 400080004, 404090404, 10000200001, 10221412201, 12102420121, 12345654321, 40000800004, 1000002000001, 1002003002001, 1004006004001, 1020304030201, 1022325232201, 1024348434201, 1210024200121, 1212225222121, 1214428244121, 1232346432321, 1234567654321, 4000008000004, 4004009004004};
     cin>>t;
     for(int f=1;f<=t;f++){
        cin>>n>>m;
        pos = 39;
        if(n > grid[pos-1]){
			cout<<0<<endl;
            continue;
        }
        if(m > grid[pos-1])
			m = grid[pos-1];
            for(int i = 0;i < pos;i++){
				if(grid[i] >= n){
					sm1 = i;
                    break;
				}
            }
            for(int i = 0;i <pos;i++){
				if(grid[i] <= m)
					sm2 = i;
            }
            cout<<"Case #"<<f<<": "<<sm2-sm1+1<<endl;
     }
     return 0;
}