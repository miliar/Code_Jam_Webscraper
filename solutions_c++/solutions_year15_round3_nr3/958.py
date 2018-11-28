#include<iostream>
#include <cstdlib>
#include <stdio.h>
#include <fstream>
using namespace std;
int compare (const void * a, const void * b)
{
  return ( *(int*)a - *(int*)b );
}

int main()
{
    ifstream fg;
    ofstream fw;
    fg.open("C.in");
    fw.open("ans-A.out");

    if(!fg.is_open() || !fw.is_open())
    {
        cout<<"Files are unable to open."<<endl;
        return 0;
    }
    int t;
    fg >> t;
    for(int i=0;i<t;i++)
    {
        int c,d,v;
        fg>>c>>d>>v;
        int p_d = d;
        int ans;
        int a[200]={0};
        for(int j=0;j<d;j++)
        {
            fg>>a[j];
        }
        cout<<endl;
        cout<<d<<" "<<p_d<<endl;
        for(int j=1;j<=v;j++)
        {
            cout<<j<<endl;
            int temp_sum = 0;
            int temp = d-1;
            while(temp_sum!=j && temp>=0)
            {
                if( (temp_sum + a[temp] )<=j)
                {
                    temp_sum = temp_sum + a[temp];
                }
                temp--;
            }
            if(temp_sum!=j)
            {
                cout<<"j " << j<<endl;
                a[d]=j;
                qsort(a, d+1, sizeof(int), compare);
                d = d+1;
            }
        }
        ans = d - p_d;
        fw<<"Case #"<<i+1<<": "<<ans<<endl;
    }

    return 0;
}

