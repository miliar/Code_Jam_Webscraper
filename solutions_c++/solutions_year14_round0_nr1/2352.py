#include<iostream>
#include<stdio.h>
#include<cstring>
using namespace std;
int main(void)
{
    int n, c=1;
    freopen("output.txt","w",stdout);
    freopen("A-small-attempt0.in","r",stdin);
    cin>>n;
    while(c<=n)
    {
        int a[4][4], b[4][4], r1, r2, cnt=0, v, i, j;
        cin>>r1;
        for(i=0;i<4;i++)
            for(j=0;j<4;j++)
                cin>>a[i][j];
        cin>>r2;
        for(i=0;i<4;i++)
            for(j=0;j<4;j++)
                cin>>b[i][j];
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                if(a[r1-1][i]==b[r2-1][j])
                {
                    //cout<<a[r1-1][i]<<endl;
                    v=a[r1-1][i];
                    cnt++;
                }
            }
        }
        cout<<"Case #"<<c++<<": ";
        if(cnt==0)  cout<<"Volunteer cheated!";
        else if(cnt>1)  cout<<"Bad magician!";
        else    cout<<v;
        cout<<endl;
    }
    fclose(stdout);
    fclose(stdin);
}
