#include <iostream>
#include <cmath>
#include <stdlib.h>
#include <string.h>
using namespace std;

const int MAX_NUM=1005;
bool arr[MAX_NUM];

bool judge(int num)
{
    int re = num;
    int temp = 0;
    while (num)
    {
        temp *= 10;
        temp += (num%10);
        
        num/=10;
    }
    if (temp==re)
    {
        return true;
    }else{
        return false;
    }
}
void build()
{
    memset(arr, 0, sizeof(arr));
    int i;
    int mx = (int)sqrt(MAX_NUM);
    for(i=1; i<=mx; i++)
    {
        if (judge(i) && judge(i*i))
        {
            arr[i*i] = true;
        }
    }
    int result = 0;
    int T;
    int count = 0;
    int begin, end;
    cin>>T;
    while(T--)
    {
        count++;
        cin>>begin>>end;
        result = 0;
        for (i=begin; i<=end; i++)
        {
            if (arr[i])
            {
                result += 1;
            }
        }
        cout<<"Case #"<<count<<": "<<result<<endl;
    }
}

int main()
{
    build();
    return 0;
}

/*
3
1 4
10 120
100 1000
*/
