#include<bits/stdc++.h>
using namespace std;
int main()
{
    long long int test,g=1;
    scanf("%lld",&test);

    while(test--)
    {
        string str;
        long long int a=1050,b=1050,leng;
        cin>>str;
        char ar[3000];
        ar[1050]=str[0];
        char y=str[0];
        leng=str.length();
        for(int i=1;i<leng;i++)
        {
           if(str[i]>=y)
           {
              a=a-1;
              ar[a]=str[i];
              y=str[i];
           }
           else
            {
                b=b+1;
                ar[b]=str[i];
            }
        }
        printf("Case #%d: ",g);
       for(int i=a;i<=b;i++)
        {
            cout<<ar[i];
        }
        printf("\n");
        g++;
    }
    return 0;
}
