#include<iostream>
#include<cstdlib>
#include<fstream>
using namespace std;
int main()
{
    fstream f1,f2;
    int a[17],b[4][4],c[4][4],i,j,flag=0,flag1,n1,n2;
    for(i=0;i<17;i++)
        a[i]=0;
    f1.open("A-small-attempt0.in",ios::in);
    f2.open("op2.txt",ios::out);
    f1>>n1;
    // cout<<n1;
    for(int k=0;k<n1;k++)
    {
        int n3;
        f1>>n3;
        // cout<<n3;
        int n4,l,m;
        for(int l=0;l<4;l++)
        {
            for(int m=0;m<4;m++)
            {
                f1>>n4;
                b[l][m]=n4;
                if(n3==(l+1))
                    a[n4]=1;
                // cout<<n4;
            }
        }
        int n5;
        f1>>n5;
        // cout<<n5;
        for(int l=0;l<4;l++)
        {
            for(int m=0;m<4;m++)
            {
                f1>>n4;
                c[l][m]=n4;
                if(n5==(l+1))
                {
                    // cout<<"\n Value"<<n4;
                    if (a[n4]==1)
                       {
                            flag++;
                            flag1=n4;
                       }
                }
                // cout<<n4;
            }
        }
        f2<<"Case #"<<k+1<<": ";
        if(flag==1)
            f2<<flag1;
        else if (flag==0)
            f2<<"Volunteer cheated!";
        else
            f2<<"Bad magician!";
            f2<<endl;
        flag=0;
        for(i=0;i<17;i++)
        a[i]=0;
    }
    f1.close();
    return 0;
}
