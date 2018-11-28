#include <bits/stdc++.h>
#define pf printf
#define sf scanf
#define SIZE 1005

using namespace std;

int arr[SIZE+1];
int process[SIZE+1];
int main()
{
    freopen("in.txt" , "r" , stdin);
    freopen("out.txt" , "w" , stdout);
    int tc;
    sf("%d",&tc);
    for (int i = 1 ; i<=tc; i++)
    {
        int noOfDigit=0;
        int res = 0;
        sf("%d",&noOfDigit);
        for(int j = 0 ; j<=noOfDigit ; j++)
        {
            sf("%1d",&arr[j]);
            if(j==1) process[j] = arr[0];
            else process[j] = process[j-1] + arr[j-1];
        }
        for (int j = 1 ; j<=noOfDigit ; j++)
        {
            int tmpRes = process[j];
            if (j>tmpRes){
                    if(res < (j-tmpRes)) res = (j-tmpRes);
            }
        }
        pf("Case #%d: %d\n", i,res);
    }
    return 0;
}
