#include<iostream>
#include<cstring>
#include<cstdio>
#include<cmath>
#include<fstream>

using namespace std;

int main()
{
    int test,i;
    int pal,l1,l2,l3;
    char buf1[1000],buf2[1000];
    ofstream ofile;
    ifstream ifile;

    ifile.open("in.txt");
    ofile.open("out.txt");
    ifile>>test;
    for(i=1;i<=test;i++)
    {
        pal=0;
        ifile>>l3>>l2;
        for(l1=1;l1<=l2;l1++)
        {
            sprintf(buf1,"%d",l1);
            strcpy(buf2,buf1);
            strrev(buf2);
            if(strcmp(buf1,buf2)==0)
            {
                int l=l1*l1;
                 //cout<<l1<<" "<<l<<endl;
                if(l<=l2 && l>=l3)
                {
                sprintf(buf1,"%d",l);
                strcpy(buf2,buf1);
                strrev(buf2);
                if(strcmp(buf1,buf2)==0)
                {
                    pal++;
                 //   cout<<l1<<" "<<l<<endl;
                }

                }

            }
        }
        ofile<<"Case #"<<i<<": "<<pal<<endl;
    }
    ifile.close();
    ofile.close();

    return 0;
}
