#include <cstdio>
using namespace std;

int counter = 0;
double C, F, X;

bool compare_sec(double f){
	double curr_time, next_time;
	curr_time = X/f;
	next_time = C/f + X/(f+F);
	if (curr_time<next_time)
		return false;
	else
		return true;
}

void make() {
	
    scanf("%lf", &C);
    scanf("%lf", &F);
    scanf("%lf", &X);
    
    double sec = 0.0, rate = 2.0;
    while(compare_sec(rate)){
		sec += C/rate;
		rate += F;
	}
	
	sec += X/rate;
    
	
	printf("Case #%d: %f \n", ++counter, sec);
	
    return;
}

int main() {
	freopen("B-large-attempt0.in", "r", stdin);
    freopen("b_outlarge0.txt", "w", stdout);
    int t; scanf("%d", &t);
    while(t--) {
        make();
    }
    return 0;
}
