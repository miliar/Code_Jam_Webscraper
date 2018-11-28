#include <iostream>
#include <stdio.h>
using namespace std;
void sort(float a[],int n)
{
    float temp;
    for(int i=0; i<n; i++)
    {
        for(int j=i; j<n; j++)
        {
            if(a[i]<a[j])
            {
                temp=a[i];
                a[i]=a[j];
                a[j]=temp;
            }
        }
    }
}
int main()
{
    //freopen("D.in","r",stdin);
    //freopen("D.out","w",stdout);
    int T;
    cin>>T;
    for(int i=0; i<T; i++)
    {
        int N;
        cin>>N;
        float A[N];
        float B[N];
        for(int j=0; j<N; j++)
        {
            cin>>A[j];
        }
        for(int j=0; j<N; j++)
        {
            cin>>B[j];
        }
        sort(A,N);
        sort(B,N);
        int ans1=0;
        int ans2=0;
        int k=N;
        for(int j=N-1; j>=0; j--)
        {
            while(k>0)
            {
                k--;
                if(A[k]>B[j])
                {
                    ans1++;
                    break;
                }
            }
        }
        k=N;
        for(int j=N-1; j>=0; j--)
        {
            while(k>0)
            {
                k--;
                if(A[j]<B[k])
                {
                    ans2++;
                    break;
                }
            }

        }

        cout<<"Case #"<<i+1<<": "<<ans1<<" "<<(N-ans2)<<endl;
    }

    return 0;
}
