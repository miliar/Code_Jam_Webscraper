#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <vector>
#include <algorithm>
#include <queue>
#define FWD(a,b,c) for(int a=(b); a<(c); ++a)
#define BCK(a,b,c) for(int a=(b); a>(c); --a)
#define PII pair<int, int>
#define x first
#define y second

using namespace std;

typedef long long LL;

int n, p, c;
int X[2010];
int A[2010];
int B[2010];
int CA[2010];
int CB[2010];
vector<int> I;
bool exist[2010];

int main(){
	int Z;
	scanf("%d", &Z);
	FWD(z,1,Z+1){
		scanf("%d", &n);
		FWD(i,0,n) scanf("%d", &A[i]);
		FWD(i,0,n) scanf("%d", &B[i]);
		FWD(i,0,n) X[i] = -1;
		FWD(i,0,n){
			I.clear();
			FWD(j,0,n){
				exist[j] = 0;
				if(X[j] != -1){
					if(I.empty() || I.back() < X[j])
						I.push_back(X[j]);
					else
						I[lower_bound(I.begin(), I.end(), X[j]) - I.begin()] = X[j];
				}
				CA[j] = I.size() + 1;
			}
			I.clear();
			BCK(j,n-1,-1){
				if(X[j] != -1){
					if(I.empty() || I.back() < X[j])
						I.push_back(X[j]);
					else
						I[lower_bound(I.begin(), I.end(), X[j]) - I.begin()] = X[j];
				}
				CB[j] = I.size() + 1;
			}
			c = -1;
			BCK(j,n-1,-1)
				if(X[j] == -1 && CA[j] == A[j] && CB[j] == B[j]){
					if(!exist[A[j]])
						c = j;
					exist[A[j]] = 1;
				}
			X[c] = i;
		}
		printf("Case #%d: ", z);
		FWD(i,0,n) printf("%d ", X[i]+1);
		printf("\n");
	}
}

