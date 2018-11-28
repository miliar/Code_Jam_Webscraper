#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include<string.h>
#define tr(c,it) for(typeof(c.begin()) it=c.begin();it!=c.end();++it)
#define all(c) c.begin(),c.end()
#define mod 1000000007
#define itor(c) typeof(c.begin())
#define ll long long
#define vi vector<int>
#define vs vector<string>
#define si set<int>
#define msi multiset<int>
#define sp set<pair<int,int> >
#define vp vector<pair<int,int> >
#define pb push_back
#define mp make_pair

using namespace std;

int main()
{
ios::sync_with_stdio(false);
int i,j,k,l,a,b,c,d,t,flag=0,n,test;
cin>>t;
for(test=1;test<=t;test++){
	c=0;
	cin>>a;
	int arr[4][4];
	for(i=0;i<4;i++){
		for(j=0;j<4;j++){
			cin>>arr[i][j];
			
		}
	}
	int arr1[4][4];
	cin>>b;
	for(i=0;i<4;i++){
		for(j=0;j<4;j++){
			cin>>arr1[i][j];
			
		}
	}
	for(i=0;i<4;i++){
		for(j=0;j<4;j++){
		if(arr[a-1][i]==arr1[b-1][j]){
			c++;
			d=arr[a-1][i];
		}	
			
			
		}
		
	}
	if(c==0){
		cout<<"Case #"<<test<<": Volunteer cheated!"<<endl;
	}
	if(c==1){
		cout<<"Case #"<<test<<": "<<d<<endl;
	}
	if(c>1){
		cout<<"Case #"<<test<<": Bad magician!"<<endl;
	}
}


    return 0;
}