#include <iostream>
#include <stdio.h>
#include <math.h>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <iomanip>
#include <cstring>
#include <fstream>
#include <limits.h>
#define mod 1000000007
using namespace std;

struct node {

};

long long A[1000005],B[1000005],C[1000005];

int main()
{
	freopen("A-small-attempt1.in","r",stdin);
	freopen("output.txt","w",stdout);
	long long i,j,k,l,m,n,x,y,z,a,b,c,d,t;
	string str;
	struct node s;
	cin>>t;
	for(j = 0; j < t; j++){
		cin>>n>>str;
		long long cnt = 0, fr = 0;
		cnt = str[0]-'0';
		for(i = 1; i < str.length(); i++){
			if(cnt < i && str[i] != '0'){
				fr+=i-cnt;
				cnt+=fr;
			}
			cnt += str[i]-'0';
			
		}
		cout<<"Case #"<<j+1<<": "<<fr<<endl;
	}
	return 0;
}
