#include <iostream>
#include <fstream>
using namespace std ;
int* diner= new int[1200];
int main()
{
    ifstream fin;
    fin.open("B-large.in");
    ofstream fout;
    fout.open("B-large.out");
    int k,step=0;
    int n,i,j,maxi,mini,sum;
    fin>>k;
    while( k )
    {
        fin>>n;
        for(i=0;i<n;i++) {
            fin>>diner[i];
            maxi = max(maxi,diner[i]) ;
        }
        mini = maxi ;
        for(i=1;i<=maxi;i++)
        {
            sum = i ;
            for(j=0;j<n;j++)
            {
                if(diner[j]>i)
                {
                    if(diner[j]%i== 0 )
                    {
                        sum+=(diner[j]/i-1) ;
                    }
                    else
                    {
                        sum+=(diner[j]/i) ;
                    }
                }
            }
            mini = min(mini,sum) ;
        }
        step++;
        fout<<"Case #"<<step<<": "<<mini<<endl;
    k--;
    }
    return 0 ;
}
