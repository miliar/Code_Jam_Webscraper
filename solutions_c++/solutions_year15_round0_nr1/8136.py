#include <stdio.h>
#include <math.h>
#include <limits.h>
#include<iostream>
#include<fstream>
using namespace std;
int main()
{
    int t,f=0;
    ofstream pno;
    pno.open("standing_ovation.txt");
    scanf("%d",&t);
    while(t--)
    {
        f++;
        int n;
        //scanf("%d",&n);
        cin>>n;
        char str[n+5];
        cin>>str;
        int i,count=0,sum=0;
        for(i=0;i<=n;i++)
        {
            if(str[i]!='0')
            {
                if(i<=sum)
                    sum+=(str[i]-'0');
                else{
                    count+=(i-sum);
                    sum=i;
                    sum+=(str[i]-'0');
                }
                if(sum>n)
                    break;
            }
            //printf("%d %d\n",sum,count);
        }
        //printf("Case #%d: %d\n",f,count);
        pno<<"Case #"<<f<<": "<<count<<endl;
    }
    pno.close();
    return 0;
}
