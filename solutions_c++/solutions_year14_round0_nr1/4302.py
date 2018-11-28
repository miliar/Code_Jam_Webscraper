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

  int a1, a2;
  int temp;
  map<int,int> m1,m2;

  int T;
  fin>>T;
  FL(t,0,T) {
    m1.clear();
    m2.clear();

    fin>>a1;
    FL(i,0,4)
    FL(j,0,4) {
      fin>>temp;
      if (i+1 == a1) {
        m1.insert(make_pair(temp,0));
      }
    }

    fin>>a2;
    FL(i,0,4)
    FL(j,0,4) {
      fin>>temp;
      if (i+1 == a2 && m1.find(temp) != m1.end()) {
        m2.insert(make_pair(temp,0));
      }
    }

    if (m2.size() == 1) {
      printf("Case #%d: %d\n",t + 1,m2.begin()->first);
    } else if (m2.size() > 1) {
      printf("Case #%d: Bad magician!\n",t + 1);
    } else {
      printf("Case #%d: Volunteer cheated!\n",t + 1);
    }
  }
  return 0;
}

