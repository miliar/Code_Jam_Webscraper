#include<iostream>
#include<string>
using namespace std;
int main(){
int T;
cin>>T;
for(int i=0;i<T;++i){
string s;
cin>>s;
int c=0;
char ch='+';
for(string::reverse_iterator it=s.rbegin();it!=s.rend();++it)
{
if(*it!=ch){++c; ch=*it;}
}
cout<<"Case #"<<i+1<<": "<<c<<endl;
}
}
