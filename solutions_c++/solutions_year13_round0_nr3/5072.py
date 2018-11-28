#include<iostream>
#include<cmath>
#include<cstdio>
using namespace std;


int arr[100]={0, 1, 2, 3, 11, 22, 101, 111, 121, 202, 212, 1001, 1111, 2002, 10001, 10101, 10201, 11011, 11111, 11211, 20002, 20102, 100001, 101101, 110011, 111111, 200002, 1000001, 1001001, 1002001,1010101,1011101, 1012101,1100011,1101011,1102011,1110111,1111111,2000002,2001002};
int main()
{
     freopen("C-small-attempt2.in","r", stdin);
     freopen("output.in","w", stdout);
    int t;
    cin>>t;
    int c=t;
    while(t--)
    {
        long long x,y;
        cin>>x>>y;
        float k=sqrt(x);
        float l=sqrt(y);
        int cnt=0;
        for(int i=0;i<40;i++)
        {
            if(arr[i]>=k&&arr[i]<=l)
            cnt++;
        }

        printf("Case #%d: ",c-t);
        printf("%d\n",cnt);

    }
}




