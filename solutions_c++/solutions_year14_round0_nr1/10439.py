#include <iostream>
#include <bits/stdc++.h>
#include <fstream>
#include <vector>
using namespace std;
int main()
{
    freopen("TT.txt","r",stdin);
    freopen("T.txt","w",stdout);
    int t;
    cin>>t;
    for (int i=0; i<t; i++)
    {
    int a[4][4];
    int aa[4][4];
    int res[4];
    int res1[4];
    int a1,a2;
    //----------------------------
        cin>>a1;
        for (int i=0; i<4; i++)
        {

            for (int j=0; j<4; j++)
            {
                cin>>a[i][j];
            }
        }
        cin>>a2;
        for (int i=0; i<4; i++)
        {
            for (int j=0; j<4; j++)
            {
                cin>>aa[i][j];
            }
        }
//------------------------------------------
        for (int j=0; j<4; j++)
        {

            res[j]=a[a1-1][j];
        }

        for (int j=0; j<4; j++)
        {
            res1[j]=aa[a2-1][j];
        }
        //----------------------------
        int co=0;
        int ans=0;
      //  sort(res,res+4);
      //  sort(res1,res1+4);
        for (int i=0; i<4; i++)
        {
            for (int j=0;j<4;j++){
            if (res[i]==res1[j])
            {
                co++;
                ans=res1[j];
            }
            }
        }
        if (co==1)
        {
            cout<<"Case #"<<i+1<<": "<<ans<<endl;
        }
        else if (co>1)
        {
            cout<<"Case #"<<i+1<<":"<<" Bad magician!"<<endl;
        }
        else if (co==0)
        {
            cout<<"Case #"<<i+1<<":"<<" Volunteer cheated!"<<endl;
        }
        //-------------------------------------------------------------

    }
    return 0;
}
