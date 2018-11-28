#include <bits/stdc++.h>
using namespace std;
int main()
{
    ifstream fin("input.in");
	ofstream fout("output.out");
	int i,T;
    fin>>T;
    int r[T],t[T];
    for(i=0;i<T;i++)
    {
        fin>>r[i];
        fin>>t[i];
    }
    int sum,n,j;
    for(i=0;i<T;i++)
    {
        sum=0;n=0;
        for(j=0;j<1000;j++)
        {
            sum=sum+(r[i]+j*2+1)*(r[i]+j*2+1)-(r[i]+j*2)*(r[i]+j*2);
            if(sum>t[i])
                break;
            n=n+1;
        }
        fout<<"Case #"<<i+1<<": "<<n<<"\n";
    }
}
