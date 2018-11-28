#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include<fstream>
#include<cstring>
#include<string>
using namespace std;  // since cin and cout are both in namespace std, this saves some text
struct str{
    char c;
    str *prev;
    str *next;
};
int main() {
    freopen("A-large.in","r",stdin);
     freopen("outputA.txt","w",stdout);

  int t, n, m;
  char s[1005];
  cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
  for (int in = 1; in <=t; ++in) {
    cin >> s;  // read n and then m.
    //cout<< s<< endl;
    int len = strlen(s);
    str *head,*tail;
    tail= new str;
    head= new str;
    head->next=tail;
    tail->prev=head;
    str *temp;
    temp = new str ;
    temp->c=s[0];
    head->next=temp;
    temp->next=tail;
    temp->prev=head;
    tail->prev=temp;
    for(int i=1;i<len;i++){
        if(s[i]>=head->next->c){
            str *temp,*after;
            temp = new str ;
            after=head->next;
            temp->c=s[i];
            head->next=temp;
            temp->next=after;
            after->prev=temp;
            temp->prev=head;
        }
        else{
             str *temp,*before;
            temp = new str ;
            before=tail->prev;
            temp->c=s[i];
            tail->prev=temp;
            temp->prev=before;
            before->next=temp;
            temp->next=tail;

        }
    }
    cout << "Case #" << in << ": " ;
    temp=head->next;
   while(temp!=tail){
        cout<< temp->c;
        temp=temp->next;
   }
    cout<< endl;
    // cout knows that n + m and n * m are ints, and prints them accordingly.
    // It also knows "Case #", ": ", and " " are strings and that endl ends the line.
  }
  fclose(stdin);
  fclose(stdout);
}

