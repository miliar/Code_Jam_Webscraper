#include<iostream>
#include<fstream>

using namespace std;

int main()
{
    int ans[100],ar[2][4],i,j,t,k,r;
    ifstream fin;
	ofstream fout;

	fin.open("A-small-attempt3.in",ios::in);
	fout.open("A-small-attempt3.out",ios::out);

    fin>>t;
    for(k=0;k<t;k++)
    {
        fin>>r;
        for(i=0;i<4*(r-1);i++)
            fin>>j;
        for(i=0;i<4;i++)
            fin>>ar[0][i];
        for(i=0;i<4*(4-r);i++)
            fin>>j;
            
        fin>>r;
        for(i=0;i<4*(r-1);i++)
            fin>>j;
        for(i=0;i<4;i++)
            fin>>ar[1][i];
        for(i=0;i<4*(4-r);i++)
            fin>>j;
        
        ans[k]=0;
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                if(ar[0][i]==ar[1][j])
                {
                    if(ans[k]==0)
                        ans[k]=ar[0][i];
                    else
                        ans[k]=-1;
                        
                    break;
                }
            }
        }
    }
    for(k=0;k<t;k++)
    {
        fout<<"Case #"<<k+1<<": ";
        if(ans[k]>0)
            fout<<ans[k]<<endl;
        else if(!ans[k])
            fout<<"Volunteer cheated!"<<endl;
        else
            fout<<"Bad magician!"<<endl;
    }
        
	fin.close();
	fout.close();
   return 0;
}
