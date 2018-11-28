#include <iostream>
#include<stdio.h>
#include<string>
#include<string.h>
using namespace std;
char s[1000];
long int t,n,i,j,sum,res;
int main()
{
    freopen ("A-small-attempt1.in","r",stdin);
    freopen ("A-small-attempt1.out","w",stdout);
    scanf("%ld",&t);
    for (i=0;i<t;i++){
        scanf("%d",&n);
        scanf(" %s",&s);
        sum=s[0]-'0';
        res=0;
        for (j=1;j<strlen(s) && sum<9;j++){
            if (j>sum && s[j]>'0'){
                res+=j-sum;
                sum+=j-sum;
            }
            sum+=s[j]-'0';
        }
        printf("Case #%ld: %ld\n",i+1,res);

    }
    return 0;
}
