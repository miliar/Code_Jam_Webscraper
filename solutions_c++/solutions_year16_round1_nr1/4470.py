#include<iostream>
#include<algorithm>
#include<cstring>
using namespace std;

struct node{
	char value;
	node *next;
};

int main(){
	string s;
	int  T,rd=0;
	cin>>T;
	while((rd++)<T){
		cin>>s;
		node *head=new node;
		node *rear=new node;
		if(s.length()==1){			
			cout<<"Case #"<<rd<<": "<<s<<endl;
			continue;
		}
		if(s[0]>s[1]){
			head->value=s[0];
			rear->value=s[1];
			head->next=rear;
		}else{
			head->value=s[1];
			rear->value=s[0];
			head->next=rear;
		}
		for(int i=2;i<s.length();i++){
			node *no=new node;
			no->value=s[i];
			if(s[i]>=head->value){
				no->next=head;
				head=no;
			}else{
				rear->next=no;
				rear=no;
			}
		}
		cout<<"Case #"<<rd<<": ";
		for(int i=0;i<s.length();i++){
			cout<<head->value;
			head=head->next;
		}
		cout<<endl;
	}
	
	return 0;
}


