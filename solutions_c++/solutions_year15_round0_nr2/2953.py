#include <iostream>
#include<cstdio>
#include<vector>
#include<string>
#include<string.h>
#include<sstream>
#include<algorithm>
#include<limits.h>
using namespace std;

int numbuti(int value,int n)
{
    /*cout<<"n "<<n<<endl;
    cout<<"value "<<value<<endl;
    cout<<"n%value "<<(n%value)<<endl;
    cout<<"n/value "<<(n/value)<<endl;
    cout<<"n/2 "<<(n/2)<<endl;
    cout<<"n/2 -1 "<<((n/2)-1)<<endl;*/
    if((n%value)==0)
        return ((n/value)-1);
        else
        return n/value;
}

int numb(vector<int>a,int value)
{
    int temp=0;
    for(int i=0;i<a.size();i++)
    {
        temp+=numbuti(value,a[i]);
        //cout<<numbuti(value,a[i])<<endl;
    }
    temp+=value;
    //cout<<value<<endl;
    return temp;
}

int binary(vector<int>a,int idx,int n,int number)
{
    int mid=(idx+n)/2;
    if(idx==n)
    {
        if(a[idx]==number)
        return idx;
        else
        return -1;
    }
    if(a[mid]==number)
    return mid;
    else if(a[mid]<number)
    return binary(a,mid+1,n,number);
    else
    return binary(a,idx,mid-1,number);
}
int main()
{
          int t,d;
         scanf("%d",&t);
         for(int ii=1;ii<=t;ii++)
         {
             scanf("%d",&d);
             vector<int>n;
             int temp=0,max;
             for(int i=0;i<d;i++)
             {
                 scanf("%d",&temp);
                 n.push_back(temp);
             }
             sort(n.begin(),n.end());
             max=n[n.size()-1];
             int ans=max,te;
             for(int i=2;i<=max;i++)
             {
                te=numb(n,i);
                //cout<<endl;
              // cout<<"te "<<te<<endl;
               if(ans>te)ans=te;
             }
        printf("Case #%d: %d\n",ii,ans);
         }
    return 0;
}
