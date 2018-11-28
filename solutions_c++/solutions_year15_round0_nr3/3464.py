#include <iostream>
#include <string.h>
#include <fstream>
#include <stdlib.h>
using namespace std;
ifstream f("input");
ofstream o("output");
int sign(int x){
    if(x>0)
        return 1;
    if(x<0)
        return -1;
    return 0;
}
int rec(int quat[5][5],char vect[10002],int len){
    int i=1,j=2,k=3,sum1=1,sum2=1,sum3=1;
    for(i=1;i<=len-2;i++){
        while(sum1!=2 and i<=len-2){
            sum1=sign(sum1)*quat[abs(sum1)][vect[i]-103];
            i++;
        }
        if(i==len-1 and sum1!=2)
            return 0;
        sum2=1;
        for(j=i;j<=len-1;j++){
            while(sum2!=3 and j<=len-1){
                sum2=sign(sum2)*quat[abs(sum2)][vect[j]-103];
                j++;}
            if(j==len and sum2!=3)
                break;
            for(k=j;k<=len;k++){
                sum3=sign(sum3)*quat[abs(sum3)][vect[k]-103];
            }
            if(sum3==4 and sum2==3 and sum1==2)
                return 1;
        }
    }
    return 0;
}
int main()
{
    int sum,m,len,i,k,t,l,x,quat[5][5];
    char vect[10002],c,temp;
    quat[1][1]=1;
    quat[1][2]=2;
    quat[1][3]=3;
    quat[1][4]=4;
    quat[2][1]=2;
    quat[2][2]=-1;
    quat[2][3]=4;
    quat[2][4]=-3;
    quat[3][1]=3;
    quat[3][2]=-4;
    quat[3][3]=-1;
    quat[3][4]=2;
    quat[4][1]=4;
    quat[4][2]=3;
    quat[4][3]=-2;
    quat[4][4]=-1;
    f>>t;
    for(m=1;m<=t;m++){
        f>>l>>x;
        f.get();
        len=l*x;
        k=0;
        for(i=1;i<=l;i++){
            f.get(c);
            vect[i]=c;
        }
        vect[0]=vect[l];
        for(i=l+1;i<=len;i++){
            temp=vect[i%l];
            vect[i]=temp;
        }
        sum=1;
        for(k=1;k<=len;k++)
        {
            sum=sign(sum)*quat[abs(sum)][vect[k]-103];
        }
        if(sum==-1){
            if(rec(quat,vect,len)==1)
                o<<"Case #"<<m<<": YES"<<endl;
            else
                o<<"Case #"<<m<<": NO"<<endl;
        }
        else
            o<<"Case #"<<m<<": NO"<<endl;
    }
    return 0;
}
