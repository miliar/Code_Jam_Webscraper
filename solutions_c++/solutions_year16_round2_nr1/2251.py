#include <stdio.h>
#include <string>
#include <string.h>
#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <stack>
#include <limits.h>
#include <math.h>
#include <iomanip>
#include <bitset>
using namespace std;
#pragma comment(linker, "/STACK:102400000,102400000")
typedef long long LL;
typedef pair<int,int> pii;
#define CLR(x,y) memset(x,y,sizeof(x));
#define PB push_back
#define MP make_pair
#define FOR(i,x,y) for(int i = (x) ; i < (y) ; ++i)
#define ROF(i,x,y) for(int i = (y)-1 ; i >= (x); --i)
#define FORG(i,x,g) for(int i = g.head[(x)] ; ~i ; i = g.next[i])
#define INF 0x3f3f3f3f

inline LL getint()
{
    int c;
    while(c=getchar(),(c<'0'||c>'9')&&(c!='-')&&(c!=EOF));
    if(c==EOF)return -1;
    bool flag=(c=='-');
    if(flag)
        c=getchar();
    LL x=0;
    while(c>='0'&&c<='9')
    {
        x = (x<<3)+x+x+c-'0';
        c=getchar();
    }
    return flag?-x:x;
}
inline void writeln(LL x)
{
    if(x<0)
    {
        putchar('-');
        x=-x;
    }
}
const int MAXN = 30;
int a[MAXN][MAXN];//�������
int x[MAXN];//�⼯
bool free_x[MAXN];//����Ƿ��ǲ�ȷ���ı�Ԫ



/*
void Debug(void)
{
    int i, j;
    for (i = 0; i < equ; i++)
    {
        for (j = 0; j < var + 1; j++)
        {
            cout << a[i][j] << " ";
        }
        cout << endl;
    }
    cout << endl;
}
*/


inline int gcd(int a,int b)
{
    int t;
    while(b!=0)
    {
        t=b;
        b=a%b;
        a=t;
    }
    return a;
}
inline int lcm(int a,int b)
{
    return a/gcd(a,b)*b;//�ȳ���˷����
}

// ��˹��Ԫ���ⷽ����(Gauss-Jordan elimination).(-2��ʾ�и������⣬���������⣬
//-1��ʾ�޽⣬0��ʾΨһ�⣬����0��ʾ����⣬���������ɱ�Ԫ�ĸ���)
//��equ�����̣�var����Ԫ�������������Ϊequ,�ֱ�Ϊ0��equ-1,����Ϊvar+1,�ֱ�Ϊ0��var.
int Gauss(int equ,int var)
{
    int i,j,k;
    int max_r;// ��ǰ���о���ֵ������.
    int col;//��ǰ�������
    int ta,tb;
    int LCM;
    int temp;
    int free_x_num;
    int free_index;

    for(int i=0;i<=var;i++)
    {
        x[i]=0;
        free_x[i]=true;
    }

    //ת��Ϊ������.
    col=0; // ��ǰ�������
    for(k = 0;k < equ && col < var;k++,col++)
    {// ö�ٵ�ǰ�������.
// �ҵ���col��Ԫ�ؾ���ֵ�����������k�н���.(Ϊ���ڳ���ʱ��С���)
        max_r=k;
        for(i=k+1;i<equ;i++)
        {
            if(abs(a[i][col])>abs(a[max_r][col])) max_r=i;
        }
        if(max_r!=k)
        {// ���k�н���.
            for(j=k;j<var+1;j++) swap(a[k][j],a[max_r][j]);
        }
        if(a[k][col]==0)
        {// ˵����col�е�k������ȫ��0�ˣ�����ǰ�е���һ��.
            k--;
            continue;
        }
        for(i=k+1;i<equ;i++)
        {// ö��Ҫɾȥ����.
            if(a[i][col]!=0)
            {
                LCM = lcm(abs(a[i][col]),abs(a[k][col]));
                ta = LCM/abs(a[i][col]);
                tb = LCM/abs(a[k][col]);
                if(a[i][col]*a[k][col]<0)tb=-tb;//��ŵ���������
                for(j=col;j<var+1;j++)
                {
                    a[i][j] = a[i][j]*ta-a[k][j]*tb;
                }
            }
        }
    }

  //  Debug();

    // 1. �޽�����: ������������д���(0, 0, ..., a)��������(a != 0).
    for (i = k; i < equ; i++)
    { // �����������˵�����Ҫ�ж���Щ�����ɱ�Ԫ����ô�����б任�еĽ����ͻ�Ӱ�죬��Ҫ��¼����.
        if (a[i][col] != 0) return -1;
    }
    // 2. ���������: ��var * (var + 1)���������г���(0, 0, ..., 0)�������У���˵��û���γ��ϸ����������.
    // �ҳ��ֵ�������Ϊ���ɱ�Ԫ�ĸ���.
    if (k < var)
    {
        // ���ȣ����ɱ�Ԫ��var - k��������ȷ���ı�Ԫ������var - k��.
        for (i = k - 1; i >= 0; i--)
        {
            // ��i��һ��������(0, 0, ..., 0)���������Ϊ�����������ڵ�k�е���equ��.
            // ͬ������i��һ��������(0, 0, ..., a), a != 0��������������޽��.
            free_x_num = 0; // �����жϸ����еĲ�ȷ���ı�Ԫ�ĸ������������1�������޷���⣬������ȻΪ��ȷ���ı�Ԫ.
            for (j = 0; j < var; j++)
            {
                if (a[i][j] != 0 && free_x[j]) free_x_num++, free_index = j;
            }
            if (free_x_num > 1) continue; // �޷�����ȷ���ı�Ԫ.
            // ˵����ֻ��һ����ȷ���ı�Ԫfree_index����ô���������ñ�Ԫ���Ҹñ�Ԫ��ȷ����.
            temp = a[i][var];
            for (j = 0; j < var; j++)
            {
                if (a[i][j] != 0 && j != free_index) temp -= a[i][j] * x[j];
            }
            x[free_index] = temp / a[i][free_index]; // ����ñ�Ԫ.
            free_x[free_index] = 0; // �ñ�Ԫ��ȷ����.
        }
        return var - k; // ���ɱ�Ԫ��var - k��.
    }
    // 3. Ψһ������: ��var * (var + 1)�����������γ��ϸ����������.
    // �����Xn-1, Xn-2 ... X0.
    for (i = var - 1; i >= 0; i--)
    {
        temp = a[i][var];
        for (j = i + 1; j < var; j++)
        {
            if (a[i][j] != 0) temp -= a[i][j] * x[j];
        }
        if (temp % a[i][i] != 0) return -2; // ˵���и������⣬����������.
        x[i] = temp / a[i][i];
    }
    return 0;
}
const int L = 3000;
int n;
int T;
char buff[L];
int cnt[MAXN];
string words[] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};

void init() {
    CLR(a,0)
    CLR(cnt,0)
    FOR(i,0,10) {
        FOR(j,0,words[i].size()) {
            ++a[words[i][j]-'A'][i];
        }
    }
}


void solve(char s[]) {
    int l = strlen(s);
    FOR(i,0,l) {
        ++cnt[s[i]-'A'];
    }
    FOR(i,0,26)
        a[i][10] = cnt[i];
    int var = 10;
    int equ = 26;
//    printf("\n");
//    FOR(i,0,26) {
//        FOR(j,0,11)
//            printf("%d",a[i][j]);
//        printf("\n");
//    }
    Gauss(equ,var);
}
void print(int cas) {
    printf("Case #%d: ",cas);
    FOR(i,0,10) {
        FOR(j,0,x[i])
            printf("%d",i);
    }
    puts("");
}
int main(void)
{
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    scanf("%d",&T);
    for(int cas = 1 ; cas <= T ; ++cas) {
        init();
        scanf(" %s",buff);
        solve(buff);
        print(cas);
    }
    return 0;
}
