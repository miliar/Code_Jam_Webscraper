#include<cstdlib>
#include<algorithm>
#include<cstring>
#include<iostream>
#include<cstdio>
#include<vector>
#include<map>
#include<queue>

#define maxn 1000000
using namespace std;

struct Node
{
    int ch;
    int val;
    Node (){}
    Node (int ch_, int val_)
    {
        ch = ch_;
        val = val_;
    }
    bool operator < (const Node& a) const
    {
        return val < a.val;
    }
};

priority_queue<Node> q;

void print1()
{
    Node u = q.top();
    q.pop();
    printf(" %c", u.ch+'A');
    u.val--;
    if (u.val > 0) q.push(u);
}

void print2()
{
    Node u = q.top();
    q.pop();
    char ch1 = u.ch+'A';
    u.val--;
    if (u.val > 0) q.push(u);

    u = q.top();
    q.pop();
    char ch2 = u.ch+'A';
    u.val--;
    if (u.val > 0) q.push(u);
    printf(" %c%c", ch1, ch2);
}
int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("ans.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int kase=1;kase<=T;kase++)
    {
        int n;
        scanf("%d", &n);
        int sum = 0;
        for (int i=0;i<n;i++)
        {
            int x;
            scanf("%d", &x);
            sum += x;
            Node node = Node(i, x);
            q.push(node);
        }
        printf("Case #%d:", kase);
        if (sum % 2 == 1) print1();
        while (!q.empty())
        {
            print2();
        }
        printf("\n");
    }
    return 0;
}
