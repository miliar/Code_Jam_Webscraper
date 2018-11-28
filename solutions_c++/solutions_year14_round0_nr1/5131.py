#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
    int t,i,j,k,n,r,v,cnt;
    int a[5][5];cin>>t;v=t;
    while(t--)
    {
        int m[20]={0};
        for(k=0;k<2;k++)
        {
            cin>>n;cnt=0;
            for(i=1;i<=4;i++)
            {
                for(j=1;j<=4;j++)
                cin>>a[i][j];
            }
            for(i=1;i<=4;i++)
            m[a[n][i]]++;
        }
        for(i=1;i<=16;i++)
        if(m[i]==2) {cnt++;r=i;}
        if(cnt==1) cout<<"Case #"<<v-t<<": "<<r<<endl;
        else if(cnt>1) cout<<"Case #"<<v-t<<": Bad magician!"<<endl;
        else if(cnt==0) cout<<"Case #"<<v-t<<": Volunteer cheated!"<<endl;
    }
    return 0;
}
