#include<iostream>
#include<cstring>
using namespace std;
int nconso(string n)
{ int i;
    for(i=0;i<n.length();i++)
    {
                             if(n[i]=='a' || n[i]=='e' || n[i]=='o' || n[i]=='u' || n[i]=='i')
                             {return 0;}
                             }
                             return 1;
                             }
int main()
{
    freopen("C:\\Users\\Dell\\Desktop\\input.txt","r",stdin);
    freopen("C:\\Users\\Dell\\Desktop\\output.txt","w",stdout);
    int t,t1;
    cin>>t1;
    cin.ignore();
    for(t=1;t<=t1;t++)
    {
                      string nm;int i,j,k=-1,n,l,sum=0,totsum=0;
                      cin>>nm>>n;//cout<<nm<<" "<<n<<endl;
                      l=nm.length();
                      for(i=0;i<=(nm.length()-n);i++)
                      {
                                                j=i+n-1;
                                                
                                                                              if(nconso(nm.substr(i,n)))
                                                                              {//cout<<nm.substr(i,n)<<endl;
                                                                              
                                                                                 int sum1=l-j;//cout<<sum1<<endl;
                                                                                 int sum2=(sum1*(i-k-1));//cout<<(sum2)<<endl;
                                                                                 sum=sum1+sum2;//cout<<sum<<endl;
                                                                                 k=i;totsum+=sum;
                                                                              }
                                                
                      }
                      cout<<"Case #"<<t<<": "<<totsum<<endl;
    }
                      return 0;
    }
                                                                                                     
    