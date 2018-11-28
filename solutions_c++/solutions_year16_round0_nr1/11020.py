#define TASKNAME ""
#include <bits/stdc++.h>

#define MAXN int(1e3 + 10)
#define INF int(1e9)
#define pb push_back
#define mp make_pair
#define sz(A) (int)(A).size()
#define pi 3.1415926535897932384626433832795
#define sqr(a) ((a) * (a))
#define x fghsdhgjfshgkjfdhgjfs
#define y jhfjghjfdsghsjfd
#define out(x) cout<<(x)<<" " << "\n"
#define DB(x) cerr<<#x<<" = "<<(x)<<"\n"
#define DB2(a,b)   cerr<<#a<<"="<<(a)<<", "<<#b<<"="<<(b)<<"\n"

using namespace std;
int tests, n, used[50];


void fill_num(int n){
  while(n > 0){
    int a = n % 10;
    used[a] = 1;
    n /= 10;
  }
}


bool check(){
  for(int i = 0; i <= 9; i++)
    if(used[i] == 0)
      return 0;
  return 1;
}


int main()
{
  
  #ifndef ONLINE_JUDGE
    freopen("A-large.in", "r", stdin);
    freopen("a.out", "w", stdout);
  #endif
  cin >> tests;
  for(int test = 1; test <= tests; test++){
    cin >> n;
   // DB(n);
    for(int i = 0; i <= 9; i++)
      used[i] = 0;
    printf("Case #%d: ", test);
    if(n == 0){
     printf("INSOMNIA\n"); 
    }
    for(int i = 1; i <= 100; i++){
      fill_num(n * i);
      if(check()){
         printf("%d\n", n * i);
         break;
      }    
    }   
  
  } 
  return 0;
}