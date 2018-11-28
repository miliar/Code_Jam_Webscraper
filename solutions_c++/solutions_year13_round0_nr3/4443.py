#include<iostream>
#include<fstream>
#include<math.h>

using namespace std;

int fair(long int x);
int square(long int x);
int main()
{
    ifstream fin;
    ofstream fout;
    fin.open("C-small-attempt0.in");
    fout.open("qout.txt");
    int i,T,y=0;
    long int A,B,ctr=0,x;
    fin>>T;
    for(i=1;i<=T;i++)
    {
        fin>>A>>B;
        ctr=0;
        for(x=A;x<=B;x++)
        {
            if(fair(x) && square(x))
            ctr++;
        }
        fout<<"Case #"<<i<<": "<<ctr<<endl;
    }
    return 0;
}
int fair(long int x)
{
        long int rev=0,temp=x;
        while(temp>0)
        {
            rev=(rev*10)+temp%10;
            temp/=10;
        }
        if(rev==x)
        return true;
        return false;
}

int square(long int x)
{
        long int root=sqrt(x);
        if(root*root==x && fair(root))
        return true;
        return false;
}

