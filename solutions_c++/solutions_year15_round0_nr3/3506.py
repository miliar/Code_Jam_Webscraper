#include <bits/stdc++.h>
#define loop(i,s,e) for(int i =s ;i < e;i++)
#define space " "
using namespace std;
#define val 6
#define MAX 10009


bool fn(int indx, int part, int sign, int x);
void preprocess();
int convert(char x);
int mul(int x, int y);
int check(int left);

char input[MAX], array[MAX];
int first[MAX], sec[MAX], visited[MAX][2][2][5];
bool dp[MAX][2][2][5];
int l, num, n, cases, t, p = 1;

int main()
{
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("oo.out", "w", stdout);
    memset(visited, - 1, sizeof(visited));
    scanf("%d", &cases);
    while(cases--)
    {
        scanf("%d %d", &l, &num);
        scanf("%s", input);
        preprocess();
        printf("Case #%d: %s\n", p++, fn(0, 0, 0, 1) == 1 ? "YES" : "NO");
    }
    return 0;
}

bool fn(int indx, int part, int sign, int x)
{
    if(indx == n)
        return 0;

    int& flag = visited[indx][part][sign][x];
    bool& ret = dp[indx][part][sign][x];
    if(flag == cases)
        return ret;
    flag = cases, ret = 0;
    int s, left;

    ///still in i
    if(part == 0)
    {
        ret = ret | fn(indx + 1, part, sign, x);
        int s = 0;
        if(first[indx] < 0)
            s = 1;

        if(first[indx] == 2)
            ret = ret | fn(indx + 1, 1, 0, 1);
    }
    else if(part == 1)
    {
        if(sec[indx] == 4 && x == 3 && sign == 0)
            ret = 1;
        ///last

        if(sign == 1)
            x = -1 * x;
        int tmp = mul(x, convert(array[indx]));
        int s = 0;
        if(tmp < 0)
            s = 1;
        ret = ret | fn(indx + 1, part, s,  abs(tmp));
    }

    return ret;
}

int check(int left)
{
    if(left == 0)
        return 1;

    if(left == 1)
        return first[l - 1];

    if(left == 2)
        return -1;

    if(left % 2 != 0)
        return -1 * first[l - 1];

    return 1;
}

void preprocess()
{
    int indx = 0;
    for(int i = 0; i < num; i++)
        for(int j = 0; j < l; j++)
            array[indx] = input[j], indx++;
    n = indx;

    int prev = 1;
    for(int k = 0; k < n; k++)
        first[k] = mul(prev, convert(array[k])), prev = first[k];

    prev = 1;
    for(int k = n - 1; k >= 0; k--)
        sec[k] = mul(convert(array[k]), prev), prev = sec[k];

}

int convert(char x)
{
    if(x == 'i')
        return 2;

    if(x == 'j')
        return 3;

    return 4;
}

int mul(int x, int y)
{
    int s1 = 1, s2 = 1;
    if(x < 0)
        s1 = -1, x = abs(x);

    if(y < 0)
        s2 = -1, y = abs(y);

    s1 = s1 * s2;

    if(x == 2 && y == 3)
        return 4 * s1;

    if(x == 3 && y == 2)
        return -4 * s1;

    ///i*k
    if(x == 2 && y == 4)
        return -3 * s1;

    if(x == 4 && y == 2)
        return 3 * s1;

    ///j*k
    if(x == 3 && y == 4)
        return 2 * s1;

    if(x == 4 && y == 3)
        return -2 * s1;

    if(x == 1 || y == 1)
        return x * y * s1;

    if(x == y)
        return -1 * s1;
}
/*
map<string,string,string>h;
int main(){
//freopen("in.txt","r",stdin)
h["'i"]["j"]="k";
h["'i"]["k"]="-j";
h["i"]["1"] = "i";
//-ves
h["-'i"]["j"]="-k";
h["'-i"]["k"]="j";
h["-i"]["1"] = "-i";

h["'j"]["i"]="-k";
h["'j"]["k"]="i";
h["j"]["1"] = "j";

h["'-j"]["i"]="k";
h["'-j"]["k"]="-i";
h["-j"]["1"] = "-j";

h["'k"]["i"]="j";
h["'k"]["j"]="-i";
h["k"]["1"] = "k";

h["'-k"]["i"]="-j";
h["'-k"]["j"]="i";
h["-k"]["1"] = "-k";

h["'1"]["i"]="j";
h["'1"]["j"]="j";
h["1"]["k"] = "k";

h["'-1"]["i"]="-i";
h["'-1"]["j"]="-j";
h["-1"]["k"] = "-k";

int l,x;
string s,ss;
cin >>l>>x;
cin >>ss;
loop(i,0,x) s+=ss;
string ks[]={"i","j","k"};
int c = 0;
string e,lastone,newone;
    lastone.push_back(s[i]);
for(int i = 1 ; i < s.size();i++){
    newone.push_back(s[i]);
    lastone=h[lastone][newone];
    if(lastone == ks [c])c++;
}
if(c == 3) cout<<"Yes\n";
else cout<<"No\n";
    return 0;
}
*/
