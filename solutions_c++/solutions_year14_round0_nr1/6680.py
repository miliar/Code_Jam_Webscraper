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
#define all(Con) Con.begin(),Con.end()

using namespace std;
int tests;
double C,F,X;
int a[20][20];
int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	//scanf("%d\n",&tests);
	cin>>tests;
	// int n = 4;
	int row1 , row2;
	for(int counter=1;counter<=tests;counter++){
		vector<int> ans;
		set<int> S;

		cin>>row1;
		for(int i=1;i<=4;i++)
			for(int j=1;j<=4;j++){
				cin>>a[i][j];
				if(row1 == i)
					S.insert(a[i][j]);
			}

		cin>>row2;
		for(int i=1;i<=4;i++)
			for(int j=1;j<=4;j++){
				cin>>a[i][j];
				if(row2 == i){
					if(S.count(a[i][j]))
						ans.push_back(a[i][j]);
				}
			}


		printf("Case #%d: ",counter);
		if(ans.size()==1) printf("%d",ans.back());
		else if(ans.size()>1) printf("Bad magician!");
		else if(ans.size()==0) printf("Volunteer cheated!");
			
		printf("\n");
	}

return 0;
}
