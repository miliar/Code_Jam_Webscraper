using namespace std;
#include<iostream>
#include<cstdio>

    int main()
    {
        int n,test=0;
        cin>>n;
        while(n--)
        {
            test++;
            int m,n,count=0;
            cin>>m>>n;
            if(1>=m && 1<=n)count++;
            if(4>=m && 4<=n)count++;
            if(9>=m && 9<=n)count++;
            if(121>=m && 121<=n)count++;
            if(484>=m && 484<=n)count++;
            printf("Case #%d: %d\n",test,count);
        }
        return 0 ;
    }
