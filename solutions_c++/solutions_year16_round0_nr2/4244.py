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
int main(){
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	//cout.tie(0);
	freopen("B-large.in","r",stdin);
	freopen("b.out","w",stdout);
	int n;
	cin>>n;
	for(int i=1;i<=n;i++){
		string s;
		cin>>s;
		bool z=0;
		int sum=0;
		if(s[0]=='-'){
			sum--;
		}
		for(int j=0;j<s.len();j++){
			if(s[j]=='-'&&z==0){
				sum+=2;
				z=1;
			}
			if(s[j]=='+'){
				z=0;
			}
		}
		cout<<"Case #"<<i<<": "<<sum<<endl;
	}
	return 0;
}