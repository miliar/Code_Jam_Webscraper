#include<iostream>
#include<fstream>
#include<algorithm>
using namespace std;
double a[1000],b[1000];
int main()
{
    ifstream fin ("D-large.in",ios::in);
    ofstream fout;
    fout.open ("D-large.txt");
    int t,x=1;
    fin>>t;
    int n,i,j,count1,count2;
    while(x<=t)
    {
        count1=0;count2=0;
        fin>>n;
        for(i=0;i<n;i++)
            fin>>a[i];
        for(i=0;i<n;i++)
            fin>>b[i];
        sort(a,a+n);
        sort(b,b+n);
        for(i=0,j=0;j<n;j++)
        {
            if(a[i]<b[j])
            {
                count1++;
                i++;
            }
        }
        for(i=0,j=0;i<n;i++)
        {
            if(a[i]>b[j])
            {
                count2++;
                j++;
            }
        }
        fout<<"Case #"<<x<<": "<<count2<<" "<<n-count1<<endl;
        x++;
    }
    return 0;
}
