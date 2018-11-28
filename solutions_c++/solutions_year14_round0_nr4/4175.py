#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <map>
#include <algorithm>
#include <set>

#define forn(i,n) for(int i = 0; i<(int) n; i++)
#define forns(i,n,s) for(int i = s; i<n; i++)
#define forn1(i,n) for(int i = 1; i<=(int) n; i++)

#define dforn(i,n) for(int i = n; i>=0; i--)
#define dforn2(i,n,s) for(int i = n; i>=s; i--)

#define MAX 1048576
#define pb push_back
#define mp make_pair

using namespace std;
int cases,a;
double b;
vector <double> naomi, ken;

int main()
{
   	freopen("input.txt", "r", stdin);
   	freopen("output.txt", "w", stdout);
   	cin>>cases;
   	forn(asdf,cases)
   	{
   	    cout<<"Case #"<<asdf+1<<": ";
        naomi.clear(); ken.clear();
        set <double> n,k;
        cin>>a;
        forn(j,a)
          cin>>b,naomi.pb(b),n.insert(b);
        forn(j,a)
          cin>>b,ken.pb(b),k.insert(b);

    sort(naomi.begin(),naomi.end());
    sort(ken.begin(),ken.end());

    int resp1 = 0;
    double no,no2;
    set<double>::iterator it,it2,it3;
    while(!n.empty())
    {
         it = k.begin();
         forn(fdsa,k.size()-1)
           it++;
         no = *(it);

         it2 = n.begin();
         forn(fdsa,n.size()-1)
           it2++;
         no2 = *(it2);

        if(no > no2)
        {
            k.erase(no);
            n.erase(n.begin());
        }
        else
        {
            it3=n.begin();
            forn(fdsa,n.size())
              if(*(it3)> *(k.begin()))
              {
                         n.erase(it3);
                        // cout<<(*it3)<<" le gana a "<<(*k.begin())<<endl;
                         break;
              }
              else
                   it3++;
            k.erase(k.begin());
            resp1++;
        }
    }

    cout<<resp1<<" ";

    int resp2=0;
    int izq=0,der=a-1;
    dforn(i,naomi.size()-1)
    {
        if(naomi[i]>ken[der])
            resp2++;
        else
            der--;
    }
    cout<<resp2<<endl;
   	}
    return 0;
}
