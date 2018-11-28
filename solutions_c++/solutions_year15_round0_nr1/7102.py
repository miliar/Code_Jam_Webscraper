#include<bits/stdc++.h>
#define ll long long

#define forf(i, a, b) for(int i =(a); i <(b); ++i)
#define forb(i, a, b) for(int i =(a); i >=(b); --i)
using namespace std;
int main()
{
ifstream file;
ofstream myfile;
myfile.open("A-large_.txt");
file.open("A-large.in");

int t,sm,cnt,np,l;


file>>t;
forf(ta,1,t+1)
{
file>>sm;
char a[sm+1];
file>>a;
l=strlen(a);
np=0;
cnt=0;

forf(i,0,l)
{
    if(np>=i){}
    else
    {
        cnt=cnt+((i-np));
        np=np+((i-np));
    }

np=np+a[i]-'0';
}
myfile<<"Case #"<<ta<<": "<<cnt<<endl;
}


myfile.close();
file.close();
return 0;
}
//myfile<<"Case #"<<ta<<": "<<endl;

