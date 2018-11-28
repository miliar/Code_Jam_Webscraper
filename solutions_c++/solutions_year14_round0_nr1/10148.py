#include<iostream>
using namespace std;
int main()
{
    int t, k, k1, a[4][4], b[4][4], i, j, y, q=0, s;
    cin>>t;
    for(i=1;i<=t;i++)
    {
        cin>>k;
        for(j=0;j<4;j++)
        {
            for(y=0;y<4;y++)
            cin>>a[j][y];
        }
        cin>>k1;
        for(j=0;j<4;j++)
        {
            for(y=0;y<4;y++)
            cin>>b[j][y];
        }
        for(j=0;j<4;j++)
        {
            for(y=0;y<4;y++)
            if(a[k-1][j]==b[k1-1][y])
            {
                //cout<<a[k][j]<<"   "<<b[k1][y]<<endl;
                q++;
                s=a[k-1][j];
            }
                
        }
        //cout<<"!!!! "<<q<<endl;
        if(q==1)cout<<"Case #"<<i<<": "<<s<<endl;
        if(q>1)cout<<"Case #"<<i<<": Bad magician!"<<endl;
        if(q==0)cout<<"Case #"<<i<<": Volunteer cheated!"<<endl;
        q=0;
        s=0;
    }
    
return 0;
}
