#include<iostream>
#include<algorithm>
#include<vector>
#include<sstream>
#include<fstream>
using namespace std;
void fun(vector<int> &w,int n)
{
    while(n)
         {
             w[n%10]=n%10;
             n=n/10;
         }
}
int main()
{
    freopen("f1.in","r",stdin);
    freopen("ofilel.out","wt",stdout);
    int t,n,j,k=0,i=0,m;
    cin>>t;
    vector<int> v(t);
    while(t)
    {
        vector<int> w(10,-1);
        cin>>n;
         for(j=0;j<10;j++)
         {
             if(n==0)
                {
                    v[i]=-1;
             break;
                }
             if(w[j]==-1)
             {
                 k++;
                 fun(w,n*k);
                 j=-1;
             }
         }
         t--;
         if(n)
        v[i]=n*k;
        i++;
        k=0;
}
for(j=0;j<i;j++)
{
    if(v[j]==-1)
        cout<<"Case #"<<(j+1)<<": "<<"INSOMNIA"<<endl;
    else
    cout<<"Case #"<<(j+1)<<": "<<v[j]<<endl;
}
}
