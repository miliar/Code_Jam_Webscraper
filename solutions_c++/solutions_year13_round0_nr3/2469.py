#include <iostream>
using namespace std;
int main()
{  
   /* 
      freopen("inputarray.txt","r",stdin);
      long long int num[40];
      for(int i=0;i<39;i++)
      cin>>num[i];\
   */
    freopen("input.in","r",stdin);
    freopen("output.txt","w",stdout);
int t;
cin>>t;
 long long int  num[]={1,4,9,121,484,10201,12321,14641ll,40804ll,44944ll,1002001ll,1234321ll,4008004ll,100020001ll,102030201ll,104060401ll,121242121ll,123454321ll,125686521ll,400080004ll,404090404ll,10000200001ll,10221412201ll,12102420121ll,12345654321ll,40000800004ll,1000002000001ll,1002003002001ll,1004006004001ll,1020304030201ll,1022325232201ll,1024348434201ll,1210024200121ll,1212225222121ll,1214428244121ll,1232346432321ll,1234567654321ll,4000008000004ll,4004009004004ll};
for(int cas=1;cas<=t;cas++)
{
 long long int a,b;
 cin>>a>>b;
        int count=0;
        for(int i=0;i<39;i++)
        { 
         if(num[i]>=a && num[i]<=b)
          count++;
        }
    
        cout<<"Case #"<<cas<<": "<<count<<"\n";
}

getchar();
return(0);
}
