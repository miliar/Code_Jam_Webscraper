#include <iostream>
#include <fstream>
#include <algorithm>
#include <cstdio>
#include <vector>
#include <string>
#include <cmath>
#include <queue>
#include <iomanip>
using namespace std;
int main(){
	long long t,te,i,j,k,n,x,ans;
	ifstream f1;
	ofstream f2;
	f1.open("input.txt");
	f2.open("output.txt");
	f1>>t;
	for(te=0;te<t;te++){
		f1>>n>>x;
		ans=0;
		long long arr[n];
		for(i=0;i<n;i++)f1>>arr[i];
		sort(arr,arr+n);
		for(i=n-1,j=0;i>=j;i--){
			if(i!=j&&(arr[i]+arr[j])<=x)j++;
			ans++;
		}
		f2<<"Case #"<<1+te<<": "<<ans<<"\n";
		cout<<"Case #"<<1+te<<": "<<ans<<"\n";
	}
	return 0;
}
