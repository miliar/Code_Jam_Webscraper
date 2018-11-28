#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <map>
#include <algorithm>
#include <string>

#define forn(i,n) for(int i = 0; i<(int) n; i++)
#define forns(i,n,s) for(int i = s; i<n; i++)
#define forn1(i,n) for(int i = 1; i<=(int) n; i++)

#define dforn(i,n) for(int i = n; i>=0; i--)
#define dforn2(i,n,s) for(int i = n; i>=s; i--)

#define MAX 1048576
#define pb push_back
#define mp make_pair

using namespace std;
int cases,a,b;
int vec [20],contador;

string frase[2]={"Volunteer cheated!","Bad magician!"};
int main()
{
   	freopen("magictrick.txt", "r", stdin);
   	freopen("magictrickout.txt", "w", stdout);
   	cin>>cases;
   	forn(i,cases)
   	{
   	    cout<<"Case #"<<i+1<<": ";
   	    int resp = 0;
   	    contador = -1;
   	    forn(i,20)vec[i]=0;
   	    forn(as,2)
   	    {
           cin>>a;a--;
            forn(i,4)
                forn(j,4)
                {                   
                    cin>>b;
                    if(i==a)
                        if(++vec[b]==2 && contador ==-1)contador = b;
                        else
                            if(contador!=-1 && vec[b]==2)
                                resp = 1;
                }
        }
        if(resp==1) cout<<frase[resp]<<endl;
        else
            if(contador!=-1) cout<<contador<<endl;
            else    cout<<frase[0]<<endl;
   	}
    return 0;
}
