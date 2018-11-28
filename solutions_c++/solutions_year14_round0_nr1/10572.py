#include<iostream>
using namespace std;
int main()
{
    int t,a,b,aa[4][4],bb[4][4],cnt,out;
    cin>>t;
   for(int x=1;x<=t;x++)
    {
        cnt=0;
        cin>>a;
        a--;
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
            cin>>aa[i][j];
            cin>>b;
            b--;
            for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
            cin>>bb[i][j];

            for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
           if(aa[a][i]==bb[b][j])
           {cnt++;
           out=aa[a][i];
           }
           if(cnt==1)
            cout<<"Case #"<<x<<": "<<out<<endl;
           else if(cnt>1)
            cout<<"Case #"<<x<<": Bad magician!\n";
           else
            cout<<"Case #"<<x<<": Volunteer cheated!\n";
    }
}
