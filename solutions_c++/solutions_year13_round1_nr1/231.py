#include <string>
#include <vector>
#include <map>
#include <utility>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <queue>
#include <stack>
#include <set>
#include <sstream>
#include <algorithm>
#include <iostream>
#include <iomanip>
#include <stdio.h>
#include <time.h>
using namespace std;
long long R,t;
long long pan(long long n){
	long long a=n+R+1;
	long long b=(n-R)/2+1;
	long double p=t;
	if(a<=p/b) return(1);
	return(0);
}
long long bin(){
	long long l,r,mid;
	l=R;r=t;
	while(l<r){
		mid=(l+r+1)/2;
		if(pan(mid)) l=mid;
		else r=mid-1;
	}
	if((l-R)%2==1) l--;
	cout<<(l-R)/2+1<<endl;
}
int main(){
    freopen("A-large.in","r",stdin);
    freopen("a.out","w",stdout);
    long long T,i;
    cin>>T;
    for(i=1;i<=T;i++){
		printf("Case #%d: ",i);
		cin>>R>>t;
		bin();
	}
}
