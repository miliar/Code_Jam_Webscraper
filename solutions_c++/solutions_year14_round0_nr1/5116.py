#include<iostream>
using namespace std;
int A1[4][4];
int A2[4][4];
int main()
{
    int num;
    cin>>num;
    for(int i=0;i<num;i++)
    {
        int i1,i2,k,l;
        cin >>i1;
        for( k=0;k<4;k++)
            for( l=0;l<4;l++)
                cin >>A1[k][l];
         cin >>i2;
         for( k=0;k<4;k++)
            for(l=0;l<4;l++)
                cin >>A2[k][l];
                int cnt=0;
                int res[4];int v=0;
         for(int m=0;m<4;m++)
         {
             for(int z=0;z<4;z++)
             {
                 if(A1[i1-1][m]==A2[i2-1][z])
                 {
                     res[v]=A1[i1-1][m];
                     A1[i1-1][m]=-78;
                     A2[i2-1][z]=-178;
                     cnt++;
                     v++;
                 }
             }
         }
         if(cnt==0)
         cout<<"Case #"<<i+1<<": Volunteer cheated!"<<endl;
         else if(cnt>1)
         cout <<"Case #"<<i+1<<": Bad magician!"<<endl;
         else if(cnt==1)
         cout<<"Case #"<<i+1<<": "<<res[0]<<endl;


    }
    return 0;
}
