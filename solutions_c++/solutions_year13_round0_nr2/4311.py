#include <iostream>
#include <fstream>
using namespace std;

int main()
{
    int t;
    cin>>t;
    ofstream cout("res.txt");
    for(int tt=1;tt<=t;tt++)
    {
        cout<<"Case #"<<tt<<": ";
        bool pos=true;
        bool br=false;
        int a,b;
        cin>>a>>b;
        int mat[a][b];
        for(int i=0;i<a;i++)
            for(int j=0;j<b;j++)
                cin>>mat[i][j];
        for(int i=0;i<a;i++)
        {
            for(int j=0;j<b;j++) //mat[i][j]
            {
                bool row=true,col=true;
                for(int ii=0;ii<a;ii++)
                {
                    if(mat[i][j]<mat[ii][j])
                    {
                        row=false;
                        break;
                    }
                }

                for(int ii=0;ii<b;ii++)
                {
                    if(mat[i][j]<mat[i][ii])
                    {
                        col=false;
                        break;
                    }
                }
                pos=pos&(row||col);
            }

            if(!pos)
            {
                cout<<"NO"<<endl;
                br=true;
                break;
            }
        }
        if(!br)
            cout<<"YES"<<endl;
    }
    return 0;
}
