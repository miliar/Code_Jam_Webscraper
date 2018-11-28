#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t=1,T;
    long long i,j,n,m;
    int a[15];
    ifstream infile;
    infile.open("A-large.in");
    ofstream outfile;
    outfile.open("output.txt");
    infile>>T;
    while(T--)
    {
        infile>>n;
        if(n==0) outfile<<"Case #"<<t++<<": "<<"INSOMNIA"<<endl;
        memset(a,0,sizeof(a));
        for(i=1;i<100000;i++)
        {
            m=i*n;
            while(m>0)
            {
                int k=m%10;
                a[k]=1;
                m=m/10;
            }
            int sum=0;
            for(j=0;j<10;j++) sum=sum+a[j];
            if(sum==10)
            {
                outfile<<"Case #"<<t++<<": "<<i*n<<endl;
                break;
            }
        }
    }
    infile.close();
    outfile.close();
}
