#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
#include <queue>
#include <deque>
#include <bitset>
#include <iterator>
#include <list>
#include <stack>
#include <map>
#include <set>
#include <functional>
#include <numeric>
#include <utility>
#include <limits>
#include <time.h>
#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#define LL long long
#define PB push_back
#define MP make_pair
#define F first
#define S second
#define sc(x) scanf("%d", &x)
#define scl(x) scanf("%lld", &x)
#define M 1000000007
#define MAXN 112345
using namespace std;

int a[10];

void calc(int x){
    stringstream ss;
    string str;
    ss << x;
    str = ss.str();
    for(int i=0;i<str.length();i++){
        a[str[i] - '0'] = 1;
    }
}

bool filled(){
    for(int i=0;i<10;i++){
        if(a[i] == 0)
            return 0;
    }
    return 1;
}

int main(){
	int n, T, t,  i, j, flag;
    freopen("A-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
	cin>>T;
	for(t=1;t<=T;t++){
		cin>>n;
        flag = 0;
        for(i=0;i<10;i++){
            a[i] = 0;
        }
		for(i=1;i<=72;i++){
            j = n * i;
            calc(j);
            if(filled()){
                 flag = 1;
                 break;
            }
		}
        cout<<"Case #"<<t<<": ";
        if(flag == 1){
             cout<<j<<endl;
        }
        else{
            cout<<"INSOMNIA"<<endl;
        }
	}
}

