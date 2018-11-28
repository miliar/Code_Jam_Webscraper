#include<fstream>
//#include<iostream>
using namespace std;
ifstream cin ("temp.in");
ofstream cout ("temp.out");
int main ()
{
    int t;
    cin>>t;
    int i;
    int save[100][100];
    for (i=0;i<t;i++)
    {
        cout<<"Case #"<<i+1<<": ";
        int n,m;
        cin>>n>>m;
        int x,y;
        for (x=0;x<n;x++)
            for (y=0;y<m;y++)
            {
                cin>>save[x][y];
            }        
        bool find=true;
        for (x=0;x<n&&find;x++)
            for (y=0;y<m&&find;y++)
            {
                bool can=false;
                int begin=x,end=x;
                while (begin>=0&&save[begin][y]<=save[x][y]) begin--;
                if (begin<0)
                { 
                   while (end<n&&save[end][y]<=save[x][y]) end++;
                   if (end>=n) can=true;
                }
                if (!can)
                {
                      int begin=y,end=y;
                      while (begin>=0&&save[x][begin]<=save[x][y]) begin--;
                      if (begin<0)
                      { 
                         while (end<m&&save[x][end]<=save[x][y]) end++;
                         if (end>=m) can=true;
                      }   
                }
                if (!can) find=false;
            }
        if (find) cout<<"YES"<<endl;
        else cout<<"NO"<<endl;
    }
    return 0;
}
