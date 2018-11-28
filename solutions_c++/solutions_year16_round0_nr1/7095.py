#include <iostream>
#include <cstdio>
using namespace std;

int main()
{
    int t;
    scanf("%d",&t);
    for (int t1(1);t1<=t;t1++)
    {
       long long int n;
        scanf("%lld",&n);
        if (n==0){cout << "Case #" << t1<<": "<<"INSOMNIA" << endl;continue;}
        int arr[10]={0};int result(0);int c(1);
        for (;true;c++)
        {
            int temp=n*c;
            for (;temp!=0;temp=temp/10)arr[temp%10]=1;
            result=0;
            for (int c1(0);c1<=9;c1++)if (arr[c1]==1)result++;
            if (result==10)break;
        }
        cout << "Case #" <<t1<<": " <<  n*c<< endl;
    }
    return 0;
}
