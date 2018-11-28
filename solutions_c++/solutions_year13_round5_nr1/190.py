#include <stdio.h>
#include <algorithm>
#include <map>
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

long long B,X[40],P[40]; int N;
map<long long, int> cnt;
double ans,expect;

void input()
{
	int i;

	scanf ("%lld %d",&B,&N);
	for (i=0;i<N;i++) scanf ("%lld",&X[i]);

}

void proc()
{
	int i,j;

	int get,c; long long x,b,nb; ans = 0;
	for (x=1;x<=1000;x++){
		get = 37 - N; b = get * x;
		for (j=0;j<get;j++) P[j] = x;
		for (j=0;j<N;j++) if (X[j] <= x){
			b += x - X[j]; 
			P[get++] = x - X[j];
		}

		sort(P,P+get); nb = b;
		for (j=0;j<get;j++){
			if (B < b) break;
			expect = 36. * (nb) / (get - j) - b;
			if (ans < expect)
				ans = expect;
			nb -= P[j];
			b++;
		}
	}
}

void output()
{
	printf ("%.8lf\n",ans);
}
