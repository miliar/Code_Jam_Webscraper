#include<iostream>
#include<cstdio>
#include<string>
#include<vector>
#include<cstring>
#include<iomanip> 
#include<utility> 
#include<climits>
#include<climits>
#include<cmath>
#include<algorithm>


using namespace std;


#define LL long long int
#define sc1(x) scanf("%d", &x)
#define sc2(x, y) scanf("%d%d", &x, &y)
#define sc3(x, y, z) scanf("%d%d%d", &x, &y, &z)
#define pr1(x) printf("%d\n", x)
#define FOR(i, a, n) for(int i=a;i<n;i++)
#define pp pair<int, int>
#define pb push_back 

#define MAX 1000001
#define MOD 1000000007LL


string func(string &str, int n) {
	string result;

	result = str[0];
	FOR(i, 1, n) {
		if(str[i] >= result[0]) result = str[i] + result;
		else result = result + str[i];
	}

	return result;
}

int main() {

	int t;

	string str;

	sc1(t);
	FOR(index, 1, t+1) {
		cin>>str;

		cout<<"Case #"<<index<<": "<<func(str, str.size())<<endl;
	}
	return 0;
}













