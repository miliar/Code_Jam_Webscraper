#include<iostream>
#include<fstream>
using namespace std;
int main()
{
    int t;
    ofstream myfile;
    myfile.open ("rajvir1.txt");
    ifstream myfile2;
    myfile2.open("A-small-attempt2.in");
    myfile2>>t;
    int z=t;
    while(t--)
    {
        int n;
        myfile2>>n;
        if(n==0)
        {
            myfile<<"Case #"<<z-t<<": INSOMNIA\n";
        }
        else
        {
            int a[10]={0};
            int sumu=0;
            int y=0;
            int cou=0;
            while(sumu!=10)
            {
                cou++;
                y=y+n;
                int x=y;
            while(x!=0)
            {
                if(a[x%10]==0)
                {
                    a[x%10]=1;
                    sumu=sumu+1;
                }
                x=x/10;
            }
            }
            myfile<<"Case #"<<z-t<<": "<<y<<"\n";
        }
    }
    return 0;
}
