#include<bits/stdc++.h>
using namespace std;

int pancake(int n,string a)
{
    if(n==0)
    return 0;
    
    if(a[n-1]=='-')
    {
        for(int i=0;i<n;i++)
        {
            if(a[i]=='+')
            a[i]='-';
            else
            a[i]='+';
        }
        
        return 1+pancake(n-1,a);
    }
    
    return pancake(n-1,a);
}



int main()
{
int t,n,c,j=1;
string a;

ifstream file;
file.open("large.in");

ofstream jojwishilpa;
jojwishilpa.open("outputpanckes.txt");

ios::sync_with_stdio(false);

file>>t;
    
    while(file>>a)
    {
   
    
    n=a.size();
   
   c=pancake(n,a);
    jojwishilpa<<"Case #"<<j<<": "<<c<<endl;
    j++;
    }
return 0;
}
