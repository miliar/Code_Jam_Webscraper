#include<cstring>
#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
using namespace std;

int main()
{
   freopen("1312.in","r",stdin);
    freopen("o131.txt","w",stdout);
    int t,k=0,n,rem,total,A[30];
    cin>>t;
    while(t--)
    {
        cin>>n;
        total=0;
        for(int i=0;i<n;++i)
        {
            cin>>A[i];
            total+=A[i];
        }
        rem=total;
        ++k;
        cout<<"Case #"<<k<<": ";
        while(total)
        {
            int maxindex=0,maxval2=0,maxindex2=0;
            for(int i=0;i<n;++i)
            {
                if(A[i]>A[maxindex])
                {
                    maxindex=i;
                }
            }
            A[maxindex]-=1;
            for(int i=0;i<n;++i)
            {
                    if(A[i]>=maxval2)
                    {
                        maxval2=A[i];
                        maxindex2=i;
                    }
            }
            //A[maxindex]-=1;
            A[maxindex2]-=1;
            rem-=2;
            bool valid=true;
            for(int i=0;i<n;++i)
            {
                if(A[i]>(rem/2))
                {
                    valid=false;
                }
            }
            if(valid)
            {
                total-=2;
                printf("%c%c ",maxindex+'A',maxindex2+'A');
            }
            else
            {
                total-=1;
                A[maxindex2]+=1;
                rem+=1;
                printf("%c ",maxindex+'A');
            }
        }
        cout<<endl;
    }
    return 0;
}

