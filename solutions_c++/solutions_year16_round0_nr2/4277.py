#include "bits/stdc++.h"
using namespace std;
typedef unsigned long long ull;
typedef long long int ll;
typedef vector<long long int> vi;
int main()
{
    ios_base::sync_with_stdio(0);
    ll n,sum=0,count=0,t;
    ifstream f("B-large.in");
    ofstream o("Bout.out");
    f>>t;
    int z=t;
    char tu[10];
    f.getline(tu,10);
    while(t--)
    {
       char a[105];
       f.getline(a,105);
       count=0;
       if(a[strlen(a)-1]=='-')
        count++;
        //cout<<a[strlen(a)-1]<<endl;
       for(int i=0;i<strlen(a)-1;i++)
       {
           if(a[i]=='-'&&a[i+1]=='+')
            count++;
            if(a[i]=='+'&&a[i+1]=='-')
            count++;
       }
       o<<"Case #"<<z-t<<": "<<count<<endl;
       //cout<<count<<endl;
    }
	return 0;
}


