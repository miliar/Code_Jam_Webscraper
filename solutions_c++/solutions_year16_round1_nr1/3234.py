#include<cstdio>
#include<cstring>
#include<deque>

using namespace std;

deque<char> d;

int main()
{
    int T;
    char S[1000+1];
    scanf("%d", &T);
    for(int i=0; i<T; ++i)
    {
        int l;
        if(!d.empty()) d.clear();
        scanf("%s", &S);
        l = strlen(S);
        d.push_back(S[0]);
        for(int j=1; j<l; ++j)
        {
            if(S[j]>=d.front()) d.push_front(S[j]);
            else d.push_back(S[j]);
        }
        printf("Case #%d: ", i+1);
        for(int j=0; j<l; ++j)
        {
            printf("%c", d.front());
            d.pop_front();
        }
        printf("\n");
    }
    return 0;
}
