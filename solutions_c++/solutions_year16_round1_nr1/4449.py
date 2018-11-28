#include<bits/stdc++.h>
using namespace std;


int main()

{
     ifstream fin ( "A-large.in" );
    ofstream fout ( "output.txt" );
    int t,i;
    fin>>t;
    int cas=1;
   // string s;
    char s[1001];
    char res[1001];
    while(cas<=t)
    {
        int i=0,j=0;
        fin>>s;
        res[0]=s[0];
        res[1]='\0';
       i++;

        while(s[i])
        {
           // cout<<"s[i]:"<<s[i]<<" res: "<<res<<endl;
            if (s[i]>=res[0])
               {   int k=0;
                   for(int k=strlen(res)+1;k>0;k--)
                    res[k]=res[k-1];
                    res[0]=s[i];
                  // cout<<"value of res:"<<res<<endl;
               }
            else
                 {res[i]=s[i];res[i+1]='\0';}
                 // cout<<"value of res2:"<<res<<endl; }
            i++;
        }

     fout<<"Case #"<<cas++<<": "<<res<<endl;
         }
   return 0;
}

