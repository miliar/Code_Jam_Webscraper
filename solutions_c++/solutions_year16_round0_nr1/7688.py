#include<iostream>
using namespace std;
class linkedlist{
public:
  struct node{
    int data;
    node *next;
  }*root,*curr,*last;
  node* create(int item){
    node *n;
    n=new node();
    n->data=item;
    return n;
  }
  linkedlist(){
    root=new node();
    root->next=create(0);
    curr=root->next;
    for(int i=1;i<=9;i++){
      curr->next=create(i);
      curr=curr->next;
    }
  }
  void display(){
    node *temp=root;
    while(temp->next!=NULL){
      temp=temp->next;
      cout<<temp->data<<" ";
    }
  }
  void check(int item){
    node *temp=root;
    while(temp->next!=NULL){
      last=temp;
      temp=temp->next;
      if(temp->data==item){
        deletenode(last,temp);
        break;
      }
      else if(temp->data>item){
        break;
      }
    }
  }
  void deletenode(node *one,node *two){
    one->next=two->next;
  }
};
int main(){
  int n,t;
  cin>>n;
  for(int i=1;i<=n;i++){
    cin>>t;
    if(t!=0){
      linkedlist a;
      int j=1,x;
      while(a.root->next!=NULL){
        x=j*t;
        while(x!=0){
          a.check(x%10);
          x=x/10;
        }
        j++;
      }
      cout<<"case #"<<i<<": "<<(j-1)*t<<endl;
    }
    else{
      cout<<"case #"<<i<<": INSOMNIA"<<endl;
    }
  }
  return 0;
}
