/*
PROG: milk2
LANG: C++
*/

#include <iostream>
#include <fstream>



using namespace std;



int main()
{
    ifstream fin("A-small-attempt0.in");
    ofstream fout("A-small-attempt0.out");
    int a[4][4]={0},b[4][4]={0};
    int N,s1,s2,M,s3,sq;
    int js=0,lst1=0,bgn1=1000000;
    fin>>N;
    for(int s=0;s<N;s++)
    {
        M=0;
        fin>>s1;
        s1=s1-1;
        for(int j=0;j<4;j++)
        {


        for(int i=0;i<4;i++)
        {
            fin>>a[j][i];
        }
        }
        fin>>s2;
        s2=s2-1;
        for(int j=0;j<4;j++)
        {


        for(int i=0;i<4;i++)
        {
            fin>>b[j][i];
        }
        }
        for(int j=0;j<4;j++)
        {


        for(int i=0;i<4;i++)
        {
            if(a[s1][i]==b[s2][j]) {M++;s3=a[s1][i];}
        }
        }
        sq=s+1;
        if(M==0) fout<<"Case #"<<sq<<": Volunteer cheated!"<<endl;
        if(M==1) fout<<"Case #"<<sq<<": "<<s3<<endl;
        if(M>1) fout<<"Case #"<<sq<<": Bad magician!"<<endl;
    }





    return 0;
}


