#include<limits.h>
#include<stdio.h>
#include<iostream>
#include<string.h>

using namespace std;

int a[1000001];



int rev(int k){

    int sum=0;
    while(k!=0){

            sum+=k%10;
            sum*=10;
			k/=10;
        }
        sum/=10;
        return sum;

    }

int main(){


	freopen("A-small-attempt1.in","r",stdin);
    freopen("outputA.in","w",stdout);


    int i,j,k,t,n,z=1;
    //char b[100001];
	memset(a,0,sizeof(a));
    a[1]=1 ;
//	cout<<a[3];
    cin>>t;

    for(int i=2;i<=1000001;i++)
    a[i]=100000000;

    for(i=2;i<=1000001;i++){


         a[i]=min(a[i-1]+1, a[i]);

         j=rev(i);
         //cout<<j<<endl;

        // if(j<1000001){
         a[j]=min(a[i]+1, a[j]) ;
       // }

    }
    //cout<<a[91]<<endl;
//cout<<a[90];
while(t--){

    cin>>n ;

        cout<<"Case #"<<z<<": "<<a[n]<<endl;
z++;
        }
    return 0;

    }
