#include<iostream>
#include<algorithm>
#include<fstream>
using namespace std;
string s;
int cnt;
int check();
int rev()
{
    int j,temp;
   // cout<<s.length()<<endl;
    cnt=0;
    int q=check();
    if(q==1)
    {
        return 0;
    }
l:
cnt++;
    for(j=s.length()-1;j>=0; j--)
    {
        if(s[j]=='-'&&(s[j+1]=='+'||s[j+1]=='\0'))
        {
           // cout<<"in"<<endl;
            //cout<<"j="<<j<<endl;
            temp=j;

        }
        else{
            continue;
        }
    }
   // cout<<cnt<<endl;
    reverse(s.begin(),s.begin()+j+1);
for(j=0;j<=temp;j++)
{
    if(s[j]=='+')
    {
        s[j]='-';
    }
    else if(s[j]=='-')
    {
        s[j]='+';
    }
}
    q=check();
    if(q==1)
    {
        return 0;
    }
    else if(q==0)
    {
        goto l;

    }
    //cout<<s<<endl;


}

int check()
{
    for(int i=0; i<s.length(); i++)
    {
        if(s[i]=='-')
        {
            return 0;
        }
    }
    return 1;
}
main()
{
     ifstream fin;
    fin.open("B-small-attempt2.in");
    int i,j,k,t;
    fin>>t;
    ofstream fout;
     fout.open("output.txt",ios::app);
    for(i=1; i<=t; i++)
    {
        fin>>s;
        rev();
        fout<<"Case #"<<i<<": "<<cnt<<endl;


    }
}
