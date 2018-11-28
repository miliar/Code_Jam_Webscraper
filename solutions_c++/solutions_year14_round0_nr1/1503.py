#include<fstream>
#include<iostream>
#include<cstdio>
using namespace std;
int t,x,y,c,s,gar;
int a[5];
int main()
{
    freopen("asmall.in","r",stdin);
    freopen("asmall.out","w",stdout);
    cin>>t;
    for(int i=1;i<=t;i++)
    {
        c=0;
        cin>>x;
        for(int j=1;j<=4;j++)
        {
            if(j==x)
                for(int k=1;k<=4;k++)
                    cin>>a[k];
            else
                for(int k=1;k<=4;k++)
                    cin>>gar;
        }
        cin>>y;
        for(int j=1;j<=4;j++)
        {
            if(j==y)
            {
                for(int k=1;k<=4;k++)
                {
                    cin>>x;
                    for(int l=1;l<=4;l++)
                        if(a[l]==x)
                        {
                            c++;
                            s=x;
                        }
                }
            }
            else
                for(int k=1;k<=4;k++)
                    cin>>gar;
        }
        printf("Case #%d: ",i);
        if(c==0)
            cout<<"Volunteer cheated!";
        else if(c>1)
            cout<<"Bad magician!";
        else
            cout<<s;
        cout<<endl;
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
