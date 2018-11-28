#include<iostream>
#include<stdio.h>
#include<algorithm>
#define forn(i,n) for(i=0;i<n;i++)

using namespace std;
int sorti(float c[],int m){
    float kc;
    for(int i=0;i<m-1;i++)
        for(int j=0;j<m-1;j++)
            if(c[j]>c[j+1])
            {
                kc=c[j];
                c[j]=c[j+1];
                c[j+1]=kc;
            }
    return 0;
}

int main()
{
	int t;
	//freopen("prob4_small.in","r",stdin);
	//freopen("prob4_small.txt","w",stdout);
	freopen("prob3_large.in","r",stdin);
	freopen("prob3_large.txt","w",stdout);
	cin>>t;
	for(int p=1;p<=t;p++)
	{

        cout<<"Case #"<<p<<": ";
        int n,i,j;
        float a[1001],b[1001],va[1001],vb[1001];
        cin>>n;
        forn(i,n) cin>>a[i];
        forn(i,n) cin>>b[i];

        sorti(a,n);
        sorti(b,n);
        int max_ptr=n-1,min_ptr=0,counter=0;

        for(i=0;i<n;i++){
            if(a[i]>b[min_ptr]){
                min_ptr++;
                counter++;
            }
            else{
                max_ptr--;
            }
        }
        cout<<counter<<" ";
        max_ptr=n-1,min_ptr=0,counter=0;
        for(i=n-1;i>=0;i--){
            if(a[i]>b[max_ptr]){
                counter++;
                min_ptr++;
            }
            else{
                max_ptr--;
            }
        }

        cout<<counter<<endl;


    }
    return 0;
}

