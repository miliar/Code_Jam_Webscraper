#include<stdio.h>
#include<iostream>
#include<string.h>
#include <cassert>
using namespace std;

int flip_invert(int *a,int n)
    {
    int i1,m,N=n,i,j; char b;

    for (m=0;;m++)
        {
        if (a[0]==1)
            {
            for (i1=0;(i1<n-1)&&(a[i1+1]==1);i1++);
            if (i1==n-1) break; 
            }
        else for (i1=n-1;(i1>=0)&&(a[i1]==1);i1--,n--);
        for (i=0,j=i1;i<=j;i++,j--)
            {
            b=1-a[i]; a[i]=1-a[j]; a[j]=b;
            }
        }
    return m;
    }
 int main()
 {
 	FILE *fin = freopen("B-large.in", "r", stdin);
    assert( fin!=NULL );
    FILE *fout = freopen("B-large.out", "w", stdout);
 	int a[200],length = 0,T,t;
 	char b[200];
 	cin>>T;
 	for(t = 1; t <= T; t++){
 	cin>>b;
	for(int i = 0; i < strlen(b); i++){
		if(b[i] == '-')
			a[i] = 0;
		else
			a[i] = 1;
		
	}
 	cout<<"Case #"<<t<<": "<<flip_invert(a,strlen(b))<<endl;

 }
}
