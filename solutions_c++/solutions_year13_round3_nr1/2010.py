#include <algorithm>
#include <functional>
#include <numeric>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <cassert>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <sstream>
using namespace std;

#define LL long long
#define LD long double
#define PR pair<int,int>

#define For(i,n) for (i=0; i<int(n); i++)
#define ForR(i,n) for (i=int(n)-1; i>=0; i--)
#define Sz(s) int((s).size())
#define All(s) (s).begin(),(s).end()
#define Fill(s,v) memset(s,v,sizeof(s))

char letter[100];
int value;
char conL[100];
int len;

void ini()
{
    Fill(conL,0);
    int flag=0;
    int i;
    For(i,len)
    {
        if(letter[i] == 'a' || letter[i] == 'e' ||letter[i] == 'i' ||letter[i] == 'o' ||letter[i] == 'u')
        {
            flag = 0;
        }
        else
        {
            if(flag<value-1)
                flag++;
            else if(flag==value-1)
            {
                conL[i] = 1;
                flag++;
            }
            else if(flag==value)
            {
                conL[i] = 1;
            }
        }
    }
}

int make()
{
    int res=0;
    int i,begin=value-1;
    for(;begin < len;begin++)
    {
        for(i=begin;i<len;i++)
        {
            if(conL[i]==1)
            {
                res = res + (len-i);
                break;
            }
        }
    }
    return res;
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt","w",stdout);
    
    int num,i;
    cin >> num;
    char t;
    cin >> t;
    for(i=0;i<num;i++)
    {
        cout << "Case #" << i+1 << ": ";
       
        len=0;
        
        while(t>='a'&&t<='z')
        {
            letter[len] = t;
            len++;
            cin >> t;
        }
        value = t - '0';
        if(!cin.eof())
            cin >> t;
        while(t>='0'&&t<='9')
        {
            value = 10*value + t - '0';
            if(!cin.eof())
                cin >> t;
            else
            {
                value = value/10;
                break;
            }
        }
         
        ini();
        int res = make();
        cout << res <<endl;
        
    }
    return 0;
    
}