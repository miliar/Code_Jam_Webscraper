#include <cassert>
#include <algorithm>
#include <iostream>
#include <vector>
#include <map>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef unsigned long ul;
typedef unsigned short us;
typedef unsigned char uc;

int main()
{
  int cases;
  cin >> cases;
  for(int loop=1; loop<=cases; loop++)
  {
    printf("Case #%d: ",loop);
    int n; ull p; cin >> n >> p;

 if (n==1) { printf("%lld %lld\n",p-1,p-1); continue; }

    vector<ull> best, worst, rank;
    ull M = (1ULL << n)-1, W=M, B=M, R=0;

    worst.push_back(W); best.push_back(B); rank.push_back(R);

    B--;
    for(int i=1;i<n-1;i++)
    {
      W/=2; R=2*R+2;
      worst.push_back(W); best.push_back(B); rank.push_back(R);
    }

    R += 2; W/=2;
    worst.push_back(W); best.push_back(B); rank.push_back(R);

    for(int i=1;i<n-1;i++)
    {
      R += (1ULL << (n-1-i)) ; B -= (1ULL << i);
      worst.push_back(W); best.push_back(B); rank.push_back(R);
    }
    
    W=B=0; R++;
    worst.push_back(W); best.push_back(B); rank.push_back(R);

    for(int i=0;i<worst.size();i++)
    {
      fprintf(stderr,"%llu: %llu-%llu\n", rank[i], worst[i],best[i]);
    }

    int k=worst.size();

    ull m = M - p + 1; fprintf(stderr, "min score = %llu\n",m);
    int a,b;
    for(a=0;a<k && worst[a]>=m;a++);
    for(b=0;b<k && best[b]>=m;b++);
    printf("%llu %llu\n", rank[a-1],rank[b-1]);

    // puts("");
  }
}
