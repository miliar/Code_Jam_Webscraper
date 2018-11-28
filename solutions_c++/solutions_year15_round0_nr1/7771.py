#include<iostream>
#include<stdio.h>
using namespace std;
#define gc getchar
void scanint(int &x)
{
    register int c = gc();
    x = 0;
    for(;(c<48 || c>57);c = gc());
    for(;c>47 && c<58;c = gc())  
        {x = (x<<1) + (x<<3) + c - 48;}//to convert into int
}
int main(){
        int t;int x=1;
        scanint(t);
        while(t--){
                int s;
                scanint(s);
                char a;int c,sum=0;int count=0;
                for(int i=0;i<=s;i++){
                        scanf("%c",&a);
                        c=a-48;
                        if(sum<i)
                                {count+=i-sum;
								sum=i;}
                       
                                sum=sum+c;
                }
                printf("Case #%d: %d\n",x++, count);
        }
        return 0;
}
