#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output2.o","w",stdout);
    deque<char>ans;
    deque<char>::iterator it;
    int t,i,j,k;
    char  s[1100];
    char f,b;
    cin >> t;
    for(int ca=1; ca<=t; ca++)
    {
        scanf("%s",&s);
        f=b=s[0];
        k=strlen(s);
        ans.push_back(s[0]);
         //cout <<"yyy";
        for(i=1; i<k; i++)
        {
            if(s[i]>=b)
            {
                ans.push_front(s[i]);
                b=s[i];
            }
            else
            {
                ans.push_back(s[i]);
                f=s[i];
            }
        }
        printf("Case #%d: ",ca);
            for(it=ans.begin(); it!=ans.end(); it++) cout <<*it;
            cout << endl;
            ans.clear();
    }
}
