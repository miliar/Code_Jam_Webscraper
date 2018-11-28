#include <cstdio>
#include <iostream>
#include <cmath>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;
 
inline void fastRead_int(int &x) {
	register int c = getchar_unlocked();
	x = 0;
	for(; (c<48 || c>57); c = getchar_unlocked());
	for(; c>47 && c<58 ; c = getchar_unlocked()) {
	x = (x<<1) + (x<<3) + c - 48;}};
inline void fastRead_intL(long int &x) {
	register int c = getchar_unlocked();
	x = 0;
	for(; (c<48 || c>57); c = getchar_unlocked());
	for(; c>47 && c<58 ; c = getchar_unlocked()) {
	x = (x<<1) + (x<<3) + c - 48;}}

int main() {
	int tcases,smax,totalpeople,friends;
	register int c;
	fastRead_int(tcases);
	for(int i =1; i <= tcases;i++){
	    fastRead_int(smax);
	    totalpeople = 0;
	    friends = 0;
	    for(int j=0;j<=smax;j++){
	        c = (int)(getchar_unlocked()- 48);
	        if(c>0){ if(totalpeople >= j){ totalpeople+= c;}
	       			 else{friends+=(j-totalpeople); totalpeople+=(j-totalpeople); totalpeople+=c;}}
	    }
	    printf("Case #%d: %d\n",i,friends);
	}
	return 0;
}