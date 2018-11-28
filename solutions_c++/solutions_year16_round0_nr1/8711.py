#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <iostream>
#include <string>
using namespace std;
typedef long long LL;
using namespace std;
int check_digit(int *a,int temp){
    int i,j;
    for(i=0;a[i]!=-1;i++){
        if(a[i]==temp){
            for( j=i;a[j]!=-1;j++){
                a[j]=a[j+1];
            }
        }
    }
    if(a[0]==-1)return 1;
    else return 0;
}

int main()
{
    FILE *fin = freopen("A-large.in", "r", stdin);
	assert( fin!=NULL );
	FILE *fout = freopen("A-large.out", "w", stdout);
    int i,temp=0,t,a[11],f=1,j;
    int n,n1,n2;
    cin >>t;
    for(int k=1;k<=t;k++){
        for(j=0;j<10;j++)
            a[j]=j;
        a[10]=-1;
        f=1;
        scanf("%d",&n);
        if(n==0){
            cout << "Case #" << k << ": "<<"INSOMNIA"<< endl;
        }
        else{
        for(i=1;f;i++){
            n1=n*i;
            n2=n1;
            while(n1){
                temp=n1%10;
                n1/=10;

                if(check_digit(a,temp)){
                    f=0;
                    cout << "Case #" << k << ": "<< n2 << endl;
                    break;
                }
            }
        }
    }
    }
	return 0;
}
