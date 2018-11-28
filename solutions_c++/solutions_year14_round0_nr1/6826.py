#include <iostream>
#include <stdio.h>
#include <fstream>
using namespace std;

int main ()
{
    ifstream ant;
    ofstream cat;
    cat.open("cat.txt");
    ant.open("ant.in");
    int f;
    ant>>f;
    for(int F = 1;F  <= f;F++){
        int x;
        ant>>x;
        int a,b,c,d;
        int p,q,r,s;
        for(int i = 1; i <= 4;i++)
        {
            ant>>a>>b>>c>>d;
            if(i == x){
                    p=a;
            q=b;
            r=c;
            s=d;}
        }
        int y;
        ant>>y;
        int u,v,w,z;
        for(int i = 1; i <= 4;i++)
        {
            ant>>a>>b>>c>>d;
            if(i == y)
                {
                    u=a;
            v=b;
            w=c;
            z=d;}
        }
        bool pqrs[4] ={0};
        if(p == u || p == v|| p == w|| p == z)pqrs[0]=1;
        if(q == u || q == v|| q == w|| q == z)pqrs[1]=1;
        if(r == u || r == v|| r == w|| r == z)pqrs[2]=1;
        if(s == u || s == v|| s == w|| s == z)pqrs[3]=1;
        int total = 0 ; // total number of matchings.
        for(int i = 0 ;  i < 4;i++)if(pqrs[i])total++;
        if(total == 0)
        {
            cat<<"Case #"<<F<<": Volunteer cheated!"<<endl;
            continue;
        }
        if(total > 1)
        {
          cat<<"Case #"<<F<<": Bad magician!"<<endl;
            continue;
        }
        // if only one matching..
        if(pqrs[0])cat<<"Case #"<<F<<": "<<p<<endl;
        if(pqrs[1])cat<<"Case #"<<F<<": "<<q<<endl;
        if(pqrs[2])cat<<"Case #"<<F<<": "<<r<<endl;
        if(pqrs[3])cat<<"Case #"<<F<<": "<<s<<endl;
    }
}
