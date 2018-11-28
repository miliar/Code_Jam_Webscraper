//Coder: Karthikeyan Arulmozhivarman

#include <algorithm>
#include <bitset>
#include <deque>
#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <utility>
#include <vector>
#include <stdio.h>
#include <conio.h>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pi;
typedef vector<string> vs;

// Basic macros

#define st          first
#define se          second
#define all(x)      (x).begin(), (x).end()
#define ini(a, v)   memset(a, v, sizeof(a))
#define re(i,s,n)  	for(int i=s;i<(n);++i)
#define fr(i,n)     re(i,0,n)
#define tr(i,x)     for(typeof(x.begin()) i=x.begin();i!=x.end();++i)
#define pu          push_back
#define mp          make_pair
#define sz(x)       (int)(x.size())

bool seen[10] = {false};

void update_seen(long long int N)
{
   while(N > 0) {
      long long int digit = N%10;
      N/=10;
      seen[digit] = true;     
   }
}

bool seen_all()
{
   int seen_all = 0;
   
   fr(i,10) { 
      if(seen[i]) {
         seen_all++;
      }
   }     
   
   if(seen_all == 10) { 
      return true;
   } else {
      return false;
   }
}

void reset_seen()
{
   fr(i,10) { 
      seen[i] = false;
   }  
}

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large-out.txt", "w", stdout);
    int T,t;
    long long int N, M, count = 1;
    bool insomia = false;
    scanf("%d", &T);
    for(t = 1; t <= T; ++t) {
        scanf("%lld", &N);
        reset_seen();
        insomia = false;
        count = 1;
        while(!seen_all()) {
           if(N == 0){ M = N; insomia = true; break;}
           else {
              M = count * N;
              //printf("M=%u count=%d\n",M, count);
              update_seen(M);
              count++;
           }
        }
        
           if(!insomia) {            
              printf("Case #%d: %lld\n", t, M);
           } else {
              printf("Case #%d: INSOMNIA\n", t);
           }
    }
    
    getch();
	return 0;
}
