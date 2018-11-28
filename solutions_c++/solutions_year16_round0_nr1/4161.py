#include<iostream>
#include<fstream>
#include<string>
#include<cstring>
#include<math.h>
#include<cassert>
#include<iomanip>
#include<algorithm>
#include<vector>
#include<map>
#include<queue>
#include<stack>
#include<set>
#include<cmath>
#include<cstdio>
#include<cstdlib>
#include<bitset>
#include<valarray>
#include<iterator>
#include<list>
#define ll long long
#define ull unsigned long long
#define mp make_pair
#define S second
#define F first
#define y1 LOL
#define pb push_back
#define len length
#define sz size
#define beg begin
const int inf=(int)1e9; 
const int mod=1e9+7;
using namespace std;
int n;
int a[11];
int main(){
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	//cout.tie(0);
	freopen("A-large.in","r",stdin);
	freopen("a.out","w",stdout);
	cin>>n;
	for(int i=1;i<=n;i++){
		int x;
		cin>>x;
		int cnt=0;
		for(int j=1;j<=1000;j++){
			ll h=x*j;
			while(h){
				int f=h%10;
				if(!a[f]){
					a[f]=1;
					cnt++;
				}
				h/=10;
			}
			if(cnt==10){
				cout<<"Case #"<<i<<": "<<x*j<<endl;
				break;
			}
			if(j==1000){
				cout<<"Case #"<<i<<": INSOMNIA"<<endl;
			}
		}
		for(int j=0;j<=9;j++){
			a[j]=0;
        }
    }
	return 0;
}