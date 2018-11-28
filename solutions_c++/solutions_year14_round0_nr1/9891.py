#include <algorithm>
#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <stdlib.h>
#include <stdio.h>
#include <string>
#include <string.h>
#include <set>
#include <stack>
#include <map>
#include <list>
#include <deque>
#include <queue>
#include <vector>
#include <bitset>
#include <cmath>
#include <ctime>
#include <functional>
#include <numeric>
#include <valarray>
#include <utility>

using namespace std;

typedef long long ll;
typedef unsigned int ui;
typedef vector <int> vi;
typedef pair <int, int> ii;
typedef vector <ii> vii;
typedef set<int> si;
typedef map<string, int> msi;

int main(){
  int T;
  scanf("%i",&T);
  for(int i=1;i<=T;i++){
     int a,b,A[4][4],B[4][4],c=0,p;
     scanf("%i",&a);
     for(int j=0;j<4;j++)for(int k=0;k<4;k++)cin>>A[j][k];
     scanf("%i",&b);
     for(int j=0;j<4;j++)for(int k=0;k<4;k++)cin>>B[j][k];
       for(int j=0;j<4;j++)for(int k=0;k<4;k++)if(A[a-1][j]==B[b-1][k]){c++;p=j;}

     if(c==0)printf("Case #%i: Volunteer cheated!\n",i);
     else if(c==1)printf("Case #%i: %i\n",i,A[a-1][p]);
     else printf("Case #%i: Bad magician!\n",i);
  }
  return 0;
}
