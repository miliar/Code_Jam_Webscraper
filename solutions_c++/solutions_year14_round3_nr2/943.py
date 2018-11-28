#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <map>
#include <algorithm>


#define forn(i,n) for(int i = 0; i<(int) n; i++)
#define forns(i,n,s) for(int i = s; i<n; i++)
#define forn1(i,n) for(int i = 1; i<=(int) n; i++)

#define dforn(i,n) for(int i = n; i>=0; i--)
#define dforn2(i,n,s) for(int i = n; i>=s; i--)

#define MAX 1048576
#define pb push_back
#define mp make_pair

using namespace std;
int n;
string coches [100];
int res=0;
int cases;
int ocurrences[50];
int coc[100];
int main()
{
   	freopen("input.txt", "r", stdin);
   	freopen("output.txt", "w", stdout);
   	cin>>cases;
   	forn(i,cases)
   	{
   	    res=0;
           cout<<"Case #"<<i+1<<":";
        cin>>n;
        forn(j,n)
            cin>>coches[j];
        forn(j,n)
        {
          string aux="";
          aux+=coches[j][0];
          forn1(a,coches[j].size()-1)
            if(coches[j][a]!=aux[aux.size()-1])aux+=coches[j][a];
          coches[j]=aux;
        }

        forn(j,n)
          coc[j]=j;
          string a="";
          bool flag=true;
//
            do {
            forn(f,50) ocurrences[f]=0;
            a="";

            forn(j,n)
               a+=coches[coc[j]];
            ocurrences[a[0]-'a']=1;
            flag=true;
            forn1(j,a.size()-1)
            {
                if(ocurrences[a[j]-'a']!=0 && a[j]!=a[j-1]) {flag=false;break;}
                ocurrences[a[j]-'a']++;
            }
            if(flag)res++;
        } while ( std::next_permutation(coc,coc+n) );
        cout<<res<<endl;
   	}
    return 0;
}
