#include <cstdio>
#include <algorithm>
#include <string>
#include <iostream>
#define fori(l,n) for(int l=0;l<n;l++)
using namespace std;
int main() {
	int I,IT,nada;

    int t;
	float N[100];
	long long int A,B,R,K;
	//int T[5000];
	int sum;
    freopen("B-small-attempt0.in","r",stdin);
   freopen("1.out","w",stdout);
    I=1;
    
        
    scanf("%d", &IT); 
    
    
    while(I<=IT){
       cin>>A>>B>>K;
       //R=A&B;
       //cout<<"R:"<<R<<endl;
      /* fori(ii,5000){
          T[ii]=0;
       }*/
       sum=0;
       fori(ii,A){
          fori(jj,B){
            R=ii&jj;
            
            if(R<K)
            sum++;//T[R]++;
          }
       }
     /*  sum=0;
       fori(ii,K){
         sum=sum+T[ii];
       }*/
        printf ("Case #%d: ",I);
        cout<<sum<<endl;
        
       I++;
    }
    scanf("%d", &nada);
	return 0;
}

