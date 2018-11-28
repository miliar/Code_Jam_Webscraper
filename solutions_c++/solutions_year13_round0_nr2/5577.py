#include<iostream>
#include<fstream>

using namespace std;

int main()
{
    int t,a[10][10],c,n,m,i,j,flag,x,rsum,csum;
	ifstream in("B-small-attempt0.in");
	ofstream out("out.txt");
    in>>t;
    for(c=1;c<=t;c++)
    {
        flag=0;
        in>>n>>m;
        for(i=0;i<n;i++)
        for(j=0;j<m;j++)
        in>>a[i][j];
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
			{flag++;break;}
        }
        if(flag)
			out<<"\nCase #"<<c<<": NO";
        else
            out<<"\nCase #"<<c<<": YES";

    }
    return 0;
}