//Bismillahir Rahmanir Rahim
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <string>
#include <vector>
#include <queue>
#include <map>
#include <algorithm>
#include <set>
#include <sstream>
#include <stack>
using namespace std ;
#define MAXN
#define FOR(i,a,b) for(int i=(int) a ; i<=(int)b;i++)

int main(int argc, char **argv){
	#ifdef unlucky_13
		freopen("//home/mazharul//Documents//A-small-attempt0.bin","r",stdin) ;
		freopen("//home/mazharul//Documents//out1.txt","w",stdout) ;
	#endif
	ios_base::sync_with_stdio(false) ;
	int tc ,r,val,num,ct;
	bool flag[20] ;
	cin>>tc ;
	ct = 1 ;
	while(tc--){
		memset(flag,0,sizeof(flag)) ;
		cin>>r ;
		FOR(i,1,4){
			FOR(j,0,3){
				cin>>val ;
				if(i==r){
					flag[val] = 1 ;
				}
			}
		}
		
		int res = 0 ;
		cin>>r ;
		FOR(i,1,4){
			FOR(j,0,3){
				cin>>val ;
				if(i==r){
					if(flag[val]) {
						res++ ;
						num = val ;
					}
				}
			}
		}
		
		cout<<"Case #"<<ct++<<": " ;
		if(res==1) cout<<num<<"\n" ;
		else if(res==0) cout<<"Volunteer cheated!\n" ;
		else cout<<"Bad magician!\n" ;
	}
	
	return 0;
}

