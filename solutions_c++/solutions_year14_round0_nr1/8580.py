#include <iostream>
#include <fstream>
using namespace std;
int main()
{
    ifstream fin("A-small-attempt0.in");
    ofstream fout("file3.out");
    int T,i,r1,r2,j,k,m,n,z,y;
    int arr1[4][4],arr2[4][4],arr11[4],arr22[4];
    fin>>T;
    for (k=1;k<=T;k++)
    {
        z=0;
        fin>>r1;
        for(i=0;i<4;i++)
            for(j=0;j<4;j++)
            {
                fin>>arr1[i][j];
                if(i==r1-1)
                    arr11[j]=arr1[i][j];
            }
            fin>>r2;
        for(i=0;i<4;i++)
            for(j=0;j<4;j++)
            {
                fin>>arr2[i][j];
                if(i==r2-1)
                    arr22[j]=arr2[i][j];
            }
        for(m=0;m<4;m++)
            for(n=0;n<4;n++)

             if(arr11[m]==arr22[n])
             {
                 z++; y=m;
             }
        fout<<"Case #"<<k<<": ";
        if(z==1)
         fout<<arr11[y]<<endl;
         else if(z>1)
         fout<<"Bad magician!"<<endl;
         else
         fout<<"Volunteer cheated!"<<endl;
    }
    return 0;
}
