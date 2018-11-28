#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <iostream>
#include <string>
#include<math.h>
#include<conio.h>
using namespace std;
int maxcd(int *c,int n){
    int maxed=-1,ind;
    for(int i=0;i<n;i++){
        if(maxed<c[i]){
            maxed=c[i];
            ind=i;
        }
    }
return ind;
}
int dup(int *c,int n,int ind,int val){
int hr=0;
    for(int i=0;i<n;i++){
        if(c[i]==val&&i!=ind)
            hr++;
    }
    return hr;
}
int main()
{
    FILE *fin = freopen("A-small-attempt0.in", "r", stdin);
	assert( fin!=NULL );
	FILE *fout = freopen("B12.out", "w", stdout);
    int max1,max2,t=1,n,j=0,temp,temp1,hr=0;
    char a[250];
    int c[100];
    cin>>t;
    //cin.getline(a,50);

    for(int k=1;k<=t;k++){
        cin>>n;
        j=0;
        for(int i=0;i<n;i++)
        cin>>c[i];
        if(n==2){
            while(1){
                if(c[0]>1&&c[1]>1){
                    a[j++]='A';
                    a[j++]='B';
                    c[0]-=1;
                    c[1]-=1;
                }
                else if(c[0]==1&&c[1]>1){
                    //a[j++]='A';
                    a[j++]='B';
                    //c[0]-=1;
                    c[1]-=0;
                }
                else if(c[0]>1&&c[1]==1){
                    a[j++]='A';
                    //a[j++]='B';
                    c[0]-=1;
                    //c[1]-=0;
                }
                else if(c[0]==1&&c[1]==1){
                    a[j++]='A';
                    a[j++]='B';
                    c[0]-=1;
                    c[1]-=1;
                    break;
                }
                a[j++]='*';
            }
        }
        if(n==3){
            while(1){
                max1=maxcd(c,n);

                if(dup(c,n,max1,c[max1])==n-1){
                    while(1){
                    if(c[0]>1){
                        for(int gh=0;gh<n;gh++){
                            a[j++]=65+gh;
                            c[gh]--;
                            a[j++]='*';
                        }
                    }
                    else{
                        a[j++]='A';
                        a[j++]='*';
                        a[j++]='B';
                        a[j++]='C';
                        a[j++]='*';
                        break;
                    }
                    }
                    break;
                }
                else{
                    a[j++]=65+max1;
                    c[max1]-=1;
                    a[j++]='*';
                }

            }
        }
        cout << "Case #"<< k << ": ";
        for(int i=0;i<j;i++){
            if(a[i]=='*')
                cout<<" ";
            else
                cout<<a[i];
        }
        cout<<endl;
    }

	return 0;
}
