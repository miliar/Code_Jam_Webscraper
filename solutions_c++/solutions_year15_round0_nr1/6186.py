#include<bits/stdc++.h>
using namespace std;
//#define FILEIO(x) freopen(#x ".in","r",stdin);freopen(#x ".out","w",stdout);
//#define FILEIOS freopen("input.txt","r",stdin);freopen("output.txt","w",stdout);

int main()
{   freopen("input.in","r",stdin);
    freopen("output.out","w",stdout);
     char str[20000];
    long int st;
      long int test,i,j;
    scanf("%ld",&test);
    for(i=1;i<=test;i++)
    {
        scanf("%ld",&st);
        scanf("%s",str);
        long int cnt=0;
       long  int sum=0;
        for(j=0;j<=st;j++)
        {
            if(str[j]!='0')
            {
        if(sum<j)
        {
            cnt+=(j-sum);
            sum=j+str[j]-48;
        }
        else sum+=str[j]-48;
        }
        }
        cout<<"Case #"<<i<<": " <<cnt<<endl;
    }
    return 0;
}
