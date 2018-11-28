#include <iostream>
#include <fstream>
using namespace std;

int main()
{
    ifstream f1("A-large.in");
    ofstream f2("2.out");
    int T;
    long long n=0;
    long long z=0;
    int a[10]={0};
    int x=0;
    int count;
    int y;
    f1>>T;
    for(int i=0;i<T;i++)
    {
        f1>>n;
        z=0;
        x=0;
        count=0;
        for(y=0;y<10;y++)
        {
            a[y]=0;
        }
        for(y=1;y<1000000;y++)
        {
            z=y*n;
            while(z)
            {
                x=z-(z/10)*10;
                a[x]=1;
                z=z/10;
            }
            count=0;
            for(int k=0;k<10;k++)
            {
                count+=a[k];
            }
            if(count==10)
            {
                break;
            }
        }
        if(y==1000000)
        {
            f2<<"Case #"<<i+1<<": "<<"INSOMNIA"<<endl;
        }
        else
        {
            f2<<"Case #"<<i+1<<": "<<n*y<<endl;
        }
    }
    return 0;
}
