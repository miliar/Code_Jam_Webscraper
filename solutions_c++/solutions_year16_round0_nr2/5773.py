#include<iostream>
#include<fstream>
#define cin ifile
#define cout ofile
using namespace std;

char str[200];

int main()
{
    ifstream ifile;
    ifile.open("B-large.in");
    ofstream ofile;
    ofile.open("output1.txt");
    int t;
    cin>>t;

    for(int v=1;v<=t;v++)
    {
        int n,a;
        cin>>str;
        //printf("%d\n",n);
        int ans=0;
        if(str[0]=='-')
            ans=1;
        for(int i=1;str[i]!='\0';i++)
        {
             if(str[i]=='+')
                continue;
             if(str[i-1]=='-')
                continue;
             ans+=2;

        }
        cout<<"Case #"<<v<<": "<<ans<<"\n";
    }

    return 0;
}
