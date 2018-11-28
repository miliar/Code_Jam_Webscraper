#include<iostream>
#include<cstring>

using namespace std;

int main(){
int t;
string s;
cin>>t;
int p=0;
while(p<t){
int n;
cin>>n;
cin>>s;
int count=0,need=0;

if(s.at(0)-'0' ==0){
 need=1;
}
else{
  count=s.at(0)-'0';
}
n++;
for(int i=1;i<n;i++)
{
 if( need+count<i){
   need+= i- (need+count);
  }
count+=s.at(i)-'0';
//cout<<endl<<"Count<<"<<count<<"i="<<i;
}
p++;
cout<<"Case #"<<p<<": "<<need<<endl;
}//while
return 0;
}
