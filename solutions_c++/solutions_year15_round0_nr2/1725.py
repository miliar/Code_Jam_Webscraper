#include<bits/stdc++.h>
using namespace std;
#define gc getchar
inline void scanint(int &n)
{
    n=0;
    int ch = gc();
    int sign = 1;
    while(ch < '0' || ch > '9')
    {
        if(ch == '-')
        sign=-1;
        ch = gc();
    }
    while(ch >= '0' && ch <= '9')
    {
        n = (n << 3) + (n << 1) + ch - '0', ch = gc();
    }
    n=n*sign;
}
int input_size,input[1003];
int ressize,res_array[1003];
bool solve(int value,int middle)
{
    int difference;
    ressize=0;
    int index;
    for(int i=1;i<=input_size;i++)
    {
        if(input[i]>middle)
        {
            difference=input[i]-middle;
            ressize++;
            res_array[ressize]=difference;
        }
    }
    index=1;
    while(index<=ressize)
    {
        if(res_array[index]>0&&value==0)
        {
            return false;
        }
        if(middle>=res_array[index])
        {
            index++;
            value--;
        }
        else
        {
            res_array[index]-=middle;
            value--;
        }
    }
    return true;
}
int main()
{
    freopen("input.in","r",stdin);
    freopen("outputfile1.txt","w",stdout);
    int t,num;
    int range,P;
    scanint(t);
    for(int cases=1;cases<=t;cases++)
    {
        bool check;
        input_size=0;
        scanint(range);
        for(int i=1; i<=range; i++)
        {
            scanint(num);
            input_size++;
            input[input_size]=num;
        }
        int result=INT_MAX;
        for(int k=0; k<=1000; k++)
        {
            int low=1,high=1000,mid;
            while(low<high)
            {
                mid=low+(high-low)/2;
                check=solve(k,mid);
                if(check==false)
                {
                    low=mid+1;
                }
                else
                {
                    high=mid;
                }
            }
            if(k+low<result)
            {
                result=k+low;
            }
        }
        printf("Case #%d: %d\n",cases,result);
    }
    return 0;
}
