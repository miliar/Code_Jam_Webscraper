#include<iostream>
#include<fstream>
using namespace std;
int main()
{
    int T, a[100][100],n,m,i,j,k,l,count;
    ifstream fin;
    fin.open("lawnmover.in");
    ofstream fout;
    fout.open("lawnmover.out");
    fin>>T;
    for(i=0;i<T;i++)
    {
                    fin>>m>>n;
                    for(j=0;j<m;j++)
                    {
                                    for(k=0;k<n;k++)
                                    fin>>a[j][k];
                    }
                    for(j=0;j<m;j++)
                    {
                                    for(k=0;k<n;k++)
                                    {
                                                    count=0;
                                                    for(l=0;l<n;l++)
                                                    {
                                                                    if(a[j][k]<a[j][l])
                                                                    {
                                                                                      count++;
                                                                                      break;
                                                                    }
                                                    }
                                                    for(l=0;l<m;l++)
                                                    {
                                                                    if(a[j][k]<a[l][k])
                                                                    {
                                                                                      count++;
                                                                                      break;
                                                                    }
                                                    }
                                                    if(count==2)
                                                    {
                                                                fout<<"Case #"<<i+1<<": NO\n";
                                                                goto next;
                                                    }
                                    }
                    }
                    fout<<"Case #"<<i+1<<": YES\n";
                    next:;
    }
    fin.close();
    fout.close();
    return(0);
}
                                                         
