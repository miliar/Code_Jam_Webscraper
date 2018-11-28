#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <fstream>
#include <functional>
#include <iomanip>
#include <iostream>
#include <limits>
#include <list>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <stack>
#include <queue>
#include <utility>
#include <vector>
#include <cstdio>
using namespace std;

typedef long long ll;
typedef pair<int,int> ii;
typedef vector<ii> vii;
typedef vector<int> vi;
#define MSG(a) cout << #a << " = " << a << endl;

int main(){
	
	int t;
	scanf("%d",&t);
	int vs[17];
	
	int tcase = 1;
	while(t--){
		memset(vs,0,sizeof(vs));
		int p,k,temp;
		scanf("%d",&p);		
		for(int i = 0; i < 4; i++){
				for(int j = 0; j < 4; j++){
						scanf("%d",&temp);
						if(i == p-1)vs[temp]++;
					}
		}
		scanf("%d",&k);
		for(int i = 0; i < 4; i++){
				for(int j = 0; j < 4; j++){
						scanf("%d",&temp);
						if(i == k-1)vs[temp]++;
					}
		}
		int ans = 0;
		int pos = -1;
		for(int i = 0; i < 17; i++){
			if(vs[i] > 1){ans++;pos = i;}
		}		
		if(ans == 0) printf("Case #%d: %s\n",tcase++,"Volunteer cheated!");
		else if(ans > 1)printf("Case #%d: %s\n",tcase++,"Bad magician!");
		else{
			printf("Case #%d: %d\n",tcase++,pos);
		}
	}	


return 0;
}
