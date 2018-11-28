#include <iostream>
#include <fstream>
using namespace std;

void bubble(int a[],int size);
int main()
{
    ofstream f2("large0.out");
    int T;
    cin>>T;
    int N;
    int a;
    for(int i=0;i<T;i++)
    {
        int height[2501]={0};
        int count=0;
        cin>>N;
        int m[N];
        for(int j=0;j<2*N-1;j++)
        {
            for(int k=0;k<N;k++)
            {
                cin>>a;
                height[a]++;
            }
        }
        for(int j=1;j<2501;j++)
        {
            if(height[j]%2)
            {
                m[count]=j;
                count++;
            }
        }
        bubble(m,N);
        f2<<"Case #"<<i+1<<": ";
        for(int j=0;j<N;j++)
        {
            f2<<m[j]<<" ";
        }
        f2<<endl;
    }
    return 0;
}

void bubble(int a[],int size)
{
    int i,j;
    int tmp;
    bool flag;
    for(i=1;i<size;++i)
    {
        flag=false;
        for(j=0;j<size-i;++j)
            if(a[j+1]<a[j])
            {
                tmp=a[j];
                a[j]=a[j+1];
                a[j+1]=tmp;
                flag=true;
            }
        if(!flag) break;
    }
}
