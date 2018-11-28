#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <cassert>
#include <algorithm>
#include <vector>
#include <deque>
#include <string>
#include <set>
#include <map>


using namespace std;

deque<double> ken;
deque<double> naomi;

deque<double> ken_c;
deque<double> naomi_c;

void copy_arrays(int n) {
    ken_c.resize(n);
    naomi_c.resize(n);
    
    copy(ken.begin(), ken.end(), ken_c.begin());
    copy(naomi.begin(), naomi.end(), naomi_c.begin());
}

int war_answer(int n) {
    // Solution for normal "War"
    copy_arrays(n);
    
    /*
    for (int i=0; i<n; i++) {
        printf("%lf %lf\n", ken_c[i], naomi_c[i]);
    }
    */
    
    int sol = 0;
    int m = n;
    while (m>0) {
        
        /*
        printf("\nNaomi:\t");
        for (int i=0; i<m; ++i) {
            printf("%lf ", naomi_c[i]);
        }
        printf("\nKen:\t");
        for (int i=0; i<m; ++i) {
            printf("%lf ", ken_c[i]);
        }
        printf("\n");
        */
        
        double a = naomi_c[0];
        naomi_c.pop_front();
        
        bool ken_wins = 0;
        for (deque<double>::iterator i=ken_c.begin(); i!=ken_c.end(); i++) {
            if ( (*i) > a ) {
                ken_wins = 1;
                ken_c.erase(i);
                break;
            }
        }
        if (!ken_wins) {
            ken_c.pop_front();
            sol++;
        }
        
        m--;
    }
    
    return sol;
}


int deceitful_war_answer(int n) {
    // Solution for normal "War"
    copy_arrays(n);
    
    int m = n;
    int sol = 0;
    
    while (m>0) {
        
        if ( naomi_c[0] < ken_c[0] ) {
            // Move A
            naomi_c.pop_front();
            ken_c.pop_back();
        }
        else {
            // Move B
            naomi_c.pop_front();
            ken_c.pop_front();
            sol++;
        }
        
        m--;
    }
    
    return sol;
}

void solve() {
	int n;
	scanf("%d", &n);
	
	ken.clear();
	naomi.clear();
	
	for (int i=0; i<n; ++i) {
	    double x;
	    scanf("%lf", &x);
	    naomi.push_back(x);
	}
	for (int i=0; i<n; ++i) {
	    double x;
	    scanf("%lf", &x);
	    ken.push_back(x);
	}
	
	sort(ken.begin(), ken.end());
	sort(naomi.begin(), naomi.end());
	
	printf("%d %d\n", deceitful_war_answer(n), war_answer(n));
}

int main() {
	
	int t;
	scanf("%d",&t);
	
	for (int i=0; i<t; ++i) {
		printf("Case #%d: ",i+1);
		solve();
	}
	
	return 0;
}
