#include<iostream>
#include<fstream>
using namespace std;
int arrf[4],arrs[4];
int main()
{
    ifstream fin ("A-small-attempt1.in",ios::in);
    ofstream fout;
    fout.open ("A-small.txt");
    int t,f,s,i,j,k,tmp,count,num;
    fin>>t;
    int x=1;
    while(x<=t)
    {
        count=0;
        fin>>f;
        for(i=0;i<4;i++)
            for(j=0;j<4;j++)
                if(i==f-1)
                    fin>>arrf[j];
                else
                    fin>>tmp;
        fin>>s;
        for(i=0;i<4;i++)
            for(j=0;j<4;j++)
                if(i==s-1)
                {
                    fin>>arrs[j];
                    for(k=0;k<4;k++)
                        if(arrs[j]==arrf[k])
                        {
                            count++;
                            num=arrf[k];
                            break;
                        }
                }
                else
                    fin>>tmp;
        switch(count)
        {
            case 0: fout<<"Case #"<<x<<": Volunteer cheated!"<<endl; break;
            case 1: fout<<"Case #"<<x<<": "<<num<<endl; break;
            default : fout<<"Case #"<<x<<": Bad magician!"<<endl; break;

        }
        x++;
    }
    return 0;

}
