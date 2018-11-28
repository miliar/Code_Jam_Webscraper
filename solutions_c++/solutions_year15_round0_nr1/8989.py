#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include<fstream>
using namespace std;
int main() {
    int t,i,j;
    ifstream input("a.txt");
    ofstream out("output.txt");
    input>>t;
    for(i=0;i<t;i++)
    {
        int max,ans=0,sum=0;
        input>>max;
       // cout<<max<<endl;
        char shy[max+1];
        input>>shy;
        if(shy[0]!=0)
        {
            sum=sum+(shy[0]-'0');
        }
        else{
            ans++;
            sum+=1;
        }
        for(j=1;j<max+1;j++)
        {
            if(shy[j]-'0'!=0&&sum>=j)
            {
                sum=sum+(shy[j]-'0');
            }
            else if(shy[j]-'0'!=0&&sum<j)
            {
                ans=ans+(j-sum);
                sum+=(j-sum);
                sum+=shy[j]-'0';
            }
        }
    out<<"case #"<<i+1<<": "<<ans<<endl;
    }
}
