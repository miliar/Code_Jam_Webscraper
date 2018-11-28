#include <iostream>
#include <cstring>
#include<cmath>
using namespace std;
long int guss(long int temp,long int bi){
   long int no=1;
   int i;
    while(temp>0){
        no=no*10;
        temp--;
    }
    no=no+bi;
    no=no*10;
    no++;
    return no;
}
long int store[10];

long int nt(long int gus){
    long int i,j,temp,k,flag=1,con=0;
    long int m=gus;
    i=2;
    while(i<=10){
        m=gus;
        j=0;
        con=0;
        while(m>0){
            temp=m%10;
            m=m/10;
            con+=temp*pow(i,j);
            j++;
        }
        j=2;
        k=sqrt(con)+1;
    //    std::cout<<endl<<con<<"\t"<<k;
        while(j<k){
            temp=con%j;
            if(temp==0){
                store[i-2]=con/j;
                break;
            }
            j++;
        }
        if(con%j!=0){
            flag=0;
            break;
        }
        i++;
    }
    return flag;

}
int main()
{   long int t,n,j,temp,k=0,gus,bi=0,l,m=0,div,i,flag=1,f=0;
    std::cin>>t>>n>>j;
    temp=n-2;
    std::cout<<"Case #1:"<<endl;
    while(k<j){
        gus=guss(temp,bi);
        div=nt(gus);
        if(div==1){
            std::cout<<gus;
            for(i=0;i<9;i++){
                std::cout<<" "<<store[i];
            }
            std::cout<<endl;
            k++;
        }
        for(l=0;l<9;l++)
        {
            store[l]=0;
        }
        f++;
        m=f;
        l=1;
        flag=1;
        i=1;/*
        while(flag){
            l=m%10;
            m=m/10;
            if(l==0){

                bi=bi+pow(10,i);
                if(i !=0)
                    bi=bi-pow(10,i-1);
                flag=0;
            }

            i++;
        }*/
        bi=0;
        do
        {
            l=m%2;
            bi=bi + (i*l);
            m=m/2;
            i=i*10;
        }while(m>0);

    }
    return 0;
}
