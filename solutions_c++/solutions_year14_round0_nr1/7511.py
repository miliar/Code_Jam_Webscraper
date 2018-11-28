//solution by Wsl_F
#include <iostream>
#include <fstream>
#include <sstream>
#include <cmath>
#include <math.h>
#include <algorithm>
#define author Wsl_F
#include <cstring>
#include <stdlib.h>
#include <stdio.h>
#include <vector>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <deque>
#include <time.h>
#include <x86intrin.h>

using namespace std;

typedef long long LL;
typedef double dbl;
typedef vector<int> vi;

#define mp(x,y)  make_pair((x),(y))
#define pb(x)  push_back(x)

int main()
{

 ios_base::sync_with_stdio(0);
 cin.tie(0);
// LL a[110];
// memset(a,0,sizeof(a));

  freopen("A_input_small.txt","r",stdin);
  freopen("output.txt","w",stdout);

 srand(__rdtsc());

 int T;
 cin>>T;

 for (int TT=1; TT<=T; TT++)
 {
     int a,b;
     set<int> s,s1; s.clear(); s1.clear();
     int t;

     cin>>a;
     for (int i=1; i<=4; i++)
        for (int j=1; j<=4; j++)
     {
         cin>>t;
         if (i==a) s.insert(t);
     }

     cin>>b;
     for (int i=1; i<=4; i++)
        for (int j=1; j<=4; j++)
     {
         cin>>t;
         if (i==b && s.count(t))
            s1.insert(t);
     }

     cout<<"Case #"<<TT<<": ";
     if (s1.size()==0) cout<<"Volunteer cheated!"<<endl;
     else if (s1.size()==1) cout<<(*s1.begin())<<endl;
     else cout<<"Bad magician!"<<endl;
 }

 return 0;
}


