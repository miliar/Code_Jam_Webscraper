#include<bits/stdc++.h>
using namespace std;
int main()
{
    int T,i,siz,counter,j;
    string A;
    cin>>T;
    for(j=1;j<=T;++j)
    {
        cin>>A;
        siz=A.length();
        counter=1;
        for(i=1;i<siz;++i)
        {
            if(A[i]!=A[i-1])
                ++counter;
        }
        if(A[siz-1]=='+')
            printf("Case #%d: %d\n",j,counter-1);

        else
            printf("Case #%d: %d\n",j,counter);
    }
    return 0;
}
