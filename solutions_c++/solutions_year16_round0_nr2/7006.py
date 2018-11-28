#include<string>
#include<cstdio>
#include<iostream>
using namespace std;

int main(){
    int t;
    int i,n;
    long long int j;
    string S;
    long long int count;
    scanf("%d\n",&t);
    for (i=1;i<=t;i++)
    {
        count = 0;
        S.clear();
        getline(cin,S);
        printf("Case #%d: ",i);
        for (j=0;j<S.size();j++)
        {
            if (S[j] == '-' && S[j+1] == '+')
                count += 1;
            if (S[j] == '-' && j+1 == S.size())
                count += 1;
            if (S[j] == '+' && S[j+1] == '-')
                count += 1;
        }
        printf("%lld\n",count);
    }
}
