#include <iostream>
#include <fstream>
#include <string>
#include <cstring>
#include <string.h>

using namespace std;

class tlwClass{
public:
    char a;
    tlwClass* next;

    tlwClass(){
        next = NULL;
    }

    void printString(tlwClass *h){
        while(h != NULL){
            cout << h->a;
            h = h->next;
        }
    }
}*head = NULL, *tale = NULL;

void theLastWord(string s){

    tlwClass *temp = new tlwClass;
    head = temp;
    tale = temp;
    temp->a = s[0];

    for(int i=1; i<s.length(); i++){
        int x = head->a;
        int y = s[i];
        if(x>y){
            temp = new tlwClass;
            temp->a = s[i];
            tale->next = temp;
            tale = temp;
        }
        else{
            temp = new tlwClass;
            temp->a = s[i];
            temp->next = head;
            head = temp;
        }
    }

    head->printString(head);
}

int main()
{

    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);

    int t;
    cin >> t;

    string s[t];

    for(int i=0; i<t; i++)
    {
        cin >> s[i];
    }

    for(int i=0; i<t; i++)
    {
        cout << "Case #" << i+1 << ": ";
        theLastWord(s[i]);
        cout << endl;
    }

    return 0;
}
