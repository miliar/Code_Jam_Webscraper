#include <iostream>
#include <vector>
#include <string>
#include <cstdio>
#include <cfloat>

#define FOR(i,C) for(int i=0; i<C; i++)
#define FOR_REV(i,C) for(int i=C-1; i>=0; i--)

typedef long long ll_t;

using namespace std;

string ans(double C, double F, double X);
double time(double C, double F, double X, int n);

int main(int argc, char* argv[]){
  int T;

  cin >> T;

  // read input
  ll_t c = 0;
  while( cin ){
    if( ++c > T ) return -1;

    double C, F, X;
    cin >> C >> F >> X;

    // output answer
    cout << "Case #" << c << ": " << ans(C,F,X) << endl;
  }
}

string ans(double C, double F, double X) {
    int n_max = (int)(X/C);   // 1<=C<=500
    double min_time = DBL_MAX;
    char ret[100];

    if (n_max <= 7) {
        min_time = time(C, F, X, 0);
        for (int i = 1; i <= n_max; ++i) {
            double t = time(C, F, X, i);
            if ( t < min_time ) {
                min_time = t;
            }
        }
    } else {
        double t0,t1,tm0,tm1;
        t0 = time(C, F, X, 0);
        t1 = time(C, F, X, 1);
        tm0 = time(C, F, X, n_max);
        tm1 = time(C, F, X, n_max-1);

        if ( t0 <= t1 ) {
            min_time = t0;
        } else if ( tm0 < tm1 ) {
            min_time = tm0;
        } else {
            int edge[2] = {1, n_max-1};
            double t_edge[2] = {t1, tm1};
            while ( true ) {
                double t_np, t_n, t_nn;
                int next = (int)((t_edge[1]*edge[0] + t_edge[0]*edge[1])/(t_edge[0] + t_edge[1]));
                t_np = time(C, F, X, next - 1);
                t_n  = time(C, F, X, next);
                t_nn = time(C, F, X, next + 1);
                /*
                printf("edge = [%d,%d], t_edge = [%f, %f] next=%d\n",
                       edge[0], edge[1], t_edge[0], t_edge[1],
                       next);
                printf("t[next-1,next,next+1] = [%f, %f, %f]\n",
                       t_np, t_n, t_nn);
                */

                if ( t_n <= t_np && t_n <= t_nn ){
                    min_time = t_n;
                    break;
                } else if (t_np <= t_n) {
                    edge[1]   = next-1;
                    t_edge[1] = t_np;
                } else {
                    edge[0]   = next+1;
                    t_edge[0] = t_nn;
                }
            }
        }
    }

    sprintf(ret, "%.7f", min_time);
    return ret;
}


double time(double C, double F, double X, int n) {
    double ret = 0;

    for (int i = 0; i < n; ++i ) {
        ret += C/(2 + i*F);
    }
    ret += X/(2 + n*F);

    return ret;
}
