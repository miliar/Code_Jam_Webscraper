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


int main()
{

	int tc,TC=0;
	int N;
	string s,t;
	cin >> tc;
	
	while (tc--){
		cin >> N;
		cin >> s >> t;
		int ans=0;
		bool can=true;
		
		int i=0,j=0;
		while (i<s.size() && j<t.size()){
			char cur=s[i];
			if (t[j]!=cur){
				can=false;
				
				break;

			}
			int cnt1=0,cnt2=0;
			while ((i<s.size() && s[i]==s[i+1]) || (i==(int)s.size()-1)){
				i++;
				cnt1++;
			}
			
			while ((j<t.size() && t[j]==t[j+1]) || (j==(int)t.size()-1)){
				j++;
				cnt2++;
			}

			ans+=absol((cnt2-cnt1));

			i++,j++;
		}
		
		if (i<s.size() || j<t.size())
			can=false;


		printf ("Case #%d: ",++TC);
		if (!can)
			cout << "Fegla Won" << endl;
		else
			cout << ans << endl;



	}
	
	return 0;

}