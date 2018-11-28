#include<iostream>
#include<fstream>
using namespace std;
int main()
{
    ifstream fin;
    fin.open("A-large.in",ios::in);
    int t,l,n;
    fin>>t;
    l=t;
    ofstream fout;
    fout.open("output.txt",ios::out);
    while(t--)
    {
        fin>>n;
        int result=0;
        char c;
        int *arr = new int[n+1];
        int *nrr = new int[n+1];
        for(int i=0;i<=n;i++)
            {
                fin>>c;
                arr[i]=c-48;
            }
        nrr[0]=0;
        for(int i=1;i<=n;i++)
        {
            nrr[i]=arr[i-1]+nrr[i-1];
            if(nrr[i]+result<i)
                result++;
        }
        fout<<"Case #"<<l-t<<": "<<result<<endl;
    }
    return 0;
}
