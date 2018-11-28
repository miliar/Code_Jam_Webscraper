#include<iostream>
#include<cstdio>
#include<fstream>
#include<vector>
#include<algorithm>

using namespace std;

long test,i;
long amole,no,j,cou;
vector <long> msize;

long rec(long a,long k,long no1);

int main()
{
    ifstream ifile;
    ofstream ofile;
    ifile.open("in.txt");
    ofile.open("out.txt");
    ifile>>test;
    for(i=1;i<=test;i++)
    {
        ifile>>amole>>no;
        msize.resize(no);
        for(j=0;j<no;j++)
            ifile>>msize[j];
        sort(msize.begin(),msize.end());
        cou=rec(amole,0,no);
        ofile<<"Case #"<<i<<": "<<cou<<endl;
    }
    return 0;
}

long rec(long a,long k,long no1)
{
    long size1,size2,size3;
    if(k>=no1)
        return 0;
    if(a>msize[k])
        return (rec(a+msize[k],k+1,no1));
    else
    if(a>1)
    {
        size1= (1+rec(a,k+1,no1));       // forhetting the term
        size2= (1+rec(a+a-1,k,no1));     // adding extra term
        size3= (1+rec(a,k,no1-1));
        if(size1>size2)
        {
           if(size2>size3)
            return size3;
          else
            return size2;
        }
        else
        {
           if(size1>size3)
            return size3;
          else
            return size1;
        }
    }
    else
        return (size1= (1+rec(a,k+1,no1)));
}
