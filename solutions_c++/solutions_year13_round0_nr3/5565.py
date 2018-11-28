#include<stdio.h>
#include<vector>
#include <iostream>
#include <algorithm>
#include <vector>
#include<math.h>
using namespace std;
int main(){
	int i,T;
	scanf("%d",&T);
	int fairsquares[]={0,1,4,9,121,484,10201,12321,40804,44944,1002001,1234321,4008004,100020001,102030201,104060401,121242121,123454321,125686521};
	vector<int> v(fairsquares,fairsquares+17);
	vector<int>::iterator low,up;
	int A,B;
	for(i=1;i<=T;i++){
		scanf("%d%d",&A,&B);
		low=std::lower_bound(v.begin(),v.end(),A);
		up=std::lower_bound(v.begin(),v.end(),B);
		if(*up==B)
			up++;
		printf("Case #%d: %d\n",i,up-low);
	}
	return 0;
}