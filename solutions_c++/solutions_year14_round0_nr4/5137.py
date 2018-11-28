#include <iostream>
#include <string>
#include <sstream>

double mnaomi[1000];
double mken[1000];
bool boolmken[1000];

using namespace std;

void sortarray(double* a, int l)
{
    double number;
    int j;
    for(int i=1;i<l;i++)
    {
        j=i;
        number = a[i];
        while(a[j-1]>number)
        {
            a[j]=a[j-1];
            j--;
        }
        a[j]=number;
    }
}

int kensmallesthigher(double x, int n)
{
    for(int i=0;i<n;i++) if ((mken[i]>x) && (boolmken[i]!=false)) return i;
    for(int i=0;i<n;i++) if (boolmken[i]!=false) return i;
    return -1;
}

void initken(int n)
{
    for(int i=0;i<n;i++) boolmken[i]=true;
}

int war(int n)
{
    initken(n);
    int res = 0;
    int index;
    for(int i=0;i<n;i++)
    {
        index = kensmallesthigher(mnaomi[i],n);
        if (mnaomi[i]>mken[index])
        {
            res++;
            boolmken[index]=false;
        }
        else boolmken[index]=false;
    }
    return res;
}

double naomitells(double x,int n,int round)
{
    //if she dominates tell x
    //#elements=n-round
    int nelements = n-round;
    int counter=1;
    int c=0;
    int naomiindex = round;
    int kenindex = 0;
    while(counter<=nelements)
    {
        while(boolmken[kenindex]==false) kenindex++;
        if (mnaomi[naomiindex]>mken[kenindex]) c++;
        counter++;
    }
    if (c==nelements)
    {
        //get biggest
        kenindex=n-1;
        while((kenindex>=0) && (boolmken[kenindex]==false)) kenindex--;
        return mken[kenindex]+0.000001;
    }
    int i=n-1;
    while((i>=0) && (boolmken[i]==false)) i--;
    if (mken[i]>x) return mken[i]-0.000001;
    else return x;
}

int dwar(int n)
{
    initken(n);
    int res = 0;
    int index;
    for(int i=0;i<n;i++)
    {
        index = kensmallesthigher(naomitells(mnaomi[i],n,i),n);
        if (mnaomi[i]>mken[index])
        {
            res++;
            boolmken[index]=false;
        }
        else boolmken[index]=false;
    }
    return res;
}

int main()
{
    string line;
    int n; //number of blocks
    getline(cin,line);
    stringstream firstline(line);
    int numbertestcases;
    firstline >> numbertestcases;
    for(int z=1;z<=numbertestcases;z++)
    {
        getline(cin,line);
        stringstream testline(line);
        testline >> n;
        getline(cin,line);
        stringstream weightline1(line);
        for(int y=1;y<=n;y++) weightline1 >> mnaomi[y-1];
        getline(cin,line);
        stringstream weightline2(line);
        for(int y=1;y<=n;y++) weightline2 >> mken[y-1];
        //sort arrays
        sortarray(mnaomi,n);
        sortarray(mken,n);
        cout << "Case #" << z << ": " << dwar(n) << " " << war(n) << endl;
    }
    return 0;
}
