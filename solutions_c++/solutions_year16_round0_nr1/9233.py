#include<iostream>
#include<fstream>
using namespace std;
int main()
{
    freopen("largea.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    scanf("%d",&t);
    for(int in =1; in <=t;in++)
    {
        long long n;
        scanf("%lld",&n);
        printf("Case #%d: ",in);
        if(n==0){printf("INSOMNIA\n");continue;}

        int a[10] = {0};
        long long temp = n;
        int j =2;
        while(1)
        {
            long long ans = temp;
            bool f = false;

            while(temp>0)
            {
                a[temp%10]++;
                temp/=10;
            }
            for(int i=0;i<10;i++)if(!a[i])f = true;
            if(f){
                temp = j*n;
                j++;
            }
            else {
                printf("%lld\n", ans);
                break;
            }
        }

    }
}
