

#include<iostream>
#include<fstream>

using namespace std;

int main()
{
    int t,a[10][10],c,n,m,i,j,f,x,rsum,csum;
	ifstream inp("test.in");
	ofstream outp("output.out");
    inp>>t;
    for(c=1;c<=t;c++)
    {
        f=0;
        inp>>n>>m;
        for(i=0;i<n;i++)
        for(j=0;j<m;j++)
        inp>>a[i][j];
        for(i=0;i<n;i++)
        for(j=0;j<m;j++)
        if(a[i][j]==1)
        {
            rsum=0;csum=0;
            for(x=0;x<n;x++)
            rsum+=a[x][j];
            for(x=0;x<m;x++)
            csum+=a[i][x];
            if(rsum!=n&&csum!=m)
			{f++;
			break;}
        }
        if(f)
			outp<<"\nCase #"<<c<<": NO";
        else
            outp<<"\nCase #"<<c<<": YES";

    }
    return 0;
}