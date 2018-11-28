#include<iostream>
#include<string.h>
using namespace std;
class stack{
public:
  char arr[10000];
  int top;
  stack(){
    top=0;
    arr[top]=0;
  }
  void insert(char a){
    arr[++top]=a;
  }
  char pop(){
    return arr[top--];
  }
  void display(){
    for(int i=1;i<=top;i++){
      cout<<arr[i];

    }
    cout<<endl;
  }
  int check(){
    int sum=0,flag=0;
    char temp,sign;
    while(top>1){
      sign=pop();
      temp=pop();
      if(sign==temp){
      }
      else{
        sum++;
      }
      insert(temp);
    }
    if(pop()=='-') sum++;
    return sum;
  }
};
int main(){
  int t;
  cin>>t;
  for(int i=1;i<=t;i++){
    string str;
    stack s1;
    cin>>str;
    for(int j=str.length()-1;j>=0;j--)
      s1.insert(str[j]);
    cout<<"case #"<<i<<": "<<s1.check()<<endl;
  }
}
