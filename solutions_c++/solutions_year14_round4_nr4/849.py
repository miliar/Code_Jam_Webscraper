#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <cmath>

using namespace std;


const int MaxM = 10;
const int MaxN = 10;
const int MaxCh = 26;

int M, N;
string S[MaxM];
int server[MaxM];

int maxnodes = 0;
int maxcount = 0;


#define hash(c) (c - 'A')

struct Node
{
    Node* next[MaxCh];
    
public:
    Node() { memset(next, 0, sizeof(next)); }
};

int TrieInsert(Node* head, string str)
{
    int newnode = 0;
    Node* node = head;
    for(int i=0; i<str.length(); i++)
    {
        int idx = hash(str[i]);
        if(!node->next[idx])
        {
            node->next[idx] = new Node();
            newnode++;
        }
        
        node = node->next[idx];
    }
    
    return newnode;
}

void check()
{
    int total = 0;
    
    for(int s=0; s<N; s++)
    {
        int nodes = 0;
        bool inserted = false;
        Node* trie = new Node();
        
        for(int i=0; i<M; i++)
            if(server[i] == s)
                nodes += TrieInsert(trie, S[i]),
                inserted = true;
        
        if(inserted) nodes++;
        total += nodes;
    }
    
    if(total > maxnodes)
    {
        maxnodes = total;
        maxcount = 1;
    }
    else if(total == maxnodes)
    {
        maxcount++;
    }
}

void divide(int depth)
{
    if(depth == M)
    {
        check();
        return;
    }
    
    for(int s=0; s<N; s++)
    {
        server[depth] = s;
        divide(depth+1);
    }
}



int main()
{
    int T;
    cin >> T;
    
    for(int c=0; c<T; c++)
    {
        cin >> M >> N;
        for(int i=0; i<M; i++)
            cin >> S[i];

        maxnodes = 0;
        maxcount = 0;
        
        divide(0);
        
        int X = maxnodes;
        int Y = maxcount;
        
        printf("Case #%d: %d %d\n", c+1, X, Y);
    }
    
    return 0;
}

