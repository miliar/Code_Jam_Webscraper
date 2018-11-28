#include <bits/stdc++.h>
using namespace std;

#define fi first
#define se second
#define pb push_back
#define mp make_pair 


typedef long long ll;
typedef double dbl;
typedef vector<int> vi;
typedef pair<int, int> pi; 

void doit() {
  int k,c,s;
  scanf("%d %d %d", &k,&c,&s);
  for(auto i=0;i<s;i++){
    if(i)putchar(' ');

    printf("%d",i+1);
  }
  puts("");
}

int main() {
  int tc;
  scanf("%d",&tc);
  for(int i=1;i<=tc;i++){
    printf("Case #%d: ",i);  
    doit();
  }
  return 0;
}
