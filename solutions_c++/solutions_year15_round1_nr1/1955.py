#include<iostream>
#include <stdio.h>
#include <fstream>
using namespace std;
int main()
{
    ifstream fg;
    ofstream fw;
    fg.open("Al.in");
    fw.open("Asol_l");

    if(!fg.is_open() || !fw.is_open())
    {
        cout<<"Files are unable to open."<<endl;
        return 0;
    }
    int t;
    fg >> t;
    for(int i=0;i<t;i++)
    {
        //cout<<"a"<<endl;
        int n;
        fg >> n;
        int a[n];
        int max_diff = 0;
        fg>>a[0];
        for(int j=1;j<n;j++)
        {
            //cout<<"b"<<j<<endl;
            fg>>a[j];
            if(a[j-1]>a[j])
            {
                int diff = a[j-1] - a[j];
                max_diff = (diff>max_diff?diff:max_diff);
            }
        }
        long long int ans1 = 0;
        long long int ans2 = 0;
        for(int j=1;j<n;j++)
        {
            if(a[j-1]>a[j])
            {
                ans1 = ans1 + (a[j-1]-a[j]);
            }
        }
        for(int j=0;j<n-1;j++)
        {
            ans2 = ans2 + (a[j]>max_diff?max_diff:a[j]);
        }
        fw<<"Case #"<<i+1<<": "<<ans1<<" "<<ans2<<endl;
    }

    return 0;
}
