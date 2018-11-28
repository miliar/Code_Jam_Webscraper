#include <iostream>
#include<bits/stdc++.h>
using namespace std;

int main()
{
    FILE *fin = freopen("A-large-attempt0.in.txt", "r", stdin);
	assert( fin!=NULL );
	FILE *fout = freopen("A-large.out.txt", "w", stdout);

    char s[1000],ans[2000];
    int t;
    cin>>t;
    for(int i=1;i<=t;i++)
    {
        cin>>s;

        if(strlen(s)==1)
        {
            cout << "Case #" << i << ": " <<s<< endl;
            continue;
        }
        int l=strlen(s);
        int up=1000,lo=1000;
        for(int j=0;j<l;j++)
        {
            if(j==0)
            {
                ans[up]=s[0];
            }
            else
            {
                if(s[j]>=ans[lo])
                {
                    ans[--lo]=s[j];
                }
                else if(s[j]<ans[lo])
                {
                    ans[++up]=s[j];
                }
            }
        }
        cout << "Case #" << i << ": ";
        for(int k=lo;k<=up;k++)
        {
            cout<<ans[k];
        }
        cout<<endl;
    }
    return 0;
}
