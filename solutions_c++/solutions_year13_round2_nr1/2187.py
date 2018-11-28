#include <iostream>
#include <cstdio>
#include <algorithm> 
#include <string>
#include <vector>
#include <queue>
#include <functional>
#include <cmath>
#include <sstream>

#define NMAX 10000
#define MMAX 10000


using namespace std;

long long int nec(long long int A, long long int B){int con=0; while (A<B){ con++; A+=A-1;} return con;} 

int main(){ int z,o,j,n,i; long long int s[NMAX],cont,cj,zj,sum,A;
cin>>z;
for (o=0;o<z;o++){ cont=0;
	cin>>A>>n; sum=A; for (j=0;j<n;j++){cin>>s[j]; } 
	sort(s,s+n);
	for (i=0;i<n;i++){ if (sum>s[i]) sum+=s[i]; 
				else {

				int con=0; if (sum> 1)while (sum<=s[i]){ con++; sum+=sum-1;} 
						else con = n+2;
	
			
					if (con>=(n-i)){ cont+=(n-i); break;}
					else {cont+=con; sum+=s[i]; }
				
					}
				/*cout<<cont<<": "<<sum<<"\n";*/

			}
	cout<<"Case #"<<o+1<<": "<<cont<<"\n";
}
return 0;}

		
