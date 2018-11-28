#include <iostream>
#include <iomanip>
#include <sstream>
#include <utility>
#include <fstream>
#include <string>
#include <vector>
#include <cmath>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <assert.h>
using namespace std;

int main()
{
    //freopen("c:/loadfiles/codejam/input.txt", "r", stdin);
    freopen("c:/loadfiles/downloads/B-small-attempt0.in","r",stdin);
	freopen("c:/loadfiles/codejam/outputCPP.txt", "w", stdout);
    int trials;
    cin >> trials;
    for (int trial = 1; trial <= trials; ++trial) {
		long long a,b,k;
		printf("Case #%d: ", trial);
		cin>>a>>b>>k;
		long long count=0;
		for(long long i=0;i<a;i++){
			for(long long j=0;j<b;j++){
				long long v=i&j;
				if(v<k){
					count++;
				}
			}
			
		}
		cout<<count;
        printf("\n");
	}
    
    return 0;
}
