#include <iostream>
#include <cstdio>
#include <cmath>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;
const double eps=1e-9;
int main(){
	//freopen("input.txt","r",stdin);
	//freopen("output.txt","w",stdout);
	int t;
	scanf("%d",&t);
	for(int cs=1;cs<=t;++cs){
		string s,u="";
		cin>>s;
		for(int i=0;i<s.size();++i){
			string a=s[i]+u;
			string b=u+s[i];
			if(a>b){
				u=a;
			}else{
				u=b;
			}
		}
		cout<<"Case #"<<cs<<": "<<u<<endl;
	}
	return 0;
}