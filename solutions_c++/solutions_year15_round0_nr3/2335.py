#include <iostream>
#include <fstream>
#include <algorithm>
#include <math.h>
#include <queue>
#include <string>
#include <vector>
#include <unordered_map>


const int SIZE = 10002;
const int LEN = 10002;
char table[SIZE][SIZE];
bool sign[SIZE][SIZE];
char line[LEN];


char cal_value(char a, char b)
{
    if(a == '1')
    {
        return b;
    }
    if(b == '1')
    {
        return a;
    }
    if(a == 'i')
    {
        if(b == 'i')
        {
            return '1';
        }
        else if(b == 'j')
        {
            return 'k';
        }
        else if(b == 'k')
        {
            return 'j';
        }
    }
    else if(a == 'j')
    {
        if(b == 'i')
        {
            return 'k';
        }
        else if(b == 'j')
        {
            return '1';
        }
        else if(b == 'k')
        {
            return 'i';
        }
    }
    else if(a == 'k')
    {
        if(b == 'i')
        {
            return 'j';
        }
        else if(b == 'j')
        {
            return 'i';
        }
        else if(b == 'k')
        {
            return '1';
        }
    }
    return '?';
}


bool cal_sign(bool a_sign, bool b_sign, char a, char b)
{
    int count_false = 0;
    if(!a_sign)
    {
        count_false ++;
    }
    if(!b_sign)
    {
        count_false ++;
    }
    if(a == 'i' && (b == 'i' || b == 'k'))
    {
        count_false ++;
    }
    else if(a == 'j' && (b == 'i' || b == 'j'))
    {
        count_false ++;
    }
    else if(a == 'k' && (b == 'j' || b == 'k'))
    {
        count_false ++;
    }
    return count_false % 2 == 0;
}


int main()
{
    //freopen("/Users/guanxiong/Documents/documents/google_code_jam/2015qualification/dijkstra/C-small-attempt2.in","r",stdin);
    //freopen("/Users/guanxiong/Documents/documents/google_code_jam/2015qualification/dijkstra/C-small-attempt2.out","w",stdout);
    int cases;
    scanf("%d", &cases);
    int len, times, total_len;
    for(int case_num = 1; case_num <= cases; case_num ++)
    {
        scanf("%d%d", &len, &times);
        getchar();
        gets(line);
        total_len = len * times;
        if(total_len < 3)
        {
            printf("Case #%d: NO\n", case_num);
            continue;
        }
        char value = '1';
        bool sign = true;
        int pos = 0;
        while(pos < total_len)
        {
            char curr = line[pos%len];
            char new_value = cal_value(value, curr);
            bool new_sign = cal_sign(sign, true, value, curr);
            if(new_value == 'i' && new_sign)
            {
                break;
            }
            value = new_value;
            sign = new_sign;
            pos++;
        }
        if(pos == total_len)
        {
            printf("Case #%d: NO\n", case_num);
            continue;
        }
        pos++;
        value = '1';
        sign = true;
        while(pos < total_len)
        {
            char curr = line[pos%len];
            char new_value = cal_value(value, curr);
            bool new_sign = cal_sign(sign, true, value, curr);
            if(new_value == 'j' && new_sign)
            {
                break;
            }
            value = new_value;
            sign = new_sign;
            pos++;
        }
        if(pos == total_len)
        {
            printf("Case #%d: NO\n", case_num);
            continue;
        }
        pos++;
        value = '1';
        sign = true;
        while(pos < total_len)
        {
            char curr = line[pos%len];
            char new_value = cal_value(value, curr);
            bool new_sign = cal_sign(sign, true, value, curr);
            if(new_value == 'k' && new_sign)
            {
                break;
            }
            value = new_value;
            sign = new_sign;
            pos++;
        }
        if(pos == total_len)
        {
            printf("Case #%d: NO\n", case_num);
            continue;
        }
        pos++;
        value = '1';
        sign = true;
        while(pos < total_len)
        {
            char curr = line[pos%len];
            char new_value = cal_value(value, curr);
            bool new_sign = cal_sign(sign, true, value, curr);
            value = new_value;
            sign = new_sign;
            pos++;
        }
        if(value != '1' || !sign)
        {
            printf("Case #%d: NO\n", case_num);
            continue;
        }
        printf("Case #%d: YES\n", case_num);
    }
    return 0;
}

