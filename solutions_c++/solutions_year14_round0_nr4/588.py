#include<iostream>
#include<cmath>
#include<fstream>
#include<algorithm>

using namespace std;

int deceitful(float* N, float* K, int n)
{
    int D=n,i,j=0;
    for(i=0;i<n && j<=n-1;i++)
    {
        if (N[i]<K[j])
            D--;
        else
            j++;
    }
    return D;
}

int undeceitful(float* N, float* K, int n)
{
    int UD=0,i,j=n-1;
    for(i=n-1;i>=0 && j>=0;i--)
    {
        if (N[i]>K[j])
            UD++;
        else
            j--;
    }
    return UD;
}

int main()
{
    int T,x,n,i,j,D,UD;
    fstream input;
    fstream output;
    input.open("D-large.txt",ios::in);
    output.open("D-large-out.txt",ios::out);
    input>>T;
    for (x=1;x<=T;x++)
    {
        input>>n;
        float N[n],K[n];
        for (i=0;i<n;i++)
        {
            input>>N[i];
        }
        for (i=0;i<n;i++)
        {
            input>>K[i];
        }
        sort(N, N + n);
        sort(K, K + n);
        if (n==1)
        {
            if(N[0]<K[0])
            {
                D=0;
                UD=0;
            }
            else
            {
                D=1;
                UD=1;
            }
        }
        else
        {
            D = deceitful(N,K,n);
            UD = undeceitful(N,K,n);
        }
        output<<"Case #"<<x<<": "<<D<<" "<<UD<<endl;
    }
    input.close();
    output.close();
    return 0;
}
