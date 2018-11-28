#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <iostream>
#include <cmath>
#include <algorithm>

using namespace std;

struct oep_t {
	unsigned long o;
	unsigned long e;
	unsigned long p;
};

struct point_t {
	unsigned long p;
	unsigned long oe;
};

bool my_sort_func_oep (oep_t i, oep_t j) { return (i.o < j.o); }
bool my_sort_func_point (point_t i, point_t j) { return (i.p < j.p); }



unsigned long cost(unsigned long stops, unsigned long N) {
	unsigned long c=0, i, last=N-stops+1;
	for (unsigned long i=N; i>=last; i--) {
		c += i;
	}
	return c;
}




int main(void) {
	int num_cases;
	
	cin >> num_cases;
	unsigned long N, M, orig_cost, new_cost, pass;
//	point_t point = new point_t [2000];
	oep_t *oep = new oep_t [1000];
	unsigned long *came_on = new unsigned long [1000];
	int i, j, k, n;
	for (int case_num=1; case_num<=num_cases; case_num++) {
		printf("Case #%d: ", case_num);
		cin >> N >> M;
		for (i=0; i<M; i++) cin >> oep[i].o >> oep[i].e >> oep[i].p;
		
	//	sort(&(oep[0]), &(oep[M]), my_sort_func_oep);
		/*
		//points of interest
		for (i=0; i<M; i++) {
			point[2*i].p = oep[i].o;	//point
			point[2*i].oe = 2*i;	//who is it
			point[2*i+1].p = oep[i].e;
			point[2*i+1].oe = 2*i+1;
		}
		
		sort(&(point[0]), &(point[2*M]), my_sort_func_point);
		*/
//		printf("\n");
		orig_cost = 0;
		for (i=0; i<M; i++) {
			orig_cost += cost(oep[i].e - oep[i].o, N) * oep[i].p;
		}
//		cout << orig_cost << endl;
		
		
		for (i=1; i<=N; i++) came_on[i] = 0;
		
		new_cost = 0;
		for (i=1; i<=N; i++) {
		//	cout << "i " << i << endl;
			for (j=0; j<M; j++) {
				if (oep[j].o == i) {	//get on
					came_on[i] += oep[j].p;
				//	cout << "on " << i << "\n";
				}
			}
			
			for (j=0; j<M; j++) {
				if (oep[j].e == i) {	//get off
				//	cout << "off " << i << " " << oep[j].p << "\n";
					for (k=0; k<oep[j].p; k++) {
					//	cout << "k " << k << endl;
						for (n=N-1; n>=0; n--) if (came_on[n]) {
							came_on[n]--;
							new_cost += cost(i-n, N);
						//	cout << "off " << n << " " << i << "\n";
							break;
						}
					}
				}
			}
		}
//		cout << new_cost << endl;
		
		printf("%lu\n", orig_cost-new_cost);
	}

	return 0;
}