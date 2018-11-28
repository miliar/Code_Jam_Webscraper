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

dbl solve(dbl c, dbl f, dbl x)
{
 dbl answer;
 dbl tempAnswer;
 answer= x/2.0;
 int kMax= int(x/c)+10;
 dbl *time = new dbl [kMax];

 time[0]= 0;
 for (int k= 1; k<kMax && time[k-1]<answer; k++)
 {
//     cout<<k<<":  "<<time[k-1]<<"  "<<c<<"  "<<(2+(k-1)*f)<<endl;
    time[k]= time[k-1]+c/(2+(k-1)*f);
    tempAnswer= time[k]+x/(2+k*f);
    if (tempAnswer<answer) answer= tempAnswer;
 }
 //cout<<"end"<<endl;
 delete time;

 return answer;
}

int main()
{

 ios_base::sync_with_stdio(0);
 cin.tie(0);
// LL a[110];
// memset(a,0,sizeof(a));

  freopen("B_input_large.txt","r",stdin);
  freopen("output.txt","w",stdout);

 srand(__rdtsc());

 int T;
 cin>>T;
 dbl C,F,X;

 cout<<fixed;
 cout.precision(7);

 for (int TT=1; TT<=T; TT++)
 {
     cin>>C>>F>>X;
   //  cout<<TT<<endl;
     cout<<"Case #"<<TT<<": "<<solve(C,F,X)<<endl;
 }


 return 0;
}


