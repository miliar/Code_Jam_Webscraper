#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <cstring>
#include <cassert>
#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <map>
#include <set>
#include <sstream>
#include <numeric>
#include <bitset>
#define REP(i, a, b) for ( int i = int(a); i <= int(b); i++ )
#define pb push_back
#define for_each(it, X) for (__typeof((X).begin()) it = (X).begin(); it != (X).end(); it++)
#define DFS_WHITE -1
#define DFS_BLACK 1
#define MAXN 1000
#define EPS 1E-7
using namespace std;

int T, N;

int main()
{
    scanf("%d", &T);
    REP(t, 1, T) {
    	scanf("%d", &N);
    	vector<double> Na(N), Ke(N);
    	REP(i, 0, N-1) {
    		scanf("%lf", &Na[i]);
    	}
    	REP(i, 0, N-1) {
    		scanf("%lf", &Ke[i]);
    	}

    	sort(Na.begin(), Na.end());
    	sort(Ke.begin(), Ke.end());

    	printf("Case #%d: ", t);
    	
    	if(Na[0] > Ke[N-1]) {
    		//Naomi's smallest option is greater that Ken's largest - Naomi will score N matter what
    		printf("%d %d\n", N, N);
    	} else if(Na[N-1] < Ke[0]) {
    		//Naomi's largest option is smaller that Ken's smallest - Naomi will score zero matter what
    		printf("0 0\n");
    	} else {
    		//Naomi will use her smallest option and deceit Ken to play his largest item
    		vector<double> Ke_dct, Ke_opt;
    		Ke_dct.assign(Ke.begin(), Ke.end());
    		Ke_opt.assign(Ke.begin(), Ke.end());

    		int Na_dct = 0, Na_opt = 0;
    		double Na_ch, Ke_ch_largest, Ke_ch_smallest;

    		//Simulating Optimal Play
    		REP(i, 0, N-1) {		
    			Na_ch = Na[i];
    			vector<double>::iterator it = upper_bound(Ke_opt.begin(), Ke_opt.end(), Na_ch);    			
    			if(it == Ke_opt.end()) {
    				Na_opt = Ke_opt.size();
    				break;
    			}
    			Ke_opt.erase(it, it+1);    			
    		}

    		//Simulating Deceitful Play
    		while(true) {
    			if(Na.size() == 0) break;    			
    			Na_ch = Na[0];
    			Ke_ch_largest = Ke_dct[ (Ke_dct.size() - 1) ];
    			Ke_ch_smallest = Ke_dct[0];    			
    			Na.erase(Na.begin(), Na.begin()+1);
    			if(Na_ch < Ke_ch_smallest) {
    				//Deceitful Play    				
    				Ke_dct.erase(Ke_dct.begin() + (Ke_dct.size() - 1));
    			} else {
    				Ke_dct.erase(Ke_dct.begin(), Ke_dct.begin()+1);
    				Na_dct++;
    			}    			
    		}
    		printf("%d %d\n", Na_dct, Na_opt);
    	}
    }
    return 0;
}
