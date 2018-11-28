#include<iostream>
#include<fstream>
using namespace std;
int main()
{
    ofstream fout;
    fout.open("output.txt");
    int t,s,n=0,m=0,i,c=0;
    char Arr[1002];
    cin>>t;
    while(t--)
    {   c++;
        n=0;m=0;
        cin>>s;
        cin>>Arr;
        for(i=0;i<=s;i++)
        {
            if(n>=i)
            {
                n+=Arr[i]-'0';
            }
            else{
                n+=1;
                n+=Arr[i]-'0';
                m+=1;
            }
        }
        fout<<"Case #"<<c<<": "<<m<<endl;
    }
    fout.close();
}
