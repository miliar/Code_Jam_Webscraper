#include <iostream>
#include <iomanip>
#include <algorithm>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sstream>
#include <math.h>
#include <limits.h>
#include <time.h>
#include <vector>
#include <utility>
#include <list>
#include <stack>
#include <queue>
#include <map>
#include <set>
using namespace std;

#define LIM_UI UINT_MAX
#define LIM_UL ULLONG_MAX
//iterations
#define repi(i,a,b) for(int i=a;i<=b;++i)
#define repd(i,a,b) for(int i=a;i>=b;--i)

int first[4][4],second[4][4];

int main(){
	ios::sync_with_stdio(false);
	int t;
	int ra,rb;
	cin>>t;
	int c=1;
	while(c<=t){
		cin>>ra;--ra;
		repi(i,0,3)
			repi(j,0,3)
				cin>>first[i][j];

		cin>>rb;--rb;
		repi(i,0,3)
			repi(j,0,3)
				cin>>second[i][j];

		int count=0;
		int same=-1;
		repi(i,0,3){
			repi(j,0,3){
				if(first[ra][i]==second[rb][j]){
					++count;
					same = first[ra][i];
				}
			}
		}

		if(count==0){
			cout<<"Case #"<<c<<": Volunteer cheated!\n";
		}else if(count==1){
			cout<<"Case #"<<c<<": "<<same<<"\n";
		}else{
			cout<<"Case #"<<c<<": Bad magician!\n";
		}
		++c;
	}
	return 0;
}