#include <iostream>
#include <string>
#include <cstdio>

using namespace std;

int T,Smax;
int tmp_sum,answer;
string Si;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    cin >> T;
    for(int i=0;i<T;++i) {
        cin >> Smax >> Si;
        tmp_sum = answer = 0;
        for(int j=0,tmp;j<Smax;++j) {
            tmp_sum += Si[j]-48;
            if(Si[j+1]-48 == 0) continue;
            tmp = max(0,j+1-tmp_sum);
            answer += tmp;
            tmp_sum += tmp;
        }
        printf("Case #%d: %d\n",i+1,answer);
    }
    return 0;
}
