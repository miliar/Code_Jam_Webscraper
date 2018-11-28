#include <stdio.h>
#include <queue>
using namespace std;

void input();
void proc();
void output();

int main()
{
	freopen ("input.txt","r",stdin);
	freopen ("output.txt","w",stdout);

	int Test,Case=1;
	scanf ("%d",&Test); while (Test--){
		input();
		proc();
		printf ("Case #%d: ",Case++);
		output();
	}

	return 0;
}

int N,A[2020],B[2020],S[2020];
bool C[2020][2020],chk[2020]; int D[2020];

void input()
{
	int i;

	scanf ("%d",&N);
	for (i=1;i<=N;i++) scanf ("%d",&A[i]);
	for (i=1;i<=N;i++) scanf ("%d",&B[i]);
}

void proc()
{
	int i,j,c,k,u;

	for (i=1;i<=N;i++) for (j=1;j<=N;j++) C[i][j] = 0;
	for (i=2;i<=N;i++){
		c = 0;
		for (j=i-1;j>=1;j--){
			if (A[j] >= A[i]) C[i][j] = 1;
			else if (A[j] + 1 == A[i] && c == 0){
				c++; C[j][i] = 1;
			}
		}
	}
	for (i=N-1;i>=1;i--){
		c = 0;
		for (j=i+1;j<=N;j++){
			if (B[j] >= B[i]) C[i][j] = 1;
			else if (B[j] + 1 == B[i] && c == 0){
				c++; C[j][i] = 1;
			}
		}
	}

	priority_queue<int, vector<int>, greater<int> > Q; k = 1;

	for (i=1;i<=N;i++){
		D[i] = 0;
	}
	for (i=1;i<=N;i++){
		for (j=1;j<=N;j++) if (C[i][j]) D[j]++;
	}
	for (i=1;i<=N;i++){
		S[i] = 0;
		if (D[i] == 0){
			Q.push(i);
		}
	}
	while (!Q.empty()){
		i = Q.top(); Q.pop();
		S[i] = k++;
		for (j=1;j<=N;j++) if (C[i][j]){
			if (--D[j] == 0){
				Q.push(j);
			}
		}
	}

	for (i=1;i<=N;i++) if (S[i] < 1 || S[i] > N) {printf ("err"); return;}
	for (i=1;i<=N;i++) for (j=i+1;j<=N;j++) if (S[i] == S[j]) {printf ("err"); return;}
	for (i=1;i<=N;i++){
		int x = 0;
		for (j=i-1;j>=1;j--) if (S[j] < S[i]){
			if (x < A[j]) x = A[j];
		}
		if (x + 1 != A[i]) printf ("err"); return;
	}

	for (i=N;i>=1;i--){
		int x = 0;
		for (j=i+1;j<=N;j++) if (S[i] > S[j]){
			if (x < B[j]) x = B[j];
		}
		if (x + 1 != B[i]) printf ("err"); return;
	}
}

void output()
{
	int i;

	for (i=1;i<N;i++) printf ("%d ",S[i]);
	printf ("%d\n",S[N]);
}
