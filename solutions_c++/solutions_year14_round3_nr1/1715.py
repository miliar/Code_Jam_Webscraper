#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
#include<vector>
#include<cmath>
#include<set>

using namespace std;

int g() {
  char c;
  while(c=getchar(),(c<'0'||c>'9')&&(c!='-'));
  bool f=(c=='-');
  if(f) c=getchar();
  int x=0;
  while(c>='0'&&c<='9') {
      x=x*10+c-48;
      c=getchar();
  }
  return f?-x:x;
}

int main()
{
    freopen("A1.in","r",stdin);
    freopen("A1.out","w",stdout);
    int count = g();
    int p,q;
    double poss;
    double f;
    for(int i = 1; i <= count; i++) {
        p=g();
        q=g();
        poss = p * pow(2, 40) / q;
        f = poss - (long long int) poss;
        if(f) { cout << "Case #" << i << ": impossible" << endl; continue; }
        int pwr = 1;
        while((double)p/(double)q < (1.0 / pow(2, pwr))) pwr++;
        cout << "Case #" << i << ": " << pwr << endl;
    }
    return 0;
}

