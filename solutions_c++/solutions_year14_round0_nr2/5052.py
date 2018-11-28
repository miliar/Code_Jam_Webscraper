#include <iostream>
#include <cstring>
#include <queue>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
#include <cstdlib>
#include <cstdio>
#include <set>
using namespace std;

const int N = 200000;

struct Item
{
    int user_id;
    int brand_id;
    int type;
    int time;
    Item(int a=0, int b=0, int c=0, int d=0)
    {
        user_id = a;
        brand_id = b;
        type = c;
        time = d;
    }
} item[N];

struct UB
{
    int u;
    int b;
    UB(int s=0, int t=0)
    {
        u = s;
        b = t;
    }
    friend bool operator <(UB A, UB B)
    {
        if(A.u != B.u)
            return A.u < B.u;
        else return A.b < B.b;
    }
};

int f[13];
void init()
{
    f[1]=f[3]=f[5]=f[7]=f[8]=f[10]=f[12]=31;
    f[2]=28;
    f[4]=f[6]=f[9]=f[11]=30;
    for(int i=1; i<=12;i++)
        f[i] += f[i-1];
    return ;
}

int tran_time(char *str)
{
    char s[20];
    int j=0;
    int i=0;
    int ret = 0;
    int time = 0;
    while(str[i] < '0' || str[i] > '9')
        i++;
    for(; str[i]; i++)
    {
        if(str[i]>='0' && str[i]<='9')
        {
            s[j++] = str[i];
        }
        else if(j != 0 && time == 0)
        {
            s[j++] = '\0';
            j = 0;
            ret += f[atoi(s)-1];
            time++;
        }
    }
    return ret + atoi(s);
}
/**
bool cmp(Item A, Item B)
{
    if(A.user_id != B.user_id)
    {
        return A.user_id < B.user_id;
    }
    else if(A.brand_id != B.brand_id)
    {
        return A.brand_id < B.brand_id;
    }
    else if(A.time != B.time)
    {
        return A.time < B.time;
    }
    else return A.type < B.type;
}
*/
bool cmp(Item a,Item b) {
    if(a.user_id == b.user_id) {
        if(a.brand_id == b.brand_id) {
            if(a.time == b.time) {
                return a.type < b.type;
            }
            return a.time < b.time;
        }
        return a.brand_id < b.brand_id;
    }
    return a.user_id < b.user_id;
}

int main()
{
    init();
    char input[100] = "input.csv";
    char output[100] = "out.csv";
    freopen(input, "r", stdin);
    freopen(output, "w", stdout);


    map<int,int>user;
    map<int,int>brand;
    map<UB,int>ub;

    int n_user = 0;
    int n_brand = 0;
    int n_ub = 0;

    char str[200];
    Item temp;
    char *p;
    int n = 0;
    while(gets(str))
    {
        p = strtok(str, ",");
        for(int i=0; i<4; i++)
        {
            if(i == 0)
            {
                int u = atoi(p);
                if(user.count(u) == 0)
                {
                    user[u] = n_user++;
                }
                ///item[n].user_id = user[u];
                item[n].user_id = u;
            }

            else if(i == 1)
            {
                int b = atoi(p);
                if(brand.count(b) == 0)
                {
                    brand[b] = n_brand++;
                }
                ///item[n].brand_id = brand[b];
                item[n].brand_id = b;
                if(ub.count(UB(item[n].user_id,item[n].brand_id)) == 0)
                {
                    ub[UB(item[n].user_id,item[n].brand_id)] = n_ub++;
                }
            }

            else if(i == 2)
            {
                int a = atoi(p);
                if(a == 1) a = 3;
                else if(a == 2) a = 1;
                else if(a == 3) a = 2;
                else a = 0;
                item[n].type = a;
            }
            else
            {
                item[n].time = tran_time(p);
            }
            p = strtok(NULL, ",");
        }
        n++;
    }
    sort(item, item+n, cmp);
    for(int i=0; i<n; i++)
    {
        printf("%d,%d,%d,%d\n", item[i].user_id, item[i].brand_id, item[i].type, item[i].time);
    }
    return 0;
}

/*
while(p)

{

printf("%s\n", p);

p = strtok(NULL, ",");

}
*/
