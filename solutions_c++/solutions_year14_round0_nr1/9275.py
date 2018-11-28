#include<iostream>
#include<cstdio>
using namespace std;

int main()
{
    int t,r1,r2,a[5][5],b[5][5],i,j,n,temp[5],k=0;
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    cin>>t;
    n=0;
    while(t--)
    {
        n++;
        k=0;
        cin>>r1;
        for(i=0;i<4;i++)
            for(j=0;j<4;j++)
                cin>>a[i][j];
        cin>>r2;
        for(i=0;i<4;i++)
            for(j=0;j<4;j++)
                cin>>b[i][j];

        for(i=0;i<4;i++)
            for(j=0;j<4;j++)
                if(a[r1-1][i]==b[r2-1][j])
                    temp[k++]=a[r1-1][i];

        if(k>1)cout<<"Case #"<<n<<": Bad magician!"<<endl;
            else if(k==0)cout<<"Case #"<<n<<": Volunteer cheated!"<<endl;
                else cout<<"Case #"<<n<<": "<<temp[0]<<endl;
    }
    return 0;
}
