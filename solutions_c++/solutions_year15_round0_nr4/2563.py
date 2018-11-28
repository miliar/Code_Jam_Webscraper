#include <iostream>
#include <cmath>
#include <cstdio>
#include <algorithm>
#include <cstring>
//#include <conio.h>
#include <fstream>
#include <cmath>
#include <map>
using namespace std;
#define pii pair<int,int>
#define mp(a,b) make_pair(a,b)
#define mpp(a,b,c) mp(mp(a,b),c)
map<pair<pii,int>,int> mapi;


void init()
{
     pair<pii,int> pr;
//1     
     mapi[mpp(1,1,1)]=1;
     mapi[mpp(1,2,1)]=1;mapi[mpp(1,2,2)]=1;
     mapi[mpp(1,3,1)]=1;
     mapi[mpp(1,4,1)]=1;mapi[mpp(1,4,2)]=1;
//2     
     mapi[mpp(2,2,1)]=1;mapi[mpp(2,2,2)]=1;
     mapi[mpp(2,3,1)]=1;mapi[mpp(2,3,2)]=1;mapi[mpp(2,3,3)]=1;
     mapi[mpp(2,4,1)]=1;mapi[mpp(2,4,2)]=1;
//3
     mapi[mpp(3,3,1)]=1;mapi[mpp(3,3,3)]=1;
     mapi[mpp(3,4,1)]=1;mapi[mpp(3,4,2)]=1;mapi[mpp(3,4,3)]=1;mapi[mpp(3,4,4)]=1;
//4
     mapi[mpp(4,4,1)]=1;mapi[mpp(4,4,2)]=1;mapi[mpp(4,4,4)]=1;     
     
     
 }

int main()
{
    ifstream fin("input.txt");
   ofstream fout("output.txt");
    
    int t;
    fin>>t;
    int x,r,c;
    init();
    int ind=1;
    while(t--)
    {
              fin>>x>>r>>c;
              fout<<"Case #"<<ind<<": ";
              if(r>c)swap(r,c);
              
              if(mapi.find(mpp(r,c,x))==mapi.end())
              fout<<"RICHARD"<<endl;
              else fout<<"GABRIEL"<<endl;
              
              ind++;
              }
    
    fout.close();
    fin.close();
    //getch();
    return 0;
}
