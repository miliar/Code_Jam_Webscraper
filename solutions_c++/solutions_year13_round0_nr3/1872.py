#include <iostream>
#include <cstdio>
#include <algorithm> 
#include <string>
#include <vector>
#include <queue>
#include <functional>
#include <cmath>
#include <sstream>
#define pb psh_back
#define all(v) v.begin(),v.end()
#define sz size()
#define rep(i,m) for(int y10=0;y10<m;y10++)
#define repv(i,n,m) for(int y11=n;y11>0;y11++)
#define For(it,c) for(__typeof(c.begin()) it=c.begin();it!=c.end();++it)
#define stringstream ss


#define NMAX 100000
#define MMAX 10000

typedef long long int ll;

using namespace std;
ll V[NMAX],c=0;

ll lbin(ll a){ll ret=1,c=10;
    while (a>0){ if((a%2)==1) ret=c; a/=2;
                 c*=10;} return ret;}
ll bin(ll a){ll ret=0,c=1;
    while (a>0){ 
      ret+=c*(a%2); a/=2;c*=10;} return ret;}
             
ll rbin(ll a){ll ret=0;
    while (a>0){ret=ret*10+a%2; a/=2;} return ret;}

ll intp(int A){ll c=1;for(ll i=0;i<A;i++) c*=10; return c;}

void create(){ ll i;  V[c]=0; c++; V[c]=1; c++; V[c]=2; c++; V[c]=3; c++;
for(i=1;i<16;i++){
	V[c]=(bin(i)*lbin(i)+rbin(i)); c++;
	V[c]=((bin(i)*10+0)*lbin(i)+rbin(i)); c++;
   	V[c]=((bin(i)*10+1)*lbin(i)+rbin(i)); c++;
	if ((i!=7)&&(i!=11)&&(i!=13)&&(i!=14)&&(i!=15)) {V[c]=((bin(i)*10+2)*lbin(i)+rbin(i)); c++;}}

}
void create1(){ int i;
for(i=0;i<4;i++){
	V[c]=2*intp(i)*intp(i)*10+2;  c++;
   	V[c]=(2*intp(i)*10+0)*intp(i)*10+2;  c++;
   	V[c]=(2*intp(i)*10+1)*intp(i)*10+2; c++;
 	}

}
int main(){ int z,o,n,t; ll A, B,sol; 
ll j;
create(); create1();
sort(V,V+c);
for(j=0;j<c;j++){/*cout<<V[j]<<" ";*/ V[j]*=V[j]; /*cout<<V[j]<<" \n";*/}
cin>>z;
for (o=0;o<z;o++){
	cin>>A>>B; sol=0;
	for(j=0;j<c;j++)if((V[j]>=A)&&(V[j]<=B)) sol++;
	cout<<"Case #"<<o+1<<": "<<sol<<"\n";
}
return 0;}

		
