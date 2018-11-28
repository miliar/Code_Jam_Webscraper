int N;

#include <stdio.h>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <vector>
#include <algorithm>

using namespace std;

int solve(int A, int N, int m[]) {

  int add = 0;

  for (int i=0; i<N; i++) {
    int a = 0;
    int del = N-i;
    while (A<=m[i]) {
      a++;
      A=A+A-1;
      if (a > del) {
          // doesnt pay off to add more, just delete tail
        return add + del;
      }
    }
    A+=m[i];
    add += a;
  }
  return add;
}

int main(int argc, char* argv[])
{
  if (argc>1) freopen(argv[1],"r",stdin);
  if (argc>2) freopen(argv[2],"w",stdout);
  // Input
  scanf("%d\n",&N);
  //fprintf(stderr,"N = %d: \n",N);

  // Output
  for (int x=1; x<=N; x++) {
    //fprintf(stderr,"Case #%d: \n",x);

    int A,N;
    int m[100];

    string str;
    getline(cin,str);
    {
    stringstream ss(str);
    ss >> A >> N;

    }
    {
      getline(cin,str);
      stringstream ss(str);
      for (int i=0; i<N; i++) {
        ss >> m[i];
      }
    }

    printf("Case #%d: ",x);
    sort(m,m+N);
    int ops = solve(A,N,m);
    printf("%d\n",ops);
    fprintf(stderr,"Case #%d: %d\n",x,ops);
  }
  return 0;
}
