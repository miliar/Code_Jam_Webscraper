#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string.h>
using namespace std;
int Hash[20];
int main(){
	int tt ,tcas = 1;
	cin>>tt;
	for(tcas = 1; tcas<=tt; tcas++){
		memset(Hash,0,sizeof(Hash));
		int r1,r2,i,j,val;
		cin>>r1;
		r1--;
		for (i = 0;i<4;i++)
			for (j = 0;j<4;j++){
				cin>>val;
				if (i==r1) Hash[val] = 1;
			}
		cin>>r2;
		r2--;
		int ans = 0,cnt = 0;
		for (i = 0;i<4;i++)
			for (j = 0;j<4;j++){
				cin>>val;
				if (i==r2){
					if (Hash[val]){
						ans = val;
						cnt++;
					}
				}
			}
		printf("Case #%d: ", tcas);
		if (cnt==0) cout<<"Volunteer cheated!"<<endl;
		else if (cnt==1) cout<<ans<<endl;
		else cout<<"Bad magician!"<<endl;
	}
}
