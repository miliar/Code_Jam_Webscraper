#include<iostream>
#include<fstream>
using namespace std;
int main()
{
    ifstream input("input.txt");

    ofstream myfile;
    myfile.open ("outputttt.txt");


    int t;
    input>>t;
    int pop;
    while(t--)
    {

        int m,n;
        input>>n>>m;
        int a[101][101];
        int b[101][101];
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<m;j++)
            {b[i][j]=100;
            //cout<<b[i][j]<<endl;
            }
        }
        int rmax[101];
        int cmax[101];
        int max=0;
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<m;j++)
            {
                input>>a[i][j];
                if(a[i][j]>max)
                max=a[i][j];
            }
            rmax[i]=max;
            max=0;
        }

        max=0;
         for(int i=0;i<m;i++)
        {
            for(int j=0;j<n;j++)
            {
                if(a[j][i]>max)
                max=a[j][i];
            }
            cmax[i]=max;
            max=0;
        }
        for(int i=0;i<n;i++)
        {
        for(int j=0;j<m;j++)
        {
            if(b[i][j]>rmax[i])
            b[i][j]=rmax[i];
        }
        }
        cout<<endl;

      /*  for(int i=0;i<n;i++)
        cout<<rmax[i]<<endl;

cout<<endl;
        for(int k=0;k<m;k++)
        cout<<cmax[k]<<endl;
        */
        for(int i=0;i<m;i++)
        {
        for(int j=0;j<n;j++)
        {
            if(b[j][i]>cmax[i])
            b[j][i]=cmax[i];
        }
        }
        int flag=0;
        for(int i=0;i<n;i++)
        {
        for(int j=0;j<m;j++)
        {

            if(a[i][j]!=b[i][j])
            {
            flag=1;
            break;
            }
        }
        cout<<endl;
        }
        if(flag==0)
        myfile<<"Case #"<<(++pop)<<": YES"<<endl;
        else
        myfile<<"Case #"<<(++pop)<<": NO"<<endl;





    }
}
