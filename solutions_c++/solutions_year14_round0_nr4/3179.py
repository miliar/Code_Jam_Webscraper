#include <iostream>
#include <algorithm>
#include <cmath>
#include <time.h>
#include <stdlib.h>
#include <string>
#include <string.h>
#include <queue>
#include <utility>
#include <vector>
#include <time.h>
#include <stdio.h>
#include <list>
#include <limits> // for numeric_limits
#include <set>
#include <iterator>
#include <memory.h>

using namespace std;

#define ff first
#define ss second
#define pb push_back
#define mp make_pair
#define var(a,b)  __typeof(b) a = b
#define rep(i,n)  for(int i = 0;(i) < (n);  ++i)
#define rept(i,a,b) for(var(i,a); i < (b); ++i)
#define tr(v,it)  for(var(it,v.begin());it!=v.end();++it)
#define fill(a,val) memset(a,val,sizeof(a))
#define gi(n) scanf("%d",&n);
#define all(v) v.begin(),v.end()
#define max(a,b) a>b?a:b
#define min(a,b) a>b?b:a
#define MOD 1000000007
#define INF 99999999
#define a_max 100100
#define ll long long int
#define debug_lld(a) printf("Debug here %lld\n",a);

typedef pair<ll,ll> pll;
typedef pair<int,int > pii;
typedef pair<ll,pii>plp;


int binSearch(vector<double> input, double what) {
  
  int temp_mid = 0;
  int low = 0;
  int high = input.size() - 1;
  int mid;
  while (low <= high) {
    mid = (low + high) / 2;
    if (input[mid] > what){
    	temp_mid = mid;
        high = mid - 1;
    }
    else if (input[mid] < what)
      low = mid + 1;
  	if(low==high) break;
  }

  if(input[low]>what)
  	temp_mid=low;
  return temp_mid; // indicate not found 
}



int main()
{
	int t;
	scanf("%d",&t);
	for(int i=0;i<t;i++)
	{
		int n;
		scanf("%d",&n);

		std::vector<double> g;
		std::vector<double> k;

		std::vector<double> g_d;
		std::vector<double> k_d;


		
		int score=0;
		int score_d=0;
		double temp;

		for(int j = 0; j<n; j++){
			scanf("%lf",&temp);
			g.push_back(temp);
			// g_d.push_back(temp);
		}

		for(int j = 0; j<n; j++){
			scanf("%lf",&temp);
			k.push_back(temp);
			// k_d.push_back(temp);
		}

		std::sort(g.begin(),g.end());
		std::sort(k.begin(),k.end());

		g_d = g;
		k_d = k;

		// printf("%d %d\n",g_d.size(), k_d.size());


		while(g_d.size() > 0){
			// printf("Here\n");
			if(g_d[g_d.size()-1] < k_d[k_d.size()-1]){
				g_d.erase(g_d.begin());
				k_d.erase(k_d.begin() + k_d.size()-1);
			}
			else{
				int point = binSearch(g_d,k_d[0]);
				score_d++;
				g_d.erase(g_d.begin()+point);
				k_d.erase(k_d.begin());
			}
		}

		// printf("%d\n", score_d);

		for(int j = 0; j<n; j++){
			if(g[j] < k[k.size()-1]){
				int point = binSearch(k,g[j]);
				k.erase(k.begin()+point);

			}
			else
				break;
		}

		printf("Case #%d: %d %d\n",i+1, score_d, (int)(k.size()));


	}
	return 0;
}

