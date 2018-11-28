
#include <iostream>
#include <fstream>
//#include <string>

using namespace std;

int main() {
    ofstream fout ("test.out");
    ifstream fin ("test.in");
    int tes;
    fin>>tes;
    for(int z=1;z<=tes;z++)
    {
            fout<<"Case #"<<z<<": ";
           int a[4][4],b[4][4],c,d,s=0,fl=1,f1=0;
           fin>>c;
           for(int i=0;i<4;i++)
           {
                   for(int j=0;j<4;j++)
                   {
                           fin>>a[i][j];
                   }
           }
           fin>>d;
           for(int i=0;i<4;i++)
           {
                   for(int j=0;j<4;j++)
                   {                           
                           fin>>b[i][j];
                   }
           }
           for(int i=0;i<4;i++)
           {
                   for(int j=0;j<4;j++)
                   {
                           if(a[c-1][i]==b[d-1][j]&&fl)
                           {
                                                       s=a[c-1][i];
                                                       fl=0;
                                                       continue;
                           }
                           if(a[c-1][i]==b[d-1][j]&&!fl&&!f1)
                           {
                               fout<<"Bad magician!\n";
                               f1=1;
                              
                           }
                   }
           }
           if(s&&!f1)               
           {
                fout<<s<<endl;
           }
           if(!s)
           {
                 fout<<"Volunteer cheated!\n";
           }
           
    }
                
           
           
           
    
    return 0;
}
