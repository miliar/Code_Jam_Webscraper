#include <cstdio>
#include <vector>
long long int t;
using namespace std;

long long int tab[] = { 
1, 
10, 
100, 
1000, 
10000, 
100000, 
1000000, 
10000000, 
100000000,
1000000000,
10000000000,
100000000000,
1000000000000,
10000000000000,
100000000000000
} ;
int nchars(long long int i){
 int c=0;
 long long int *p = tab ;
 do{c++;}while(*(p+c) <= i);
return c;
}
long long int wut(long long int i, long long int acc){
if(i==0)return acc;
return wut(i/10,10*acc+(i%10));
}

long long int prev(long long a){
a--;
//printf("%Ld %d\n",a,nchars(a));
int n=nchars(a);
long long dixn=1;
for(int i=0;i<(n+1)/2;i++)dixn*=10;
return dixn*(a/dixn)+1;
}

long long int prev_b(long long a){
 return prev(a-1);
}


long long int solve(long long int a){
long long int sol=1;

while(a!=1){
//printf ("a=%Ld prev=%Ld wut=%Ld\n",a,prev(a),wut(a,0));
if(prev(a)==a)// 2e moitie de a est 00001
{
if(wut(a,0)==a){sol+=a-prev_b(a);a=prev_b(a);}
else{sol++;a=wut(a,0);}
}
else{
sol+=a-prev(a);
a=prev(a);
}
}

return sol;


}


int main(){
scanf("%d",&t);
int npb;

for(int npb=1;npb<=t;npb++){
long long int a;
scanf("%Ld",&a);

long long int sol=solve(a);


printf("Case #%d: %Ld\n",npb,sol);
}
}
