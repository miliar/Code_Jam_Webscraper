#include<iostream>
#include<vector>
#include<algorithm>
#include<sstream>
#include<string>
#include<set>
#include<stdio.h>

using namespace std;

string s,r;

vector<long long>v,pal;

int main()
{
	freopen("sam.txt","r",stdin);
	freopen("out.txt","w",stdout);
	long long i,sum,num,a,b;
	int t,p=0;
	for(i=1;i<=10000000;i++){
		stringstream ss (stringstream::in | stringstream::out);
		ss<<(i);
		s=ss.str();
		r=s;
		reverse(s.begin(),s.end());
		if(s==r)v.push_back(i);
	}
	for(i=0;i<v.size();i++){
		num=v[i]*v[i];
		stringstream ss (stringstream::in | stringstream::out);
		ss<<num;
		s=ss.str();
		r=s;
		reverse(s.begin(),s.end());
		if(s==r)pal.push_back(num);
	}
	cin>>t;
	while(t--){
	    cin>>a>>b;
	    sum=0;
	    for(i=0;i<pal.size();i++){
	        if(pal[i]>=a && pal[i]<=b)++sum;
	    }
	    printf("Case #%d: %lld\n",++p,sum);
	}
	return 0;
}
