#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <iostream>
#include <string>
using namespace std;
typedef long long LL;
using namespace std;
int reverse_p(char *a,int temp){
    char temp1;
    int ind=temp;
    for(int i=0;i<temp;i++,temp--){
        temp1=a[temp];
        if(a[i]=='+')a[temp]='-';
        else a[temp]='+';
        if(temp1=='+')a[i]='-';
        else a[i]='+';
    }
    if(ind%2==0){
        if(a[temp]=='+')a[temp]='-';
            else a[temp]='+';
    }
    return 0;
}

int main()
{
    FILE *fin = freopen("B-large.in", "r", stdin);
	assert( fin!=NULL );
	FILE *fout = freopen("B8.out", "w", stdout);
    int i,temp=0,t,f=1,j,n,n1,n2,len,moves;
    char a[150];
    cin>>t;
    for(int k=1;k<=t;k++){
        for(j=0;j<100;j++)
            a[j]='\0';
        f=0;
        moves=0;
        cin >>a;
        for(len=0;a[len];len++);
            len--;
        for(int i=0;i<=len;i++){
            if(a[i]=='-'){
                    f=1;
            }
        }
        while(f){
            for(;a[len]!='-';len--);
            if(a[0]=='+'&&len!=0){
                for(int yu=0;a[yu]!='-';yu++){
                    a[yu]='-';
                }
                moves++;

            }
            reverse_p(a,len);
            len--;
            moves++;
            f=0;
            for(i=0;i<=len;i++){
                if(a[i]=='-'){
                    f=1;
                    break;
                }
            }
        }
        cout << "Case #" << k << ": "<< moves<< endl;
    }
	return 0;
}
