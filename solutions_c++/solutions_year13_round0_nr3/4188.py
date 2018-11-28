#include <iostream>
#include <algorithm>
#include <cmath>
#include <math.h>
#include <stdio.h>
#include <cstring>
#include <vector>
#include <map>
#include <string.h>
#include <set>
#include <sstream>
#include <iomanip>


using namespace std;
#define ll long long int
#define pb push_back

int main(){
	int t, cs = 0;ll a, b;
	cin >> t;
	ll ar[] = {1L,4L,9L,121L,484L,10201L,12321L,14641L,40804L,44944L,1002001L,1234321L,4008004L,100020001L,102030201L,104060401L,121242121L,123454321L,125686521L,400080004L,404090404L,10000200001L,10221412201L,12102420121L,12345654321L,40000800004L,1000002000001L,1002003002001L,1004006004001L,1020304030201L,1022325232201L,1024348434201L,1210024200121L,1212225222121L,1214428244121L,1232346432321L,1234567654321L,4000008000004L,4004009004004L};
	while(t--){cs++;int c = 0;
		cin >> a >> b;
		for(int i = 0; i < 39; i++){
			if(ar[i] >= a && ar[i] <= b)c++;
			
		}
		cout << "Case #" << cs<< ": " << c << endl;
	}
	return 0;
}

