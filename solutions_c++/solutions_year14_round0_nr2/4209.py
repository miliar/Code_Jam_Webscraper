#include <cstdio>
#include <iostream>
#include <map>
#include <set>
#include <vector>
#include <cstring>
#include <sstream>
#include <stack>
#include <queue>
#include <deque>
#include <algorithm>
#include <cmath>
#include <cstdlib>

using namespace std;

int main(){
freopen("input.txt","r",stdin);
freopen("output.txt","w",stdout);

int t;
scanf("%d",&t);

double X,F,C;

for (int i=1;i<=t;++i){
cin>>C>>F>>X;
double V;
V=2.0;

double timer=0;

double a,b;
double work;

printf("Case #%d: ",i);
if (X<=C)
printf("%.7lf\n",X/V);
else{
while (true){

timer+=C/V;
a=(X-C)/V;
b=(X)/(V+F); 

if (a<b){
timer+=a;
break;
}
V+=F;	


}	
printf("%.7lf\n",timer);
}

}


return 0;
}
