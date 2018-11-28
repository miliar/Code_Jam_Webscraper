#include<iostream>
#include<fstream>
#include<string>
#include<cstdlib>
#include<sstream>
#include<cstdlib>
using namespace std;
int main ()
{
    fstream fin;
    fstream fohash;
    fohash.open("A_small.out",ios::out);
    fin.open("A-small-attempt0.in",ios::in);
    char ch;
    string s1 = "",s2,a[4],b,in = "0";
    int i,i1 = 0,j = 0,k,l=1,n;
        fin.get(ch);
        while(fin&&ch!=' '&&ch!='\n'&&ch!='\t')
        {
            j = 10*j + (int)ch - 48;
            fin.get(ch);
        }
        fin.get(ch);
        for(;j>0;j--)
        {
            cout<<j<<ch<<"    ";
            i = (int)ch - 48;
            fin.get(ch);
            fin.get(ch);
            i1 = i;
            for(i;i>1;i--)
            {
                while(fin&&ch!='\n')
                {
                    fin.get(ch);
                }
                fin.get(ch);
            }

            for(k=4;k>0;k--)
            {
                while(fin&&ch!=' '&&ch!='\n'&&ch!='\t')
                {
                    s1+=ch;
                    fin.get(ch);
                }
                a[k-1] = s1;
                s1.clear();
                fin.get(ch);
            }

            for(i1;i1<4;i1++)
            {
                while(fin&&ch!='\n')
                {
                    fin.get(ch);
                }
                fin.get(ch);
            }
            i = (int)ch - 48;
            fin.get(ch);
            fin.get(ch);
            i1 = i;
            s1.clear();
            for(i;i>1;i--)
            {
                while(fin&&ch!='\n')
                {
                    fin.get(ch);
                }
                fin.get(ch);
            }
            for(k=4;k>0;k--)
            {
                while(fin && ch!=' ' && ch!='\n' && ch!='\t')
                {
                    s1+=ch;
                    fin.get(ch);
                }
                b = s1;
                //cout<<"check"<<b<<"done";

                cout<<"check"<<s1<<"done\n";
                s1.clear();
                fin.get(ch);
                for(n=4;n>0;n--)
                {
                    if(a[n-1]==b)
                    {
                        if(in=="0")
                        in = b;
                        else
                            in = "17";
                    }
                }
            }
            if(in=="0")
                fohash<<"case #"<<l<<": Volunteer cheated!\n";
            else if(in=="17")
                fohash<<"case #"<<l<<": Bad magician!\n";
            else
                fohash<<"case #"<<l<<": "<<in<<"\n";
            in = "0";
            l++;
            cout<<i1;
            for(i1;i1<4;i1++)
            {
                cout<<"dh";
                while(fin&&ch!='\n')
                {
                    fin.get(ch);
                    cout<<"\n"<<ch;
                }
                if(fin)
                fin.get(ch);
            }

        }
    fin.close();
    fohash.close();
    return(0);
}
