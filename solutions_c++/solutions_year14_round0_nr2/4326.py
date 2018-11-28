#include<fstream>
#include<iostream>
#include<cstdio>
#include<map>

using namespace std;

#define FL(i, a, b) for(int i = a; i < b; i++)
#define MIN(a, b) ((a > b)? b : a)
#define MAX(a, b) ((a > b)? a : b)

int main(int argc, char *argv[]) {
  if (argc != 2) {
    printf("file input\n");
    return -1;
  }

  ifstream fin(argv[1]);

  double c,f,x;
  int fac,fac_begin,fac_end;
  double time;
  bool buy;

  int T;
  fin>>T;
  FL(t,0,T) {
    fin>>c>>f>>x;
    fac_begin = 0;
    fac_end = 1000000;
    time=0;
    buy=true;

    while(buy) {
      fac=(fac_begin+fac_end)/2;
      if (fac_begin == fac_end) {
        break;
      }

      double time_win = x / (2 + f*fac);
      double time_buy = c / (2 + f*fac) + x / (2 + f*(fac+1));
      if (time_win<=time_buy) {
        fac_end = fac;
      } else {
        fac_begin = fac+1;
      }
    }

    FL(i,0,fac) {
      time += c / (2 + f*i);
    }
    time += x / (2 + f*fac);

    printf("Case #%d: %.7f\n",t + 1,time);
  }
  return 0;
}

