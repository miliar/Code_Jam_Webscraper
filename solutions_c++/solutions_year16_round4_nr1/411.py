#include <iostream>
#include <stdio.h>
#include <string.h>
using namespace std;
#define NUM 26
typedef struct DictNode
{
    int count;
    bool isWord;
    struct DictNode *NodeList[NUM];

    DictNode()
    {
        count = 1;
        isWord = false;
        for(int i = 0;i<NUM;i++)
            NodeList[i] = NULL;
    }
} Node;

int main()
{
//    freopen("in.txt","r",stdin);
    int N;
    cin>>N;
    string ss;
    Node *root = new Node();
    while(N--)
    {
        cin>>ss;
        Node *p;
        p = root;
        for(int i = 0 ; i < ss.size(); i++)
        {
            if(p->NodeList[ss[i]-'a']){
                p = p->NodeList[ss[i]-'a'];
                p->count++;
            }
            else{
                p->NodeList[ss[i]-'a'] = new Node();
                p = p->NodeList[ss[i]-'a'];
            }
        }
        p->isWord = true;
    }
    cin>>N;
    while(N--)
    {
        cin>>ss;
        Node *p;
        p = root;
        int i;
        for(i = 0 ; i < ss.size(); i++)
        {
            if(p->NodeList[ss[i]-'a']){
                p = p->NodeList[ss[i]-'a'];
            }
            else
                break;
        }
        if(i<ss.size())
            cout<<0<<endl;
        else
            cout<<p->count<<endl;
    }
    return 0;
}