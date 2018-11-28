#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdlib>
#include <ctime>
#include <cstdio>
#include <set>
#include <queue>
#include <cmath>

using namespace std;

typedef pair<double, double> couple;
#define rep(i, n) for (int i = 0; i < n; ++i) 

double C, F, X;

void
read_input() {    
    cin >> C >> F >> X;
}

inline double 
cost_of_farm(int farm)
{
    double cost=0;
    rep(i, farm)
    {
	cost += C/(2+(i*F));
    }
    return X/(2+(farm*F)) + cost;
}

void
solve2(){
    if(X/2 < C/2 + (X/(2+F)))
    {
	printf("%.7f\n",X/2);
	return;
    }
    int lower = 1;
    int upper2 = -1;
    int upper = 1;
    double cost_upper;
    
    while (1)
    {
	cost_upper = cost_of_farm(upper);
	double cost_p1 = cost_of_farm(upper+1);
	double cost_m1 = cost_of_farm(upper-1);
//	cerr << "value of upper " << upper << " upper2 " << upper2 << " lower " << lower  << endl;
//	cerr << " -1 : " << cost_m1 << " +1 : " << cost_p1 << endl;
	if(cost_upper <= cost_p1 && 
	   cost_upper <= cost_m1)
	    break;
	
	if(cost_upper > cost_p1)
	{
	    if(upper2 == -1)
	    {
		lower = upper;
		upper = upper*2;
	    }
	    else
	    {
		double old_upper = upper;
		double new_upper = (upper+upper2)/2;
		if(new_upper == upper) upper = new_upper+1;
		else upper = new_upper;
		lower = old_upper;		
	    }
	    continue;
	}
	else if(cost_upper > cost_m1)
	{
	    double old_upper = upper;
	    upper2 = upper;
	    double new_upper = (upper + lower)/2;
	    if(new_upper == lower) upper = lower+1;
	    else upper = new_upper;
	    continue;	    
	}
	
    }
		
    printf("%.7f\n", cost_upper);    
}

void
solve(){
    // vector < double > cost_farm;
double cost_farm[100000];
    if(X <= 2)
    {
	printf("%.7f\n", X/2);
	return;
    }
    // cost_farm.resize(X/2+1);
    cost_farm[0] = 0;
    for(int i = 1; i<= 2*X; i++)
    {
	cost_farm[i] = cost_farm[i-1] + C/((i-1)*F+2);
//	cerr << "cost for " << i << " " << cost_farm[i] << endl;
    }

    double min = X/2;
    for(int i = 1; i< 2*X; i++)
    {
	if(cost_farm[i] + X/(2+F*i) < min) 
	{
	    min = cost_farm[i] + X/(2+F*i);
	    cerr << "min is with " << i << " - value" << min << endl;
	}
    } 
//    cerr << "--------------------" << min << "-----------------" << endl;
    printf("%.7f\n", min);
//    cout << min << endl;
}



int
main(int argc, char *argv[]) {

    int nb_input;
    cin >> nb_input;
    
    for(int nb_case = 0; nb_case < nb_input; nb_case++)
    {
	read_input();
	cout << "Case #" << nb_case+1 << ": " ;
	cerr << "Case #" << nb_case+1 << ": " ;
	solve2();
    }
  return 0;
}
