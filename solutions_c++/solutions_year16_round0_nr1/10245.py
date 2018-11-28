#include <iostream>
#include <fstream>
#include <string>
#include <stdlib.h>
#include <cstring>

using namespace std;

bool verifica(bool numbers[])
{
    for(int i=0;i<10;i++)
    {
        if(!numbers[i]) return false;
    }
    return true;
}

int main()
{
    //ifstream in("A-large.in");
    //ofstream out("A-large.out");

    int t; cin>>t;
    int cont=1;
    bool numbers[10];
    while(t--)
    {
        for(int i=0;i<10;i++) numbers[i]=false;

        long n; cin>>n;
        long mult=0,num=0;

        if(n==0) cout<<"Case #"<<cont++<<": INSOMNIA"<<endl;
        else
        {
            while(!verifica(numbers))
            {
                num=++mult*n;
                while(num)
                {
                    int r = num%10;
                    numbers[r]=true;
                    num/=10;
                }
            }
            cout<<"Case #"<<cont++<<": "<<mult*n<<endl;
        }
    }

    return 0;
}
