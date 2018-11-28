#include <iostream>
#include <cstdlib>
using namespace std;
struct node
{
    char info;
    node *next;
};
int main() {
    int t,tno;
    char str[1002];
    cin>>t;
    for(tno=1;tno<=t;tno++)
    {
        cin>>str;
        node *start=NULL;
        node *end=NULL;
        node *newnode;
        node *traverse;
        for(int i=0;str[i]!='\0';i++)
        {
            newnode = new node;
            newnode->info = str[i];
            newnode->next = NULL;
            if(start==NULL)
            {
                start = end = newnode;
            }
            else
            {
                char s = start->info;
                if(s<=str[i])
                {
                    newnode->next = start;
                    start = newnode;
                }
                else
                {
                    end->next = newnode;
                    end = newnode;
                }
            }
        }
        traverse = start;
        while(traverse!=NULL)
        {
            cout<<traverse->info;
            traverse=traverse->next;
        }
        cout<<"\n";
    }
	// your code goes here
	return 0;
}
