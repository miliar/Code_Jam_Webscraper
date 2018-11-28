#include <iostream>
#include<stdio.h>
#include<stdlib.h>
using namespace std;

long long int dtb(int n){
long long int bn=0;
if(n==0)
    bn=0;
else{
int y=1;

        while(n>=1){

            int r=n%2;
            n=n/2;
            bn=y*r+bn;
            y=y*10;
        }
}
        return bn;
}
long long int sum(long long int p,long long int q){
long long int sum=0;
if(p==0||q==0)
    sum=0;
    else{
            int j=1;
    while(p>0&&q>0){
            if((p%10+q%10)==2)
        sum=sum+(j*1);

        p=p/10;
        q=q/10;
    j=10*j;
    }
    }
    return sum;

}



int main()
{
    int t;
     freopen("input.in","rt",stdin);
    freopen("output.txt","wt",stdout);
    cin>>t;
    for(int i=0;i<t;i++)
    {
        int a,b,k,w=0;
        cin>>a>>b>>k;
        long long int ba=0,bb=0,bd=0;
        long long int *bk=new long long int[k];
        //converting all to binary
        for(int l=0;l<k;l++){
                bk[l]=dtb(l);
                }
        for(int j=0;j<a;j++){
            ba=dtb(j);

            for(int m=0;m<b;m++){

                bb=dtb(m);
                bd=sum(ba,bb);

                for(int l=0;l<k;l++){
                if(bd==bk[l]){
                    w++;
                    break;
                }
                }

            }
        }
        cout<<"Case #"<<i+1<<": "<<w<<endl;
    delete bk;
    }

    return 0;
}
