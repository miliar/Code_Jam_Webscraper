#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
using namespace std;
int main(){
int T;
cin>>T;
for(int i=0;i<T;++i){
string s;
cin>>s;
int c0=count(s.begin(),s.end(),'Z');
int c2=count(s.begin(),s.end(),'W');
int c4=count(s.begin(),s.end(),'U');
int c6=count(s.begin(),s.end(),'X');
int c8=count(s.begin(),s.end(),'G');
int c3=count(s.begin(),s.end(),'H')-c8;
int c5=count(s.begin(),s.end(),'F')-c4;
int c7=count(s.begin(),s.end(),'S')-c6;
int c9=count(s.begin(),s.end(),'I')-c5-c6-c8;
int c1=count(s.begin(),s.end(),'O')-c0-c2-c4;
vector<int> c;
c.push_back(c0);
c.push_back(c1);
c.push_back(c2);
c.push_back(c3);
c.push_back(c4);
c.push_back(c5);
c.push_back(c6);
c.push_back(c7);
c.push_back(c8);
c.push_back(c9);
cout<<"Case #"<<i+1<<": ";
for(int j=0;j<10;++j){
for(int h=0;h<c[j];++h){
cout<<j;
}}
cout<<endl;




}


}
