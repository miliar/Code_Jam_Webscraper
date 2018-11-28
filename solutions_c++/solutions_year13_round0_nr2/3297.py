#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    ifstream in("googlecodejam.in");
    ofstream out("googlecodejam.out");
    int t,n,m;
    int r,c;
    int** a;
    in>>t;
    for(int i=0;i<t;i++)
    {
        in>>n;
        in>>m;
        a=new int*[n];
        for(int j=0;j<n;j++) a[j] = new int[m];
        for(int j=0;j<n;j++)
        {
            for(int k=0;k<m;k++)
            {
                in>>a[j][k];
                //cout<<a[j][k]<<" ";
            }
            //cout<<endl;
        }
        for(int j=0;j<n;j++)
        {
            for(int k=0;k<m;k++)
            {
                r=0;
                c=0;
                for(int l=0;l<m;l++)
                {
                    //cout<<"ar "<<a[j][k]<<" - "<<a[j][l]<<endl;
                    if(a[j][k]<a[j][l]) {r=1;goto end2;}
                }
                end2:;
                for(int l=0;l<n;l++)
                {
                    //cout<<"ac "<<a[j][k]<<" - "<<a[l][k]<<endl;
                    if(a[j][k]<a[l][k]) {c=1;goto end3;}
                }
                end3:;
                //cout<<r<<" x "<<c<<endl;
                if((r==1)&&(c==1)) {out<<"Case #"<<i+1<<": NO"<<endl;goto end;}
            }
        }
        out<<"Case #"<<i+1<<": YES"<<endl;
        end:;
        //cout<<endl;
    }
    return 0;
}
