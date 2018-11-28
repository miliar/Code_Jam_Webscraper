#include<iostream>
#include<math.h>
#include<stdio.h>
using namespace std;
inline bool palin(int n);
inline int len(int n);
int main(){
    unsigned t=0;int tt=1;
    FILE *p=fopen("C-small-attempt2.in","r");//------------
    FILE *o=fopen("out.txt","w+");
    fscanf(p,"%u",&t);
    while(t){
        int x,y;
        fscanf(p,"%d%d",&x,&y);
        int count=0;
        for(int i=x;i<=y;i++)
        {
            if(palin(i)){
                double m =sqrt(i);
                int p;
                p=m;
                if(p==m)
                    if(palin(p))
                        count++;
            }


        }
        fprintf(o,"Case #%d: %d\n",tt,count);
        tt++;
        t--;
    }
    fclose(p);
    fclose(o);
return 0;
}
inline int len(int n){
    //if(x>=1000) return 4;
    if(n>=100) return 3;
    if(n>=10) return 2;
    return 1;
}
inline bool palin(int n){
    if(1000==n)
        return false;
    int l=len(n);
    if(1==l){
        return true;
    }
    else if(2==l){
       if((n/10)==(n%10))
            return true;
    }
    else{
        if((n/100)==((n%100)%10))
            return true;
    }
      return false;
}

