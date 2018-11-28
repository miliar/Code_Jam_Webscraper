#include<iostream>
#include<vector>
#include<algorithm>
#include<stdio.h>
#include<fstream>
using namespace std;
int main()
{
    ofstream fout("output.in");
    ifstream fin("A-small-attempt1.in");
    int t,m=1,k;
    fin>>t;
    for(k=1;k<=t;k++)
    {
        vector<int> hash(17);

        vector< vector<int> > arr(4, vector<int> (4));
        int a,i,j;
        fin>>a;
        for(i=0;i<4;i++)
            for(j=0;j<4;j++)
               {
                   fin>>arr[i][j];
                   if((i+1)==a)
                   {
                       hash[arr[i][j]]++;
                   }
               }
          int b;
          fin>>b;
          for(i=0;i<4;i++)
            for(j=0;j<4;j++)
               {
                   fin>>arr[i][j];
                   if((i+1)==b)
                   {
                       hash[arr[i][j]]++;
                   }
               }
          int count=0,ans;
          for(i=1;i<=16;i++)
                {
                    if(hash[i]==2)
                    {
                        count++;
                        ans=i;
                    }
                }
                if(count==1)
                {
                    fout<<"Case #"<<k<<": "<<ans<<endl;
                    //continue;
                }
                else
                    if(count>1)
                {
                    fout<<"Case #"<<k<<": "<<"Bad magician!"<<endl;
                }
                else
                    if(count==0)
                {
                    fout<<"Case #"<<k<<": "<<"Volunteer cheated!"<<endl;
                }
                //m++;
    }
}
