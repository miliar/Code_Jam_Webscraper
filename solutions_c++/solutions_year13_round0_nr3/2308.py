#include<cstring>
#include<cstdio>
#include<iostream>
#include<algorithm>
#include<map>
#include<list>
#include<vector>
struct node {
    int x;
    int y;
}node;

using namespace std;

int main()
{
     long long int t,k=0,d=0,c,m;
     long long int j,a,b;
     long long int arr[] = {1, 4, 9, 121, 484, 10201, 12321, 14641, 40804, 44944, 1002001, 1234321, 4008004, 100020001, 102030201, 104060401, 121242121, 123454321, 125686521, 400080004, 404090404, 10000200001, 10221412201, 12102420121, 12345654321, 40000800004, 1000002000001, 1002003002001, 1004006004001, 1020304030201, 1022325232201, 1024348434201, 1210024200121, 1212225222121, 1214428244121, 1232346432321, 1234567654321, 4000008000004, 4004009004004};
     cin>>t;
     while(t--)
     {
                vector<int>v1,v2;
                vector<vector<int> >v4;
               d++;
               cin>>a>>b;
               k = 39;
               if(a>arr[k-1])
               {
                cout<<0<<endl;
                continue;
                }
               if(b>arr[k-1])
               b=arr[k-1];
               for(int i=0;i<k;i++)
               {
                       if(arr[i]>=a)
                       {
                       c=i;
                       break;}
               }
               for(int i=0;i<k;i++)
               {
                       if(arr[i]<=b)
                       m=i;
               }
                cout<<"Case #"<<d<<": "<<m-c+1<<endl;

     }
     return 0;
}

