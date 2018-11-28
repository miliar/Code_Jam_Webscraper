#include<iostream>
#include<list>
#include<cstdio>
#include<cmath>
#include<numeric>
#include<utility>
#include<list>
#include<set>
#include<map>
#include<bitset>
#include<vector>
#include<algorithm>
#include<bitset>
#include <deque>
#include<queue>
#include<limits>
#include<string>
#include<cstring>
#include<cctype>
#include<iomanip>
#include<sstream>
#include<fstream>

using namespace std;

typedef unsigned long long int ull;
typedef unsigned long int ul;
typedef long long int ll;
typedef long int li;
typedef unsigned int ui;

int main(){
	int T;
	cin >> T;

	for(int t = 1; t <= T; t++){
          int a, b, k, count = 0;
          cin >> a >> b >> k;
          for(int i = 0; i < a; i++)
            for(int j = 0; j < b; j++)
              if( (i & j) < k){ 
                // cout << "i = " << i << " j = " << j << " and = " << (i&j) << endl; 
                count++; 
              }

          cout << "Case #" << t << ": " << count << endl;
	}
	return 0;
}
