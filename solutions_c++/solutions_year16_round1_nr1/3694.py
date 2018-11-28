#include<bits/stdc++.h>
#define fo(i,n) for(i=0;i<n;++i)
#define ll long long
using namespace std;

int main(){

 ifstream fin ("A-large.in");
 ofstream fout ("a-large-out.txt");
 int t, te, i;
 string s, temp;
 fin>>t;
 for(te=0;te<t;te++){

    fin>>s;

    temp=s[0];
    for(i=1;i<s.length();i++)
    {
       if((s[i])>=(temp[0]))
            temp=s[i]+temp;
        else
            temp=temp+s[i];


    }



    fout<<"Case #"<<te+1<<": "<<temp<<endl;
 }

 return 0;
}
