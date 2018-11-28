#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<fstream>
using namespace std;
int a[1005] = {0};
int b[1005] = {0};
int lowbit(int t)
{
    return t & ( t ^ ( t - 1 ) );
}
void add(int pos , int num)
{
    while(pos <= 1000)
    {
          b[pos] += num;
          pos += lowbit(pos);
    }
}
int Sum(int i)
{
    int sum = 0;
    while(i> 0)
    {
        sum += b[i];
        i -= lowbit(i);
    }
    return sum;
}

int main()
{
    int T,n,m;
    a[1] = 1;
    a[4] = 1;
    a[9] = 1;
    a[121] = 1;
    a[484] = 1;
    int i,j,k = 1;
    ifstream cin("C-small-attempt1.in");
    ofstream cout("C-small-attempt1.out");
    cin >> T;
    for(i = 1; i <= 1005; i++)
    {
        add(i,a[i]);
    }
    while(T--)
    {
        cin >> n >> m;

        cout <<"Case #"<< k++ << ": " <<Sum(m) - Sum(n-1) << endl;
    }
    return 0;
}
