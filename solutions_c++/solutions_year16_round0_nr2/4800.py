#include <iostream>
#include <fstream>
#include <set>

using namespace std;

int getdonesize(string ss)
{
    int n;
    n=ss.size();
    for (int jj=n-1;jj>=0;jj--)
        if (ss[jj]=='-')
            return jj;
    return -1;
}

int main()
{
    int inputnumber,ii,n,totalcopy;
    int total,nn,top;
    ifstream fin("input");
    ofstream fout("output");
    string ss;
    bool sleep;
    fin>>inputnumber;
    for (int ii=1;ii<=inputnumber;ii++)
    {
        total=0;
        fin>>ss;
        top=getdonesize(ss);
        while (top>=0)
        {
//            cout<<ss<<endl;
            if (ss[0]=='-')
            {
                string newss;
                for (int i=top;i>=0;i--)
                    {
                        if (ss[i]=='+')
                            newss+='-';
                        else
                            newss+='+';
                    }
                for (int i=top+1;i<ss.size();i++)
                    newss+=ss[i];
                ss=newss;
                total++;
            }
            else
            {
                int j=0;
                while (ss[j]=='+')
                {
                    ss[j]='-';
                    j++;
                }
                total++;
            }
            top=getdonesize(ss);
        }
        fout<<"Case #"<<ii<<": "<<total<<endl;
    }
    return 0;
}