#include<iostream>
#include<algorithm>
#include<fstream>
#include<vector>
using namespace std;
vector<string> v;
int sz;
void fun(int n,string s)
{
     if(n==0 && s.length()==sz)
     {
           v.push_back(s);  
     }
     else if(n>0)
     {
         fun(n-1,s+"0");
         fun(n-1,s+"1");
     }
     
}
int main(int n)
{
    ifstream fin;
    fin.open("input.txt");
    ofstream fout;
    fout.open("output.txt");
    int t,q=0;
    fin>>t;
    while(t--)
    {
         q++;     
         int a,n;
         fin>>a>>n;
         int arr[n];
         for(int i=0;i<n;i++)
         {
               fin>>arr[i];  
         }
         cout<<q<<endl;
         fout<<"Case #"<<q<<": ";
         if(a==1)
                 fout<<n<<endl;
         else
         {
                 sort(arr,arr+n);
                 int k,sum,ans=n,l;
                 sum=a,k=0,l=0;
                 for(int j=0;j<n;j++)
                {
                                 //cout<<n<<" "<<arr[i]<<" "<<sum<<endl;
                                 if(arr[j]<sum)
                                 {
                                          sum+=arr[j];
                                 }
                                 else
                                 {
                                     int p=0;
                                     while(arr[j]>=sum)
                                     {
                                                sum+=sum-1;
                                                p++;            
                                     }
                                     if(n-j<=p)
                                     {
                                               l+=n-j;
                                               break;
                                     }
                                     else
                                     {
                                              l+=p;
                                              
                                     }
                                     sum+=arr[j];
                                 }                       
         
                 } 
                 ans=min(ans,l);
                 fout<<ans<<endl;
                 v.clear();
         }
                 
              
    }
    fout.close();
    fin.close();
    system("pause");
    return 0;
}
    
