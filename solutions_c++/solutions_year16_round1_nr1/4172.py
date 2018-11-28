#include <bits/stdc++.h>

using namespace std;

#define ll long long

struct per{
	string s;
	per* next;

};

int main() {

	ll t;string ss;string temp;
	cin>>t;
	for(int m=1;m<=t;m++){
		cin>>ss;
		temp=ss[0];
		per * head,*first,*last;
		head=new per;
		head->s=temp;
		head->next=NULL;
		first=head;	
		last=head;

		for(int i=1;i<ss.length();i++){
			temp=ss[i];per * nhead;
			if(temp.compare(first->s)>=0){
				nhead=new per;
				nhead->s=temp;
				nhead->next=first;
				first=nhead;
				//cout<<nhead->s;
			}
			else{
				nhead=new per;
				nhead->s=temp;
				nhead->next=NULL;
				last->next=nhead;
				last=nhead;
				//cout<<nhead->s;
			}
		}


		cout<<"Case #"<<m<<": ";
		per *temp=first;
		while(temp->next!=NULL){
			cout<<temp->s;
			temp=temp->next;
	}
	cout<<temp->s;
	cout<<endl;
	
	
}
return 0;
}