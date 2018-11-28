#include<iostream>
#include<math.h>
#include<stdio.h>
using namespace std;
inline bool palindrome(int n);
inline int length(long long int n);
inline long int reverse(long long int n);
int main(){
    unsigned test=0, t=1;
    scanf("%u",&test);
    while(test){
        int x,y;
        scanf("%d%d",&x,&y);
        int count=0;
        int i;
        for(i=x;i<=y;i++)
        {
            if(palindrome(i)){
                double m =sqrt(i);
                int p;
                p=m;
                if(p==m)
                    if(palindrome(p))
                        count++;
            }


        }
        printf("Case #%d: %d\n",t,count);
        t++;
        test--;
    }
return 0;
}

inline int length(int num){
    if(num>=100) return 3;
    if(num>=10) return 2;
    return 1;
}
inline bool palindrome(int n){
    if(1000==n) return false;
    int l=length(n);
    if(1==l) return true;
    if(2==l){
        if((n/10)==(n%10))
            return true;
    }
    else{
        if((n/100)==(n%10))
            return true;
    }
    return false;

}

