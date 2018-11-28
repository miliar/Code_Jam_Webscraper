#include <vector>
#include <iostream>
#include <fstream>
#include <utility>
#include <queue>
#include <set>
#include "assert.h"
#include <string>
#include <map>
#include <cstdlib>

using namespace std;

inline int abs(int a) {
     return max(a, -a);
     }

inline int distance(int xa, int ya, int xb, int yb) {
     return max(abs(xa-xb),abs(ya-yb));
     }

int main(void) {
     ifstream IN("C-large.in");
     ofstream OUT("C-large.out");
     int num_test;
     IN>>num_test;
          
     for (int test=1; test<=num_test; test++) {
          int W,H,B;
          IN>>W>>H>>B;
          
          vector <int> x0(B+2), y0(B+2), x1(B+2), y1(B+2);
          
          x0[0]=-1; x1[0]=0; y0[0]=0; y1[0]=H+1;
          
          for (int i=1; i<=B; i++) {
               IN>>x0[i]>>y0[i]>>x1[i]>>y1[i];
               x1[i]++;
               y1[i]++;
               }
          
          x0[B+1]=W; x1[B+1]=W+1; y0[B+1]=0; y1[B+1]=H+1;
          
          vector <int> DIST(B+2, W);
          vector <bool> used(B+2, false);
          DIST[0]=0;
          
          for (int t=0; t<B+2; t++) {
               int F=B+1;
               for (int i=0; i<=B+1; i++) if (!used[i] && (DIST[F]>DIST[i])) F=i;
               for (int i=0; i<=B+1; i++) if (i!=F) {
                    int dist=2*W+2*H;
                    dist=min(dist, distance(x0[F], y0[F], x0[i], y0[i]));
                    dist=min(dist, distance(x0[F], y0[F], x0[i], y1[i]));
                    dist=min(dist, distance(x0[F], y0[F], x1[i], y0[i]));
                    dist=min(dist, distance(x0[F], y0[F], x1[i], y1[i]));
                    dist=min(dist, distance(x0[F], y1[F], x0[i], y0[i]));
                    dist=min(dist, distance(x0[F], y1[F], x0[i], y1[i]));
                    dist=min(dist, distance(x0[F], y1[F], x1[i], y0[i]));
                    dist=min(dist, distance(x0[F], y1[F], x1[i], y1[i]));
                    dist=min(dist, distance(x1[F], y0[F], x0[i], y0[i]));
                    dist=min(dist, distance(x1[F], y0[F], x0[i], y1[i]));
                    dist=min(dist, distance(x1[F], y0[F], x1[i], y0[i]));
                    dist=min(dist, distance(x1[F], y0[F], x1[i], y1[i]));
                    dist=min(dist, distance(x1[F], y1[F], x0[i], y0[i]));
                    dist=min(dist, distance(x1[F], y1[F], x0[i], y1[i]));
                    dist=min(dist, distance(x1[F], y1[F], x1[i], y0[i]));
                    dist=min(dist, distance(x1[F], y1[F], x1[i], y1[i]));
                    if (x1[F]>=x0[i] && x1[i]>=x0[F]) dist=min(dist, min(abs(y0[i]-y1[F]),abs(y0[F]-y1[i])));
                    if (y1[F]>=y0[i] && y1[i]>=y0[F]) dist=min(dist, min(abs(x0[i]-x1[F]),abs(x0[F]-x1[i])));
                    
                    
                    DIST[i]=min(DIST[i], DIST[F]+dist);
                    }
               used[F]=true;
               }
          OUT<<"Case #"<<test<<": "<<DIST[B+1]<<"\n";
          }
     return 0;
     }
