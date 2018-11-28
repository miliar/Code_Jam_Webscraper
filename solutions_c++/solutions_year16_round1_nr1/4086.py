/*
#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
#include <fstream>
#include <algorithm>
#include <cmath>
#include <queue>
#include <stack>
#include <vector>
#include <map>
#include <set>
#include <iomanip>

using namespace std;
#pragma comment(linker, "/STACK:102400000,102400000")
#define maxn 1000005
#define MOD 1000000007
#define mem(a , b) memset(a , b , sizeof(a))
#define LL long long
#define ULL long long
const long long INF=0x3fffffff;
bool vis[11];
char a[105];
//ofstream  ofile;
int main()
{
    int n , cas = 1 , t;
    cin >> t;
    while(t--)
    {
        cin >> n;
        cout << (n & (-n)) << endl;
        int tmp = -n;
        while(tmp != 0)
        {
            if(tmp & 1) cout << 1;
            else cout << 0;
            tmp >>= 1;
        }
        cout << endl;
    }
    return 0;
}
*/

/*
#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
#include <cmath>
#include <algorithm>

using namespace std;

class node
{
public :

  int val;
  node *next;
};

void add(int val , node *head)
{
  node *p  ;
  p = head;
  while(p -> next != NULL)  p = p-> next;
  node *tmp = new node();       //重点，用new分配内存空间，c需要malloc。如，node temp=(Node *)malloc(sizeof(Node));
  tmp -> val = val;
  tmp -> next = NULL;
  p -> next = tmp;
}

void  del(node * head , int num)
{
  node *p;
  p = head;
  while(p -> next != NULL)
  {
    if(p -> next -> val == num)
    {
      p -> next = p -> next -> next;
      continue;
    }
    p = p -> next ;
  }
}

node *Reverse(node *head)
{
    node *p1 , *p2 , *p3;
    if(head == NULL || head -> next == NULL) return head;

    p1 = head , p2 = head -> next;
    while(p2 != NULL)
    {
        p3 = p2 -> next;
        p2 -> next = p1;
        p1 = p2 ;
        p2 = p3;
    }
    head -> next = NULL;
    head = p1 ;
    return head;

}

void solve(node * head , node *tmp)
{
    if(head -> next == NULL)
    {
        tmp = head;
        return;
    }
    solve(head -> next , tmp);
    head -> next -> next = head;
}

node *Reverse2(node * head , node *tmp)
{
    solve(head , tmp);
    return tmp;
}


int main()
{
  node *head = new node();
  head->val = 2;
  head -> next = NULL;
  cout << head -> val << endl;
  int a , num;
  while(cin >> a && a != 0)
  {
    add(a , head);
  }
 // cin >> num;
 // del(head , num);
 node * tmp = new node();
  head = Reverse(head);
 // head = Reverse2(head , tmp);
 // head = tmp;
  while(head -> next != NULL) cout << head -> next -> val << " " , head = head->next;
  cout << endl;
  return 0;
}
*/

#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
#include <fstream>
#include <algorithm>
#include <cmath>
#include <queue>
#include <stack>
#include <vector>
#include <map>
#include <set>
#include <iomanip>

using namespace std;
#pragma comment(linker, "/STACK:102400000,102400000")
#define maxn 1000005
#define MOD 1000000007
#define mem(a , b) memset(a , b , sizeof(a))
#define LL long long
#define ULL long long
const long long INF=0x3fffffff;
bool vis[11];
char a[105];
//ofstream  ofile;
int main()
{
    freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
    int n , cas = 1 , t;
    cin >> t;
    while(t--)
    {
        string str ;
        cin >> str;
        int len = str.size();
        string ans = "";
        string tmp = "";
        ans = str[0];
        for(int i = 1 ; i < len ; i ++)
        {
            tmp = str[i];
            if(tmp[0] >= ans[0])
            {
                tmp += ans;
                ans = tmp;
                tmp = "";
            }
            else
            {
                ans += tmp;
                tmp = "";
            }
        }
        printf("Case #%d: " , cas++ );
        cout << ans << endl;
    }
    return 0;
}
