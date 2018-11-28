#include<iostream>
#include<fstream>
using namespace std;
int main(){
    freopen ("googlecodejamfirstoutput.txt","w",stdout);
int t;
cin>>t;
int c;
for(c=1;c<=t;c++){
                  cout<<"Case #"<<c<<": ";
                  int a,b,k,i,j,count=0;
                  cin>>a>>b>>k;
                  for(i=0;i<a;i++)
                  for(j=0;j<b;j++)
                  if((i&j)<k)
                  count++;
                  cout<<count<<endl;
}
    }
