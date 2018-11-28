#include<iostream>
#include<cstdio>
using namespace std;
int GetLastNum(int n);
int main()
{
        freopen("A-large.in","r",stdin);
        freopen("output.out","w",stdout);
        int T,N,rnd=0,lastNum;
        cin>>T;
        while(T--)
        {
                ++rnd;
                cin>>N;
                lastNum=GetLastNum(N);
                printf("Case #%d: ",rnd);
                if(lastNum==0)
                        printf("INSOMNIA\n");
                else
                        printf("%d\n",lastNum);
        }
        return 0;
}

int GetLastNum(int n)
{
        int numCnt[10]={0};
        if(n==0)
                return 0;
        else{
                for(int i=0;;i+=n)
                {
                        int j=i;
                        while(j!=0)
                        {
                                ++numCnt[j%10];
                                j/=10;
                        }
                        int k;
                        for(k=0;k!=10;++k)
                                if(numCnt[k]==0)
                                break;
                        if(k==10)
                                return i;
                }
        }
}
