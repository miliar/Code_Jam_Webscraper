#include<iostream>
#include<algorithm>
#include<fstream>
using namespace std;
int main()
{
    ofstream outfile;
    ifstream infile;
    outfile.open("b.out");
    infile.open("A-small-attempt0.in");
    int t;
    infile >> t;
    //cin>>t;
    for(int j=0;j<t;j++)
    {
        int smax;
        infile >> smax;
        //cin>>smax;
        int x[smax+1];
        char str[smax+1];
        infile >> str;
        //cin>>str;
        for(int i=0;i<smax+1;i++)
          x[i]=str[i]-48;
        int sum=0;
        int extra=0;
        for(int r=0;r<smax+1;r++)
        {
         if(r<=sum)
            sum=sum+x[r];
         else
         {
            if(x[r]!=0){
                extra=extra+(r-sum);
                sum=sum+x[r]+extra;
            }
         }
        }
        outfile<<"Case #"<<j+1<<": "<<extra<<endl;
    }
    return 0;
}
