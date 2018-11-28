#include<fstream>
using namespace std;

int main()
{
    ofstream fout;
    ifstream fin;
    fin.open("A-small-attempt0.in");
    fout.open("output.txt");
    int T,data,row_old[16],row_new[16],count,r1,r2,i,j,k,ans;
    fin>>T;
    for(k=1;k<=T;k++)
    {
        count=0;
        ans=0;
        fin>>r1;
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                fin>>data;
                row_old[data-1]=i;
            }
        }
        fin>>r2;
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                fin>>data;
                row_new[data-1]=i;
            }
        }
        for(i=0;i<16;i++)
        {
            if(row_old[i]==r1-1 && row_new[i]==r2-1)
            {
                count++;
                ans=i+1;
            }
        }
        if(count==1)
        fout<<"Case #"<<k<<": "<<ans<<endl;
        else if(count>1)
        fout<<"Case #"<<k<<": Bad magician!"<<endl;
        else
        fout<<"Case #"<<k<<": Volunteer cheated!"<<endl;
    }
    return 0;
}



