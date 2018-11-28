# include<iostream>
# include<fstream>
# include<vector>
# include<string>
# include<cmath>
# include<stdio.h>
# include<stdlib.h>
# include<string.h>
# include<stddef.h>

using namespace std;
int ispalin(long long int n)
{
    char buff[100];
    itoa(n,buff,10);
    int len=strlen(buff);
    for(int i=0,j=len-1;i<j;i++,j--)
    {
        if(buff[i]!=buff[j])
            return 0;
    }
    return 1;
}
int main()
{
    long long int t,ind=1;
    cin>>t;
    fstream op;
    op.open("output.txt");
    while(t--)
    {
        int a,b,i,j,c=0;
        cin>>a>>b;
        for(i=a;i<=b;i++)
        {
            long long int sq=sqrt(i);
         //   cout<<"sq root of " << i << "is "<<sq<<endl;
            if(sq*sq==i)
            {
                if(ispalin(i)&&ispalin(sq))
                    c++;
            }

        }
        op<<"Case #"<<ind<<": "<<c<<endl;
        ind++;
    }
}
