#include<fstream>
#include<iostream>
#include<cstdio>
#include <algorithm>
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

  int n;
  int temp;
  double naomi[10000],ken[10000];
  int s1,s2;

  int T;
  fin>>T;
  FL(t,0,T) {
    fin>>n;
    FL(i,0,n) {
      fin>>naomi[i];
    }
    FL(i,0,n) {
      fin>>ken[i];
    }
    sort(naomi, naomi + n);
    sort(ken, ken + n);

    s1 = 0;
    temp = n-1;
    for (int i = n-1; i >= 0,temp >= 0; i--) {
      while (temp >= 0) {
        if (naomi[i] > ken[temp]) {
          s1++;
          temp--;
          break;
        }
        temp--;
      }
    }

    s2 = n;
    temp = 0;
    for (int i = 0; i < n,temp < n; i++) {
      while (temp < n) {
        if (ken[temp] > naomi[i]) {
          s2--;
          temp++;
          break;
        }
        temp++;
      }
    }
    printf("Case #%d: %d %d\n",t + 1, s1, s2);
  }
  return 0;
}

