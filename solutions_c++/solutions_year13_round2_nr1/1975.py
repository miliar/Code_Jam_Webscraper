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

#define fillchar(a,i) memset(a,i,sizeof(a))
#define maxe(v) max_element(v.begin(),v.end())
#define mine(v) min_element(v.begin(),v.end())
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
yash cont(vector<long long> v,int pos,int a,int n){
	yash tmp;
	long long ww=a;
	int flag=0;
	int cnt=0;
	while(ww<=v[pos]){
			if((ww-1)==0){
					flag=1;
					cnt=n-pos;
					break;
			}
			ww+=ww-1;
			cnt++;
	}
	tmp.x=cnt;
	tmp.y=ww;
	return  tmp;
}
long long find(vector<long long> v,long long pos,long long a,long long n){
	long long ans=n;
	//cout<<a<<" "<<ans<<endl;
	yash tmp;
	if(pos>=n){
		return 0;
	}
	if(a>v[pos]){
		a+=v[pos];
		ans=min(ans,find(v,pos+1, a,n)+0);
	}
	else{
		 tmp=cont(v,pos,a,n);
	//	cout<<tmp.x<<endl;
		ans= min(ans,min(n-pos,find(v,pos+1, tmp.y+v[pos],n)+tmp.x));
	}
	return ans;
}
int main(){
	long long t;
	cin>>t;
	for(long long g=1;g<=t;g++){
		long long n,m,sm,cnt=0,mx,mn,a,p,wt;
		long long arr[200][200]={0};
		vector<long long> v;
		cin>>a>>n;
		wt=a;
		for(int i=0;i<n;i++){
			cin>>p;
			v.push_back(p);
		}
		sort(v.begin(),v.end());
		long long ans=0;
		int flag=0;
		ans=find(v,0, a,n);
		cout<<"Case #"<<g<<": "<<ans<<endl;
	}
	return 0;
}