#include<iostream>
#include<cstring>
#include<fstream>
using namespace std;
struct node
{
    char val;
    node *next;
    node *prev;
};
int main()
{
    node *temp = 0,*head = 0,*tail = 0;
    ifstream in("C:\\Users\\Abhi\\Documents\\CodeJam\\1A\\A-large.in");
    ofstream out("C:\\Users\\Abhi\\Documents\\CodeJam\\1A\\A-large.out");
    char word[1005];
    int t;
    int i;
    in>>t;
    for(i=0;i<t;++i){
        in>>word;
        int j;
        for(j=0;j<strlen(word);++j){
            temp = new node;
            temp->val = word[j];
            if(!head){
                temp->next = 0;
                temp->prev = 0;
                head = temp;
                tail = temp;
            }
            else if(temp->val>=head->val){
                head->prev = temp;
                temp->prev = 0;
                temp->next = head;
                head = temp;
            }
            else{
                tail->next = temp;
                temp->prev = tail;
                temp->next = 0;
                tail = temp;
            }
        }
        temp = head;
        out<<"Case #"<<i+1<<": ";
        while(temp){
            out<<temp->val;
            temp = temp->next;
        }
        out<<endl;
        while(head){
            temp = head->next;
            delete head;
            head = temp;
        }
    }
}
