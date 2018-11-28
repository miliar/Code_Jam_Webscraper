									/*ba yade oo */
//Mehrdad AP

//#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <string>
#include <cstdio>
#include <string.h>
#include <algorithm>
#include <stdio.h>
#include <math.h>
#include <cstring>
#include <sstream>
#include <queue>
#include <vector>
#include <stack>
#include <set>
#include <map>
#include <time.h>

using namespace std;

#define absol(x) ((x)>(0) ? (x):(-1)*(x))
#define pow2(x) ((x)*(x))
#define EPS 1e-9
#define MAX 30000
#define MOD 1000000007
#define Left(x) (2*x)
#define Right(x) ((2*(x)+1)
#define mP make_pair
#define pB push_back

//#define inRange(x,y) (x>=0 && x<N && y>=0 && y<M)

typedef long long int LL;
typedef vector<int> vi;
typedef pair<int,int> pii;
typedef pair<int,pii> piii;

const double PI = 2.0*acos(0.0);
const int INF = 1000*1000*1000;
const int maxn=100009;

#define assert(x) { cerr  << #x << ": "<< (x) << endl;}
#define SP system("pause")

bool candid[20];

int main()
{

	int TC=0,tc;
	int g,x;
	cin >> tc;
	while (tc--){
		cin >> g;g--;
		memset(candid,false,sizeof candid);
		for (int i=0;i<4;i++)
			for (int j=0;j<4;j++){
				cin >>x;
				if (i==g)
					candid[x]=true;
			}

		int cnt=0,num;
		cin >> g;g--;
		for (int i=0;i<4;i++)
			for (int j=0;j<4;j++){
				cin >> x;
				if (i==g && candid[x]){
					cnt++;
					num=x;
				}
			}

		printf("Case #%d: ",++TC);
		if (cnt==1)
			cout << num << endl;
		else if (cnt==0)
			cout << "Volunteer cheated!"<<endl;
		else 
			cout << "Bad magician!"<<endl;


	}


	return 0;

}