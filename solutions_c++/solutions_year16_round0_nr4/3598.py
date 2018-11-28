#include<iostream>
#include<cstdio>
using namespace std;

int main()
{
    freopen("D-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);

    int T;
    cin>>T;
    for (int i = 1; i <= T; i++)
    {
        int k,c,s;
        cin >> k >> c >> s;

        cout<<"Case #"<<i<<": ";
        for (int j = 1; j <= s; j++)
            cout<<j<<" ";
        cout<<endl;
    }

    fclose(stdin);
    fclose(stdout);
}
