/*
 * test.cpp
 *
 *  Created on: Sep 26, 2016
 *      Author: SCE15-0683
 */

#include<iostream>
#include<cstdio>
#include<vector>
#include<algorithm>
#include<queue>
#include<string>
#include<map>
#include<cmath>
#include<bitset>
#include<set>
#include<iomanip>
#include<fstream>
#include<bitset>
#include<cstring>
#include<cstdlib>
#include<complex>
#include<list>
#include<sstream>

using namespace std;

typedef pair<int,int> ii;
typedef pair<int,long long> il;
typedef pair<long long,long long> ll;
typedef pair<ll,int> lli;
typedef pair<long long,int> li;
typedef pair<double,double> dd;
typedef pair<ii,int> iii;
long long mod = 1000000007LL;
long long base = 37;
long long large = 1000000000000000000LL;

int main(){
	int t;
	cin>>t;
	int test=0;
	ofstream out;
	out.open("result.txt");
	while(t--){
		test++;
		out<<"Case #"<<test<<": ";
		string s;
		cin>>s;
		int k;
		cin>>k;
		int n = (int)s.length();
		int cnt = 0;
		for(int i=0;i+k<=n;i++){
			if(s[i]=='-'){
				cnt++;
				for(int j=0;j<k;j++){
					if(s[i+j]=='-'){
						s[i+j]='+';
					}else{
						s[i+j]='-';
					}
				}
			}
		}

		bool flag = true;
		for(int i=0;i<n;i++){
			if(s[i]=='-') flag=false;
		}
		if(flag){
			out<<cnt<<endl;
		}else{
			out<<"IMPOSSIBLE"<<endl;
		}
		cout<<cnt<<endl;
	}

	out.close();
	return 0;
}
