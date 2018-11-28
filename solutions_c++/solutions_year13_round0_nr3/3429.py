/*************************************************************************
> File Name: C.cpp
> Author: myf
> Mail: 374684987@qq.com 
> Created Time: Sat 13 Apr 2013 23:52:06 CST
************************************************************************/

#include <fstream>
//#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <cstdlib>
#include <cctype>
#include <queue>
#include <string>
#include <bitset>
#include <vector>
#include <utility>
#include <map>
#include <set>
#include <string.h>
#include <iomanip>
#include <stdlib.h>
#include <stdio.h>


using namespace std;

ifstream cin("1.in");
ofstream cout("1.out");

bool Check(int p){
	int q=0,x=p;
	while(x>0){
		q=q*10+x%10;
		x/=10;
	}
	return (p==q);
}

int Calc(int l,int r){
	int tot=0;
	int a=sqrt(l),b=sqrt(r);
	if (a*a<l) a++;
	for(int i=a;i!=b+1;i++) tot+=Check(i)&&Check(i*i);
	return tot;
}

int main(){
	int t,l,r;
	cin>>t;
	for(int q=1;q!=t+1;q++){
		cin>>l>>r;
		cout<<"Case #"<<q<<": "<<Calc(l,r)<<endl;
	}
	return 0;
}
