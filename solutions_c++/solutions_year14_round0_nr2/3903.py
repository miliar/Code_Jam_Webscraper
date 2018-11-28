
//main includes
#include<iostream>
#include<cstdio>
#include<cstring>
#include<ctime>
#include<cmath>


//other includes
#include<algorithm>
#include<climits>
#include<vector>
#include<queue>
#include<stack>
#include<bitset>
#include<set>
#include<deque>
#include<cstdlib>
#include<map>
#include <iomanip> 
#include <utility>

#define re



using namespace std;

#define FOR(a,b)        for(__typeof(b) i=(a);i<(b);i++)




int main(){
#ifdef re
freopen("input.txt","r",stdin);
freopen("output.txt","w",stdout);
freopen("log.txt","w",stderr);;
#endif

int n=1,t;
double c,f,x;
double rate=2;
double minTime;
double tmpTime;
cin>>t;
while(n<=t){
rate=2;
cin>>c>>f>>x;
minTime=x/rate;
tmpTime=c/rate;
rate+=f;

while((tmpTime+x/rate)<minTime){
//cout<<minTime<<" ";
minTime=tmpTime+x/rate;
tmpTime+=c/rate;
rate+=f;
}

cout<<"Case #"<<n<<": "<<setprecision(7)<<fixed<<minTime<<endl;

n++;
}



#ifdef re
//printf("\n  Time Taken  %.31f sec\n",(double)clock()/(CLOCKS_PER_SEC));

#endif
return 0;
}

