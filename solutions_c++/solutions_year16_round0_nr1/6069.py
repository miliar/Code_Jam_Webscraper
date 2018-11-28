#include<cstdio>
#include<algorithm>
#include<iostream>
#include<cstring>
#include<set>
using namespace std;

int t,num,kount;

void solve()
{
    set <int> p;
    int k = 2;
    int temp1 = num;
    int temp2 = num;
    while(num!=0){
        temp2 = temp1;
        while(temp2 != 0){
            p.insert(temp2%10);
            temp2 /= 10;
            //cout << "***"<<p.size() << endl;
        }
        if(p.size()== 10) break;
        temp1 = num;
        temp1 *= k;
        k++;
    }
    if( num == 0) printf("Case #%d: INSOMNIA\n",++kount);
    else
        printf("Case #%d: %d\n",++kount,temp1);
}

int main()
{
    freopen("A-small-attempt6.in","r",stdin);
    freopen("1.out","w",stdout);
    scanf("%d",&t);
    while(t--){
        scanf("%d",&num);
        solve();
    }
    return 0;
}
