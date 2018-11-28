#include<bits/stdc++.h>
using namespace std;
string s;
int c=0;
void flip(int i)
{
c++;
    char temp;
    int start = 0;
    while (start <=i)
    {
      if(s[start]=='-'){

        temp='+';
      }
        else{
          temp='-';
        }
        if( s[i]=='-'){

          s[start]='+';
        }
          else{
            s[start]='-';
          }

        s[i] = temp;
        start++;
        i--;
    }
 //cout<<"2"<<" "<<s<<endl;
}



int main(){

  int t;
  cin>>t;
for(int j=1;j<=t;++j){
bool flag=false;
c=0;
cin>>s;
while(1){
for(int i=1;i<=s.length()-1;++i){
if(s[i]==s[i-1]){
flag=false;
}
else {
flag=true;
break;
}
}
if(flag){
for(int i=1;i<=s.length()-1;++i){
if(s[i]!=s[i-1]){

flip(i-1);

}

}
}
else{
break;
}

}
//cout<<s<<endl;
if(s[0]=='+')
cout<<"Case #"<<j<<":"<<" "<<c<<endl;
else
cout<<"Case #"<<j<<":"<<" "<<c+1<<endl;

}
}
