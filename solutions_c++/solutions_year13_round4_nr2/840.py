//
//  main.cpp
//  GCJ_R2_B
//
//  Created by Ningchen Ying on 6/1/13.
//  Copyright (c) 2013 Ningchen Ying. All rights reserved.
//
#include <iostream>
#include <algorithm>
#include <cmath>
#include <vector>
#include <cstdlib>
#include <cstdio>
#include <string>
#include <cstring>
using namespace std;

long long n,p;

long long solve1(){
    long long l = 1 , r = 1<<(n);
	while (l < r) {
		long long m = (l+r+1)/2, res = 0, b = (m-1) ;
		for (int j = 1 ; j <= n ; j++){
			if (!b) res <<= 1;
			else {
                res *= 2, res += 1;
                --b, b/=2;
			}
		}
		if (res+1<=p) l = m;
		else r = m-1;
	}
	return l-1;
}
long long solve2(){
    long long l = 1 , r = 1<<(n);
	while (l < r) {
		long long m = (l+r+1)/2, res = 0, b = (1<<(n))-m;
		for (int j = 1 ; j <= n ; j++){
			if (!b) res <<= 1, res +=1;
			else {
                res *= 2;
                b-=1, b/=2;
			}
		}
		if (res+1<=p) l = m;
		else r = m-1;
	}
	return l-1;
}

int main(int argc, const char * argv[])
{
    freopen("/Users/YNingC/Documents/CodeForces/GCJ_R2_B/GCJ_R2_B/B-small-attempt3.in","r",stdin);
    freopen("/Users/YNingC/Documents/CodeForces/GCJ_R2_B/GCJ_R2_B/B-small-attempt3.out","w",stdout);
    int T;
    //cout<<(1<<0)<<endl;
    cin>>T;
    for(int ca=1;ca<=T;ca++){
        cin>>n>>p;
        printf("Case #%d: ",ca);
        cout<<solve1()<<" "<<solve2()<<endl;
    }
    return 0;
}
