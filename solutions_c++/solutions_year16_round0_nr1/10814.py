#include<iostream>
#include<stdio.h>
using namespace std;

char a[10];


int binarySearch(int low,int high,int value);
int main()
{
    freopen("A-large.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int T,N,count;
    cin>>T;
    for(int caseNo=1;caseNo<=T;caseNo++)
    {
        for(int i=0;i<10;i++)
            a[i]=0;
        count = 0;
        cin>>N;
        if(N==0)
        {
            cout<<"Case #"<<caseNo<<": INSOMNIA"<<endl;
            continue;
        }
        int i=1,temp,rem,pos;
        while(count != 10)
        {
            temp=N*i;
            do
            {
                rem = temp%10;
                temp /= 10;
                pos = binarySearch(0,9,rem);
                if(a[pos]==0)
                {
                    a[pos] = 1;
                    count++;
                }
            }while(temp != 0);
            i++;
        }
        cout<<"Case #"<<caseNo<<": "<<N*(i-1)<<endl;
    }
}

int binarySearch(int low,int high,int value)
{
    int mid = (low + high) / 2;
    if(high < low)
        return -1;
    if(value == mid)
        return mid;
    else if(value < mid)
        binarySearch(low,mid-1,value);
    else
        binarySearch(mid+1,high,value);
}
