#include <iostream>
#include <algorithm>
#include<stdio.h>
using namespace std;
int main()
{
    freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
    long long tc, N, i=1, hold=0;
    bool flag=false;
    cin>>tc;
    for(int x=0; x<tc; x++)
    {
        cin>>N;
        hold=0;
        flag=false;
        int arr[10]= {0};
        i=0;
        int temp=0, temp2=0;
        if(N>0)
        {
            while(flag!=true)
            {

                temp2=N;
                temp2*=i;
                temp=temp2;
                while(temp>0)
                {
                    int number;
                    number=temp%10;
                    arr[number]++;
                    temp=temp/10;
                }
                hold=temp2;
                for(int j=0; j<=9; j++)
                {
                    if(arr[j]==0)
                    {
                        flag=false;
                        break;
                    }
                    else
                        flag=true;
                }
                i++;
            }
            cout<<"Case #"<<x+1<<": "<<hold<<"\n";
        }
        else
            cout<<"Case #"<<x+1<<": INSOMNIA\n";
    }
    return 0;
}
