#include<iostream>
#include<stdio.h>
#include<fstream>

using namespace std;

//ifstream fin("input.txt");
//ofstream fout("output.txt");

int main()
{
    int t,c=1;
    cin>>t;
    string s;
    while(t--)
    {
        cin>>s;
        int i=s.size()-1,k=0,cnt=0;
        while(i>=0)
        {
            if((k%2==1 && s[i]=='+')||(k%2==0 && s[i]=='-'))
            {
                k++;
                cnt++;
            }
            i--;
        }
        cout<<s<<endl;
        cout<<"Case #"<<c++<<": "<<cnt<<endl;
    }
    return 0;
}

