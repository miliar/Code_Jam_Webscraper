#include <bits/stdc++.h>
#define loop(i,a,b) for(i=a;i<b;i++)
#define itloop(i,a) for(i=a.begin();i!=a.end();i++)
#define rev(i,a,b) for(i=a;i>=b;i--)
#define SET(a,c) memset(a,c,sizeof(a))
#define READ(file)  freopen(file, "r", stdin)
#define WRITE(file)  freopen(file, "w", stdout)
#define pb(a) push_back(a)
#define pf(a) push_front(a)
#define tup(a,b) make_pair(a,b)
#define popb()  pop_back()
#define popf()  pop_front()
#define x  first
#define y  second
#define LIM 1005

using namespace std;
typedef long long large;
typedef pair<int,int> ii;
typedef deque<int> di;
typedef deque<ii> dii;
typedef di::iterator dit;
char cad[LIM];
int main(void){
  int i, n, ncasos, caso, ct, acum;
  //setvbuf(stdin, NULL, _IOFBF, 1<<18);
  //setvbuf(stdout, NULL, _IOFBF, 1<<18);
  READ("A-large.in");
  WRITE("Al.out");
  scanf("%d", &ncasos);
  loop(caso, 0, ncasos){
    scanf("%d %s", &n, cad);
    ct=acum=0;
    loop(i, 0, n+1){
      if (acum<i){
        ct+=(i-acum);
        acum+=(i-acum);
      }
      acum+=cad[i]-'0';
    }
    printf("Case #%d: %d\n", 1+caso, ct);
  }
  return 0;
}
