#include <iostream>
#include <stdio.h>


using namespace std;

int sumo(int a[]);

int main(){

    freopen( "input.in", "r", stdin );
	freopen( "output.out", "w", stdout );

    int t,p;
    scanf("%d",&t);
    for(p=1;p<=t;p++){
        int n;
        scanf("%d",&n);
        if(n==0)
            printf("Case #%d: INSOMNIA\n",p);
        else{
            int a[10]={0};
            int i=1,k,j,c;
            while(sumo(a)!=10){
                k=n*i;
                while(k!=0){
                    j=k%10;
                    a[j]=1;
                    k=k/10;
				}
                i++;
            }
            printf("Case #%d: %d\n",p,n*(i-1));
        }
    }
    return 0;
}

int sumo(int a[]){
    int c=0,i;
    for(i=0;i<10;i++)
        c+=a[i];
    return c;
}
