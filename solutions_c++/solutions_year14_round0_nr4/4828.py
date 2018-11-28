#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#define MAXN 1010
using namespace std;
double a[MAXN], b[MAXN];
int flag[MAXN];
int main(void){
	FILE *fp = fopen("out.txt", "w");
	int T;
	cin >> T;
	for(int t=1; t<=T; ++t){
		int n;
		cin >> n;
		double maxa = -5;
		for(int i=0; i<n; ++i){
			cin >> a[i];
			maxa = max(maxa, a[i]);
		} 
		for(int j=0; j<n; ++j){
			cin >> b[j];
		}
		
		sort(a, a+n);
		sort(b, b+n);
		
		int count1 = 0;
		int nj = n-1;
		memset(flag, 0, sizeof(flag));
		for(int i=0; i<n; ++i){
			for(int j=0; j<n; ++j){
				if(a[i]>b[j] && flag[j]==0){
					count1++;
//					cout << "a[i] = " << a[i] << " b[j] = " << b[j] << endl;
					flag[j] = 1;
					break;
				} else if(a[i]<=b[j] && flag[nj]==0){
					flag[nj] = 1;
					nj--;
					break;
				}
			}
		}
		int count2 = 0;
		memset(flag, 0, sizeof(flag));
		for(int i=0; i<n; ++i){
			for(int j=0; j<n; ++j){
				if(b[j]-a[i]>1e-6 && flag[j]==0){
					flag[j] = 1;
					count2++; 
					break;
				}
			}
		}
		fprintf(fp, "Case #%d: %d %d\n", t, count1, n-count2);
	}
	return 0;
} 
