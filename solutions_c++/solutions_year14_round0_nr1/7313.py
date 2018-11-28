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
#include<stdio.h>
#include<climits>


using namespace std;

#define rep(i,a,b) for(int i=a;i<b;++i)
typedef long long ll;
#define s(n) cin>>n
#define p(n) cout<<n<<endl


int main(){


	int t;
	s(t);
	int caseCount =0;
	while(t--){
		++caseCount;
		int a;
		int matA[4][4];
		int b;
		int matB[4][4];

		s(a);
		rep(i,0,4){
			rep(j,0,4){
				s(matA[i][j]);
			}
		}


		s(b);
		rep(i,0,4){
			rep(j,0,4){
				s(matB[i][j]);
			}
		}

		int count = 0;
		int num = 0;

		/*
		   vector <int>hashMatrix(100,0);

		   rep(i,0,4){
		   hashMatrix[matA[a-1][i]]=1;
		   }


		   rep(j,0,4){
		   if(hashMatrix[matB[b-1][j]]==1){
		   ++count;
		   num = matB[b-1][j];
		   }
		   }
		   */


		rep(i,0,4){
			rep(j,0,4){
				if(matA[a-1][i]==matB[b-1][j]){
					++count;
					num = matA[a-1][i];
				}
			}
		}

		if(count==1){
			printf("Case #%d: %d\n",caseCount,num);
		}else if(count>1){
			printf("Case #%d: Bad magician!\n",caseCount);
		}else{
			printf("Case #%d: Volunteer cheated!\n",caseCount);
		}


	}




	return 0;
}
