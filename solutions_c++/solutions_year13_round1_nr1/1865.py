#include <iostream>
#include <cstdio>
using namespace std;

int main() {
	int t;
    cin>>t;
    for(int i = 1; i<=t; i++){
        int sum = 0;
        int r,n,ret = 0;
        cin>>r>>n;
        while(sum<n){
            sum = sum + 2*r + 4*ret + 1;
            if(sum<=n)ret++;
        }
        printf("Case #%d: %d\n",i,ret);
    }
	return 0;
}