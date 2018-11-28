#include <iostream>
using namespace std;

void bestAns(double C, double F, double X, double V, double &cur, bool flag){
	if (X < C)
	{
		cur += X / V;
		flag = true;
		return;
	}
	if (flag == true)
		return;
	double t1, t2, tmp;
	t1 = X / V;
	tmp = C / V + X / (V + F);
	if (t1 < tmp){
		cur += t1;
		flag = true;
		return;
	}
	else{
		cur += C / V;
		bestAns(C, F, X, V + F, cur, flag);
	}
	return;
}

void main(){
	double C, X, F;
	int N;
	FILE *fr, *fw;
	fopen_s(&fr, "B-small-attempt1.in", "r");
	fopen_s(&fw, "output.txt", "w");
	fscanf_s(fr, "%d", &N);
	int x = 1;
	double ans = 0;
	while (x <= N){
		fscanf_s(fr, "%lf%lf%lf", &C, &F, &X);
		ans = 0;
		double V = 2;
		bestAns(C, F, X, V, ans, false);
		fprintf_s(fw, "Case #%d: %.7lf\n", x, ans);
		x++;
	}
}