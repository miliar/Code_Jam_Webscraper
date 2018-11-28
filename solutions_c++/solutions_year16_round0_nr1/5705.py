#include<iostream>
#include<fstream>
#define cin ifile
#define cout ofile
using namespace std;

int main()
{
    ifstream ifile;
    ifile.open("A-large.in");
    ofstream ofile;
    ofile.open("output1.txt");
    int t;
    cin>>t;

    for(int v=1;v<=t;v++)
    {
        int n,a;
        cin>>n;
        //printf("%d\n",n);
        int arr[10]={0};

        if(n==0)
            {
                cout<<"Case #"<<v<<": INSOMNIA\n";
                continue;
            }

        int fl=0;
        for(int i=1;i<1000;i++)
        {
            a=n*i;

            while(a)
            {
                arr[a%10]=1;
                a=a/10;
            }
            int flag=0;
            for(int j=0;j<10;j++)
            {
                if(arr[j]!=1)
                    {
                        flag=1;
                        break;
                    }
            }
            if(flag==0)
            {
                cout<<"Case #"<<v<<": "<<n*i<<"\n";
                fl=1;
                break;
            }
        }
        if(fl==0)
            cout<<"Case #"<<v<<"1: INSOMNIA\n";

    }

    return 0;
}
