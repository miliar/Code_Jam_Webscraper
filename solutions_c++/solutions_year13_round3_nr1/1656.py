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
int check(string s2,int n){
	int l=s2.size();
	int cnt=0;
	int flag=0;
	for(int i=0;i<l;i++){
	//	cout<<s2[i];
		if(s2[i]!='a' && s2[i]!='e' && s2[i] !='i' && s2[i] !='o' && s2[i] !='u'){
			flag=1;
			cnt++;
	//		cout<<cnt<<endl;
		}
		else{
			flag=0;
			cnt=0;
		}
		if(cnt>=n)
			return 1;
	}
	if(cnt>=n)
			return 1;
	return 0;
}
int main(){
	long long t;
	cin>>t;
	for(long long g=1;g<=t;g++){
		long long n,m,sm,cnt=0,mx,mn;
		string s;
		string s2;
		vector<long long> v;
		cin>>s>>n;
		int l=s.size();
		int flag=0;
		//flag=check("quartz",n);
		for(int i=0;i<l;i++){
			for(int j=1;j<=l-i;j++){
				flag=0;
				s2=s.substr (i,j);
				
				flag=check(s2,n);
		//		cout<<s2<<" "<<flag<<endl;
				if(flag)
					cnt++;
			}
		}
		cout<<"Case #"<<g<<": "<<cnt<<endl;
	}
	return 0;
}