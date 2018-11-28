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

int main(void){
  int i, j, n, ncasos, caso, x, r, c, a, b;
  READ("D-small-attempt3.in");
  WRITE("Ds.out");
  scanf("%d", &ncasos);
  loop(caso, 0, ncasos){
    scanf("%d %d %d", &x, &r, &c);
    if (r>c) swap(r, c);
    //printf("\nx= %d\nr, c %d %d\n", x, r, c);
    if (x==1)
      printf("Case #%d: GABRIEL\n", 1+caso);
    else if (x>c || (r*c)%x!=0)
      printf("Case #%d: RICHARD\n", 1+caso);
    else if (x<=r || x==2)
      printf("Case #%d: GABRIEL\n", 1+caso);
    else if (x>2*r)
      printf("Case #%d: RICHARD\n", 1+caso);
    else{
      loop(i, 1, x-r){
        a=r-i; //left part of "tee"
        loop(j, 0, c-r){
          //printf("%d"
          if ((j*r+a)%x==0) break; //it works-->Gabriel wins
          //if ((r*c-(j*r+a))
        }
        if (j==c-r) break;//gabriel couldn't-->Richard wins
      }
      if(i>=x-r) printf("Case #%d: GABRIEL\n", 1+caso);
      else           printf("Case #%d: RICHARD\n", 1+caso);
    }
  }
  return 0;
}
