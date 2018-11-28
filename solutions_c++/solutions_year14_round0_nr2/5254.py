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
int i,j,k,l,a,b,c,t,flag=0,n,test;
cin>>t;
for(test=1;test<=t;test++){
	double arr[100000],arr1[100000];
	double c,f,x,d;
	j=2.000000;
	cin>>c>>f>>x;
	arr[0]=c/j;
   arr1[0]=x/j;	
   d=j+f;
	for(i=1;i<100000;i++){
   	arr[i]=arr[i-1]+c/d;
   	arr1[i]=arr[i-1]+x/d;
   	d=d+f;
 
 
 
	}
	sort(arr1,arr1+100000);
 
	cout<<setprecision(20)<<"Case #"<<test<<": "<<arr1[0]<<endl;
	//for(i=0;i<10;i++){
	//	cout<<arr[i]<<" ";
	//}
 
//	for(i=0;i<80;i++){
//		cout<<arr1[i]<<endl;
//	}
 
}
    return 0;
}