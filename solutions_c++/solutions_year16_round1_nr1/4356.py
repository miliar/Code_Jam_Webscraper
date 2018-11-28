#include<stdio.h>
#include<iostream>
#include<string>
using namespace std;
struct chararray{
	char c;
	chararray *link;
};
/*//int main(){
	int test1,test;
	cin>>test1;*/
#include <iostream>  // includes cin to read from stdin and cout to write to stdout
using namespace std;  // since cin and cout are both in namespace std, this saves some text
int main() {
  int t, n, m;
  cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
  for (int ij = 1; ij <= t; ++ij) {
   // cin >> n >> m;  // read n and then m.
    //cout << "Case #" << i << ": " << (n + m) << " " << (n * m) << endl;
    // cout knows that n + m and n * m are ints, and prints them accordingly.
    // It also knows "Case #", ": ", and " " are strings and that endl ends the line.
 // }
//}
//	for(test=1;test<=test1;test++){
		char string[1000000];
		cin>>string;
		int i=1;
		chararray *head=NULL;
		chararray *temp,*previous;
		temp=new chararray;
		head=temp;
		temp->c=string[0];
		temp->link=NULL;
		previous=temp;
		while(string[i]!='\0'){
			chararray *temp1;
			temp1=new chararray;
			temp1->c=string[i];
			if(string[i]<head->c){
				previous->link=temp1;
				previous=temp1;
			}
			else{
				temp1->link=head;
				head=temp1;
			}
			i++;
		}
//printf("Case #%d: ",test);
cout << "Case #" << ij << ": ";// << (n + m) << " " << (n * m) << endl;
		while(head!=NULL){
			cout<<head->c;
			head=head->link;
		}
		cout<<'\n';
	}
	return 0;
}
