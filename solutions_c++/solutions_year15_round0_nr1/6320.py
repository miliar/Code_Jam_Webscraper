/*
 Author : Komal Nagar
 Contest Name : Qualification Round 2015
 Problem Name : standing oviation
 */
#include <iostream>
#include <vector>
#include <set>
#include <queue>
#include <deque>
#include <map>
#include <stack>
#include <string>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
using namespace std;

#define maxN 100001
#define INF 99999999
#define LL long long
#define mod 1000000007

int main(int argc, char const *argv[]) {
	int t,len,available,need;
	string inp;

	cin>>t;
	for(int x=1;x<=t;x++){
		cin>>len>>inp;
		available = 0; need = 0;

		for(int i=0;i<inp.size();i++){
			if(inp[i] > '0' && i > available){
				need += (i - available);
				available += (i - available);
			}
			available += (inp[i]-'0');
			//cout<<"i = "<<i<<" need = "<<need<<" available = "<<available<<endl;
		}
		//cout<<"Case #"<<x<<": "<<need<<endl;
		printf("Case #%d: %d\n",x,need);

	}

	return 0;
}
