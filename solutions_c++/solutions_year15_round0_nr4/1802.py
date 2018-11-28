//============================================================================
// Name        : Contest.cpp
// Author      : Alireza
// Version     :
// Copyright   : Enjoy It!
// Description : Hello World in C++, Ansi-style
//============================================================================
#include <sys/resource.h>
#include <iostream>
#include <fstream>
#include <string>
#include <cstdio>
#include <cstring>
#include <queue>
#include <functional>

#define FOR(i,c,n) for(int i=(c);(i)<(n);++(i))
#define FR(i,n) FOR(i,0,n)
using namespace std;

int main() {
	freopen("/home/alireza/Downloads/D-small-attempt0.in","r",stdin);
	//freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int tcase;cin>>tcase;
	FR(cas,tcase){
		printf("Case #%d: ",cas+1);
		int x,r,c;
		cin>>x>>r>>c;
		if(r<c) swap(r,c);
		string s[]={"GABRIEL","RICHARD"};
		if(x==1) cout<<s[0]<<endl;
		if(x==2) cout<<s[(r*c)%2]<<endl;
		if(x==3){
			if(r==4){
				if(c==3)cout<<s[0]<<endl;
				else cout<<s[1]<<endl;
			}
			else if(r==3){
				if(c==1)cout<<s[1]<<endl;
				else cout<<s[0]<<endl;
			}else
				cout<<s[1]<<endl;
		}
		if(x==4){
			if(r==4){
				if(c>=3) cout<<s[0]<<endl;
				else cout<<s[1]<<endl;
			}
			else cout<<s[1]<<endl;
		}

	}
}
