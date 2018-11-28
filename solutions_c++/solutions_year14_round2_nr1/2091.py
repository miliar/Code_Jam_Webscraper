#include<iostream>
#include<cstdio>
#include<fstream>
using namespace std;
int main(){
freopen ("googlecodejamfirstoutput.txt","w",stdout);
int t;
cin>>t;
int c;
for(c=1;c<=t;c++){
cout<<"Case #"<<c<<": ";
int n,total=0;
char arr1[101],arr2[101];
cin>>n;cin>>arr1;cin>>arr2;
int f1=0,f2=0;
while(1){int cou=0,con=0;char ch=arr1[f1];if(ch=='\0'&&arr2[f2]=='\0')
break;if(arr2[f2]==ch){while(arr1[f1]==ch)
{f1++;cou++;
}
while(arr2[f2]==ch)
{f2++;con++;
}total+=abs(con-cou);
}
else{cout<<"Fegla Won\n";
goto A;
}
}cout<<total<<endl;A:;
}}
