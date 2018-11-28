//divesh uttamchandani
#include<iostream>
#include<vector>
#include<conio.h>

using namespace std;


int main()
{
    int T,i;
    cin>>T;

    for(i=0;i<T;i++)
    {
        //Test case i+1
        int n=0;
        char ch;
        cin>>n;
        int j=0;
        int sum=0,nop=0;
        char t[n+1];
        cin>>t;

        for(j=0;j<=n;j++)
        {
        ch=t[j];
        if(ch>='0' && ch<='9')
         {
             int z=(int)(ch-'0');
             if(sum>=j && z!=0)
             {
                 sum+=z;
             }
             if(sum<j && z!=0)
             {
                 nop+=j-sum;
                 sum+=nop;
                 sum+=z;
             }
         }
        }
    cout<<"Case #"<<i+1<<": "<<nop<<"\n";
    }
}
