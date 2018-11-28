#include<iostream>
using namespace std;
int main()
{
        freopen("input.txt","r",stdin);
        freopen("output.txt","w",stdout);
        int testcase,temp,n,m,i,j,k;
        bool check1,check2;
        int mat[10][10];
        cin>>testcase;
        temp=testcase;
        while(testcase>0)
        {
           cin>>n;
           cin>>m;
           check1=check2=true;
        for(i=0;i<n;i++)
        {
            for(j=0;j<m;j++)
            cin>>mat[i][j];
        }
        /*for(i=0;i<n;i++)
        {
            {for(j=0;j<m;j++)
            cout<<mat[i][j];}
            cout<<endl;
        }*/

         for(i=0;i<n;i++)
        {
            for(j=0;j<m;j++)
         {
             check1=check2=true;
         if(mat[i][j]==1)
         {
             //cout<<"i j"<<i<<" "<<j<<endl;
            for(k=0;k<m;k++)
            {
                if(mat[i][k]==2)
                {
                    check1=false;
                    break;
                }
            }
            for(k=0;k<n;k++)
            {
                if(mat[k][j]==2)
                {
                    check2=false;
                    break;
                }
            }
         if((check1==false)&&(check2==false))
         {
             cout<<"Case #"<<temp-testcase+1<<": NO"<<endl;
             goto x;
         }

         }

        }

        }
        cout<<"Case #"<<temp-testcase+1<<": YES"<<endl;




x:
        testcase--;
        }


        return 0;
}
