#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cmath>
#include<vector>
#include<set>
#include<map>
#include<algorithm>
#include<utility>
#include<iostream>
#include<string>
using namespace std;

bool p[100000007];
vector<int> prime;

int J,N;
int countJ;


void init()
{
    prime.clear();    
    memset(p, true, sizeof(p));
    p[0]=false;
    p[1]=false;
    
    for(int i=2; i<100000007;++i)
    {
        if(p[i]==true)
        {
            prime.push_back(i);           
        }
        else
            continue;
        for(int j=i+i;j<100000007;j+=i)
            p[j] = false;
    }
    /*
    printf("Prime SIZE : %d\n", (int)prime.size());
    for(int i=0;i<100;++i)
        printf(" %d", prime[i]);
    printf("\n");
    */
}

inline bool isPrime(const string& input, int base)
{
    long long value = 0LL;
    for(int i=0;i<input.length();++i)
    {
        value = value*base + (input[i] - '0');
    }

    if(value < 100000007LL)
        return !p[(int)value];
    int root = (int)sqrt(value) + 1;;
    for(int i=0;i<prime.size() && prime[i]<=root;++i)   
        if(value%prime[i]==0)
            return true;;
    return false;
}

inline void showAll(const string& input)
{
    for(int k=2;k<11;++k)
    {
        long long value = 0LL;
        for(int i=0;i<input.length();++i)
        {
            value = value*k + (input[i] - '0');
        }
        for(int j=0;j<prime.size();++j)
            if((value%prime[j])==0LL)
            {
                printf(" %d", prime[j]);
                break;
            }
    }
    printf("\n");
}

inline bool isValid(const string& input)
{
    for(int i=2;i<11;++i)
    {
        if(isPrime(input, i)==false)
        {
            //cout << input << " " << i << endl;
            return false;
        }
    }
    return true;
}

void dfs(int sz, const string& input)
{
    if(countJ >= J) return;
    if(sz==N-2)
    {
        string target = "1" + input + "1";
        //cout << target << endl;
        if(isValid(target))
        {
            printf("%s", target.c_str());
            showAll(target);
            countJ++;
            if(countJ >= J) return;
        }
        return;
    }
    dfs(sz + 1, input+"0");
    dfs(sz + 1, input+"1");
}

int main()
{
    int T;
    init();
    scanf("%d", &T);
    for(int i=1;i<T+1;++i)
    {
        scanf("%d%d", &N, &J);
        countJ = 0;
        printf("Case #%d:\n", i);
        dfs(0, "");
    }
    return 0;
}
