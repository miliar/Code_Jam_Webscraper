#include <fstream>
#include <iostream>
using namespace std;


int main()
{
    int a,b,c,k,n;
    int i,j,l,s;


    ifstream infile;
    infile.open("in.txt");

    ofstream outfile;
    outfile.open("out.txt");


    infile>>n;
    cout<<n;


for(c=0; c<n; c++)
{
    infile>>a>>b>>k;
    s=0;
    for(i=0; i<=a-1; i++)
    {
        for(j=0; j<=b-1; j++)
        {
            for(l=0;l<=k-1; l++)
            {
                if((i&j)==l)
                {
                    s=s+1;

                }


            }
        }
    }
    outfile<<"Case #"<<c+1<<":"<<" "<<s<<endl;
    //cout<<c<<endl;



}


    return 0;
}
