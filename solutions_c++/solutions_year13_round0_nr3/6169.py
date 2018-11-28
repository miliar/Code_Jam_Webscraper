#include<stdio.h>
#include<string.h>
#include<iostream>
#include<sstream>

using namespace std;

int arr[1001];

bool isPal(int a)
{
    stringstream ss;
    ss << a;
    string s = ss.str();
    int j = s.size() - 1;
    for(int i = 0; i<s.size()/2; i++)
    {
        if(s[i] != s[j])
            return false;
        j--;
    }
    
    return true;
}
int main(void)
{
    for(int i = 1; i<=1000; i++)
        {
            if(isPal(i)== true && isPal(i*i) == true)
            {
                if(i*i<=1000)
                    arr[i*i] = 1;
            }
        }
    int T;
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("C-small-attempt0.out", "w", stdout);
    scanf("%d",&T);
    for(int t = 0; t<T; t++)
    {
        int cnt = 0;
        int a, b;
        scanf("%d%d", &a,&b);
        for(int i = a; i<=b; i++)
        {
            if(arr[i])
            {
                cnt++;
            }
        }
        printf("Case #%d: %d\n", t + 1, cnt);
    }
    return 0;
}
