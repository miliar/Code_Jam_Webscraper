#include<bits/stdc++.h>
using namespace std;

int main()
{
    ifstream fin ( "B-large.in" );
    ofstream fout ( "pancakes_large.txt" );
    int t,i,result=0,w=0;
    string s ;
    fin>>t;
     char prev;
    while(t--)
    {   i=0;
        w++;
        fin>>s;
        prev=s[i];
        i++;
        while(s[i])
        {
          if (s[i]!=prev )
          {result++; prev=s[i];}
          i++;

        }
        i--;
        if (s[i]=='-') result++;
       // cout<< "Case #"<<w<<": "<<result<<endl;
        fout<< "Case #"<<w<<": "<<result<<endl;
        result=0;
    }

  return 0;
}
