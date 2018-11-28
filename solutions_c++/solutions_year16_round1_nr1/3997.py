#include<iostream>
#include<string.h>
using namespace std;
class stack{
public:
  struct node{
    char data;
    node *next;
  }*root,*first,*last;
  stack(){
    root=new node();
    root->next=NULL;
    last=new node();
    first=new node();
    last=NULL;
  }
  void insert(char a){
    node *n;
    n=new node();
    n->data=a;
    n->next=NULL;
    if(root->next==NULL){
      first=n;
      root->next=first;

    }
    else if(first->next==NULL){
      last=n;
      first->next=last;
    }
    else{
      last->next=n;
      last=n;
    }
  }
  void insertend(char a){
    node *n;
    n=new node();
    n->data=a;
    n->next=NULL;
    if(root->next==NULL){
      root->next=n;
      last=n;
    }
    else{
      last->next=n;
      last=n;
    }
  }
  void insertstart(char a){
    node *n;
    n=new node();
    n->data=a;
    n->next=NULL;
    if(root->next==NULL){
      root->next=n;
      last=n;
    }
    else{
      n->next=root->next;
      root->next=n;
    }
  }
  void display(){
    node *temp;
    temp=root;
    while(temp->next!=NULL)
    {
      temp=temp->next;
      cout<<temp->data;
    }
    cout<<endl;
  }
  void check(char a){
    if(root->next==NULL){
      insertstart(a);
    }
    else if(a>=root->next->data){
      insertstart(a);
    }
    else{
      insertend(a);
    }
  }
};
int main(){
  int t;
  cin>>t;
  for(int i=1;i<=t;i++){
    string str;
    stack s1;
    cin>>str;
    for(int j=0;j<str.length();j++)
      s1.check(str[j]);


    cout<<"case #"<<i<<": ";
    s1.display();
  }

  return 0;
}
