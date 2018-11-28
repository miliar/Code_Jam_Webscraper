#include<bits/stdc++.h>
using namespace std;

int main()
{
    int a[2000];
    long int test,step=0,l=0;
    long int n,i,j,maximum=0,min1,sum,p,q;
    ifstream fin;
    ofstream fout;
    fin.open("pan.in",ios::in);
    fout.open("ans2.txt",ios::out);
    fin>>test;
    while(test--)
    {
        maximum=0;
        fin>>n;
        for(i=0 ; i<n ; i++)            //Finds out the maximum
        {
            fin>>a[i];
            if(a[i]>maximum)
                maximum=a[i];
        }
        min1 = maximum ;
        for(i=1; i<=maximum ;i++)
        {
            sum = i ;
            for(j=0 ; j<n ; j++)
            {
                if(a[j] > i)
                {
                    if(a[j]%i == 0)
                        sum += (a[j]/i-1) ;
                    else
                        sum += (a[j]/i) ;
                }
            }
            min1 = min(min1,sum) ;
        }
        step++;
        fout<<"Case #"<<step<<": "<<min1<<endl;
    }
    return 0 ;
}
