#include<iostream>
#include<fstream>
using namespace std;
int main()
{
    fstream fin("input.in",ios::in);
    fstream fout("output.out",ios::out);
    int t;
    fin>>t;
    int smax;
    char space;
    char a[1005];
    int standing,out;
    int x=1;
    while(t--)
    {
        fin>>smax;
        fin.read((char*)&space,sizeof(char));
        fin.read((char*)&a,sizeof(char)*(smax+1));
        //for(int i=0;i<smax+1;++i)
          //  cout<<a[i];
        out=0;
        standing=0;
        for(int i=0;i<smax+1;++i)
        {
            if(i>(standing+out) && ((int)a[i]-48)>0)
            {
                //cout<<"hello";
                out=out+i-standing-out;
            }
            standing=standing+(int)a[i]-48;
            //cout<<standing<<endl;
        }
        //cout<<"------------"<<endl;
        fout<<"case #"<<x<<": "<<out<<endl;
        x++;
    }
    return 0;
}
