#include <iostream>
#include <fstream>

using namespace std;

ofstream myfile;

void test(int x, int ar[], int n)
{
    int first=0,sec=0,maks=0;

    for(int i=1;i<x;i++)
    {
        if(ar[i-1]>ar[i])
        {
            first += ar[i-1]-ar[i];
            if(maks< (ar[i-1]-ar[i]) )
                maks = ar[i-1]-ar[i];
        }
    }

    for(int i=0;i<x-1;i++)
    {
        if(ar[i]>maks)
            sec+=maks;
        else
            sec+=ar[i];

    }
    myfile << "Case #" << n <<": "<<first<<" "<<sec<<"\n";
}

void rea()
{
    ifstream read("C:\\Users\\Melih\\Desktop\\input.txt");
    int lines,n;
    int ar[1005];
    read>>lines;//number of lines
    for(int i=1;i<=lines;i++)
    {
            read>>n;
            for(int j=0;j<n;j++)
                read>>ar[j];
            test(n,ar,i);
    }

}

int main () {
    myfile.open ("C:\\Users\\Melih\\Desktop\\output.txt");
    rea();
    myfile.close();
    return 0;
}
