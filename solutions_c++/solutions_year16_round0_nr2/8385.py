#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

char stack[101];
char redu[101];

int analys(char s[])
{
    int n=strlen(s);
    if(s[n-1]=='+')return n-1;
    else return n;
}

void transmit()
{
    int i=1,n=strlen(stack),j=1;
    //char prev=stack[0];
    redu[0]=stack[0];
    while(i<n){
        if(stack[i]!=stack[i-1]){
            redu[j++]=stack[i];
        }
        i++;
    }
    redu[j]=0;
}

/*
void flip(int n)
{
    int i=0;
    while(i<n-1-i) {
        swap(stack[i],stack[n-1-i]);
        i++;
    }
}

int opti(int n)//return the number of steps
{
    if(n==0) {
        return 0;
    }
    if(stack[n-1]=='+') {
        return opti(n-1);
    } else {
        if(stack[0]=='-') {
            flip(n);
            return opti(n-1)+1;
        } else {
            int j=n-2;
            while(stack[j]!='+') {
                j--;
            }
            if(j==0) {
                return 2;
            } else {
                flip(j+1);
                flip(n);
                return 2+opti(n-1);
            }
        }
    }
}
*/


int main(int argc, char *argv[])
{
   // freopen("B-small-attempt0","r",stdin);
   // freopen("out.txt","w",stdout);
    int t;
    scanf("%d",&t);
    for(int i=0; i<t; i++) {
        scanf("%s",stack);
        //int n=strlen(stack);
        transmit();
        printf("Case #%d: %d\n",i+1,analys(redu));
    }
    return 0;
}
