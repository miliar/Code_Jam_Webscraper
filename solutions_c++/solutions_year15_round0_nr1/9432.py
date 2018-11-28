#include<iostream>
#include<cstring>
#include<fstream>

using namespace std;
int main()
{
    ifstream fp_in;
    ofstream fp_out;
    fp_in.open("A-large.in", ios::in);
    fp_out.open("out.out", ios::out);
    int t=0,stand=0,add=0,update=0,max_sh=0,audiant=0;
    string audiance;
    fp_in>>t;
    int j=1;
    while(t>0)
    {
        fp_in>>max_sh>>audiance;
        for(int i=0;i<max_sh+1;i++)
        {
            audiant=audiance[i]-48;
            if(audiant==0)
            {
                continue;
            }
                if(i<=stand)
                {
                    stand+=audiant;
                }
                else
                {
                    update=i-stand;
                    add+=update;
                    stand+=update;
                    stand+=audiant;
                }

        }
        fp_out<<"Case #"<<j<<": "<<add<<endl;
        j++;
            stand=0;
            add=0;
            update=0;
            t--;
    }

}

