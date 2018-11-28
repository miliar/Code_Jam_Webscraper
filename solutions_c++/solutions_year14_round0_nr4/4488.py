/*
 * Q1.cpp
 *
 *  Created on: Apr 12, 2014
 *      Author: Neil
 */

#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <set>
#include <iomanip>
#include <cstring>
#include <algorithm>

using namespace std;

#define EPS 1e-8

int test;

#define LL long long

int N;

double A[10001];
double B[10001];

int main() {


	freopen("D-large.in","r", stdin);
	freopen("Q4.out","w",stdout);

	cin >> test;

	for(int t = 0; t < test; t++) {
		cout << "Case #" << t + 1 << ": ";

		cin >> N;

		for(int i = 0; i < N; i++) {
			cin >> A[i];
		}

		for(int i = 0; i < N; i++)
			cin >> B[i];



		sort(A,A+N);
		sort(B,B+N);

		int ans1 = 0;

		for(int b_min = 0, b_max = N - 1,a_min = 0, a_max = N - 1; b_max >= b_min;) {
			if(A[a_max] > B[b_max]) {
				a_max--;
				b_min++;
				ans1++;
			} else  {
				a_max--;
				b_max--;
			}
		}

		int ans2 = 0;

		for(int b_min = 0, b_max = N - 1,a_min = 0, a_max = N - 1; b_max >= b_min;) {
			if(A[a_min] < B[b_min]) {
				a_min++;
				b_max--;
			} else {
				a_min++;
				b_min++;
				ans2++;
			}
		}

//		for(int b_min = 0, b_max = N - 1,a_min = 0, a_max = N - 1; b_max >= b_min;) {
//			if(A[a_max] < B[b_max]) {
//				if(A[a_max] > B[b_min]) {
//					a_max--;
//					b_min++;
//					ans2++;
//				} else {
//					a_max--;
//					b_max--;
//				}
//			} else  {
//				if(A[a_min] < B[b_min]) {
//					a_min++;
//					b_min++;
//				} else {
//					a_min++;
//					b_min++;
//					ans2++;
//				}
//			}
//		}



		cout << ans2 << " " <<ans1 << endl;

//		for(int i = 0; i < N; i++) {
//			cout << A[i] << " " << B[i] << endl;
//		}


	}

	return 0;
}


