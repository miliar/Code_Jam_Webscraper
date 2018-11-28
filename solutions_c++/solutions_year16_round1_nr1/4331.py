#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main()
{
    int j, n, i;
    char dir, esq;
    scanf("%d", &n);
    for(j=0;j<n;j++) {

    string s, saida ="";

    cin>>s;

    vector<char> v;

    esq = dir = s[0];
    saida += s[0];
    for(i=1;i<s.size();i++)
    {
        if(s[i]>=esq)
        {
            esq = s[i];
            v.push_back(s[i]);
        }
        if(s[i] < esq)
        {
            saida += s[i];
        }
    }
    printf("Case #%d: ", j+1);
    for(i=v.size() -1 ;i>=0;i--)
        printf("%c", v[i]);

    cout<<saida<<endl;


    }
    return 0;
}
