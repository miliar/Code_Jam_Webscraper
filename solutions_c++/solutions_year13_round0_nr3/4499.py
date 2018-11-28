#include <iostream>
#include <fstream>
#include <string>
#include<algorithm>
#include<string.h>
#include<sstream>
using namespace std;
int main()
{
    ofstream cout ("prog2.out");
    ifstream cin ("C-small-attempt2.in");
    int t,counter=0;


    long long base,i,j,n,arr[10001],k,j1,k1,low,high;

    int sum=0,mizo=0;
    base=10;
    for(i=1;i<10000001;i++)
    {
        j=i*i;
        j1=i;
        n=1;
        k=0;k1=0;
        long long miz;
        while(j!=0)
        {
            miz=j%base;
            if(miz>9)n*=10;
            k+=(n*(j%base));
            n*=10;
            j/=base;
        }
        n=1;
        while(j1!=0)
        {
            miz=j1%base;
            if(miz>9)n*=10;
            k1+=(n*(j1%base));
            n*=10;
            j1/=base;
        }
        string str1,str2;
        ostringstream convert;
        convert << k;
        str1 = convert.str();
        str2=str1;
        reverse(str1.begin(),str1.end());
        if(str1==str2){
             str1,str2;
        ostringstream convert;
        convert << k1;
        str1 = convert.str();
        str2=str1;
        reverse(str1.begin(),str1.end());
        if(str1==str2){
            arr[mizo]=k;mizo++;
            }
            }
    }
cin>>t;
while(t--)
    {
        counter++;
        sum=0;
        cin>>low>>high;
        for(i=0;i<mizo;i++)
        {
            if(arr[i]>=low&&arr[i]<=high)sum++;
        }
        cout<<"Case #"<<counter<<": "<<sum<<endl;
    }
    return 0;
}
