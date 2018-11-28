#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <string>
#include <algorithm> 
#include <utility>
#include <stack>
#include <queue> 
#include <cmath>
#include <map>
#include <sstream>
#include <functional>
#include <numeric>

#define mp make_pair
#define pb push_back

using namespace std;

long long toint(string s) { istringstream in(s); long long x; in>>x; return x; }
template<class T> string tostring(T x) { ostringstream out; out<<x; return out.str();}
vector< vector<int> >pals;
bool isSquare(int n){
	int m = (int)(sqrt(n));
	return m*m==n;
}
bool isPal(int n){
	int m = n;
	int rev = 0;
	while(m>0){
		rev = rev*10 + m%10;
		m/=10;
	}
	return rev==n;
}
int dig(int n){
	int ret = 0;
	while(n>0){
		n/=10;
		ret++;
	}
	return ret;
}
int main(int argc, char *argv[]){
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    vector<int>sub;
    for(int i=1; i<10; i++)//1
    	sub.pb(i);
    pals.pb(sub);
    sub.clear();

    for(int i=1; i<=9; i++)//2
    	sub.pb(i*10+i);
    pals.pb(sub);
    sub.clear();

    for(int i=1; i<=9; i++){
    	for(int j=0; j<=9; j++){
    		sub.pb(i*100+j*10+i);
    	}
    }
    pals.pb(sub);/*
    for(int i=0; i<3; i++){
    	printf("%d:\n", i+1);
    	for(int j=0; j<pals[i].size(); j++)
    		printf("%d\n", pals[i][j]);
    	printf("\n\n");
    }*/
    int t;
    scanf("%d", &t);
    for(int tt=1; tt<=t; tt++){
    	printf("Case #%d: ", tt);
    	int a, b;
    	scanf("%d%d", &a, &b);
    	//printf("%d %d\n", dig(a)-1, dig(b)-1);
    	if(b==1000)b--;
    	int ret = 0;
    	for(int i=dig(a)-1; i<=dig(b)-1; i++){
    		for(int j=0; j<pals[i].size(); j++){
    			if(pals[i][j]>=a&&pals[i][j]<=b&&isSquare(pals[i][j])){
    				if(isPal((int)sqrt(pals[i][j]))){
    					ret++;
    					//printf("\n%d %d\n", pals[i][j], (int)sqrt(pals[i][j]));
    				}
    			}
    		}
    	}
    	printf("%d\n", ret);
    }
    return 0;
}