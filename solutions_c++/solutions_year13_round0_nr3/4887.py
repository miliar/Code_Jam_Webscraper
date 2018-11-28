#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>

using namespace std;
bool isPalindrome(int num)
{
    if (num<10)
        return 1;

    char s[20];
    sprintf(s,"%d",num);
    int L= strlen(s);
    for (int i=0,j=L-1; i<(L+1)/2; i++,j--)
        if (s[i]!=s[j]) return 0;
    return 1;
}
int main ()
{
    freopen("read.in","r",stdin);
    freopen("write.txt","w",stdout);
    int root[1010];
    bool isSquare[1010];
    memset(isSquare,0,sizeof isSquare);

    for (int i=0;i*i<=1000;i++)
        isSquare[i*i]=1,root[i*i]=i;
    int T;
    cin >> T;
    for (int t=1; t<=T; t++)
    {
        printf("Case #%d: ",t);
        int A,B,cnt=0;
        cin >> A >> B;
        for (int i=A;i<=B;i++)
            if (isSquare[i] && isPalindrome(i) && isPalindrome(root[i]))
                    cnt++;
        cout << cnt << endl;
    }
    return 0;
}


