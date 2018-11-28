#include <cstdio>
#include <cstring>
#include <cmath>
#include <cctype>
#include <cstdlib>
#include <algorithm>
#include <stack>
#include <queue>
#include <list>
#include <vector>
#include <map>
//#include <iostream>

using namespace std;

int main()
{
    int a,b,t,count;
    /*freopen("C-small-attempt4.in", "r", stdin);
    freopen("fairandsquare.o", "w", stdout);*/
    scanf("%d",&t);
    for(int i=1;i<=t;i++)
    {
        count=0;
        scanf("%d%d",&a,&b);
        for(int j=a;j<=b;j++)
        {
            int n, num, digit, rev;
            float m;
            bool num1=false,num2=false;
            rev = 0;
            num=j;
            n = num;
            do
            {
                digit = num%10;
                rev = (rev*10) + digit;
                num = num/10;
            }while (num!=0);
            if (n == rev)
                num1=true;
           m=sqrt(n);
           if(m==(int) m)
           {
                m=(int) m;
                num=m;
                n=num;
                rev=0;
                do
                {
                    digit = num%10;
                    rev = (rev*10) + digit;
                    num = num/10;
                }while (num!=0);
                if(n==rev)
                    num2=true;
           }
            if(num1 && num2)
                count++;
            //cout<<num1<<" "<<num2<<endl;
        }
        printf("Case #%d: %d\n",i,count);
    }

}
