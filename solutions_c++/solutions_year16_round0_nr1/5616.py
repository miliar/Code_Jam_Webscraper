#include <stdio.h>
#include <iostream>

using namespace std;

int sum(int a[]){
    int c=0,i;
    for(i=0;i<10;i++)
        c+=a[i];
    return c;
}

int main(){

    freopen( "input.in", "r", stdin );
	freopen( "output.out", "w", stdout );

    int t,z;
    scanf("%d",&t);
    for(z=1;z<=t;z++){
        int n;
        scanf("%d",&n);
        if(n==0)
            printf("Case #%d: INSOMNIA\n",z);
        else{
            int a[10]={0};
            int i=1,x,j,c;
            while(sum(a)!=10){
                x=n*i;
                while(x!=0){
                    j=x%10;
                    a[j]=1;
                    x=x/10;
				}
                i++;
            }
            printf("Case #%d: %d\n",z,n*(i-1));
        }
    }
    return 0;
}
