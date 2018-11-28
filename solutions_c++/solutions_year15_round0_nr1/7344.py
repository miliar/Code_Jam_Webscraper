#include<iostream>
#include<stdlib.h>
//#include<cstdio>
//0500001
using namespace std;
int main(int argc,char **argv)
{
//freopen(argv[1],"r",stdin);
//freopen("output.txt","w",stdout);

int t,s,temp,current,required;
string str;
cin>>t;
for(int z=0;z<t;z++){
required=0;
cin>>s;
cin>>str;
current=str[0]-'0';
for(int i=1;i<str.length();i++){
    temp=str[i]-'0';
    if(current<i&&temp!=0){
        required+=i-current;
        current+=i-current;
        }
     current+=temp;
}
cout<<"Case #"<<z+1<<": "<<required<<endl;
}
return 0;}
