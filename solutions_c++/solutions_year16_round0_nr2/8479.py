/**
     Programmer: S. Roy(CSE'12).
     ----------- HSTU, Dinajpur.
     Online Judge:
     Problem name:
     Imp. Algorithm:
**/
using namespace std;
#include<bits/stdc++.h>

#define sf scanf
#define pf printf

#define DEBUG1(x) cout << "> " << #x << ": " << x << endl
#define DEBUG2(x, y) cout << "> " << #x << ": " << x << " > " << #y << ": " << y << endl
#define DEBUG3(x, y, z) cout << "> " << #x << ": " << x << " > " << #y << ": " << y << " > " << #z << ": " << z << endl

/**--------------- Direction Arrays ------------------*/
//int dx[]={1,0,-1,0}; int dy[]={0,1,0,-1}; //4 Direction
//int dx[]={1,1,0,-1,-1,-1,0,1}; int dy[]={0,1,1,1,0,-1,-1,-1};//8 direction
//int dx[]={2,1,-1,-2,-2,-1,1,2}; int dy[]={1,2,2,1,-1,-2,-2,-1};//Knight Direction
/**--------------- Direction Arrays ------------------**/

int main()
{
//#ifndef ONLINE_JUDGE
//    freopen("IN.txt", "r", stdin);
//    freopen("OUT.txt", "w", stdout);
//#endif // ONLINE_JUDGE

#define maxn 102
    int cnum;
    char str[maxn], genStr[maxn];
    sf ("%d", &cnum);
    for (int cs = 1; cs <= cnum; cs++)
    {
        sf ("%s", str);

        int indx = 1;
        genStr[0] = str[0];
        for (int i = 1; str[i]; i++){
            if (genStr[indx - 1] != str[i]){
                genStr[indx] = str[i];
                indx++;
            }
        }
        genStr[indx] = 0;
        if (indx == 1){
            pf ("Case #%d: %d\n", cs, (int)(genStr[0] == '-'));
            continue;
        }

//        DEBUG1 (genStr);

        int ans = 0;
        char tempChar = genStr[0];
        for (int i = 1; i < indx; i++){
            char now = genStr[i];
            if (tempChar == '+' && now == '+') ans += 0;
            else if (tempChar == '+' && now == '-') ans += 2;
            else if (tempChar == '-' && now == '+') ans += 1;
            tempChar = '+';
        }

        pf ("Case #%d: %d\n", cs, ans);
    }
    return 0;
}
