#include<iostream>
#include<cstdio>
#include<cstring>
#include<string>
using namespace std;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout);

    int T;
    cin>>T;
    for (int j = 1; j<= T; j++)
    {
        char pancake[120];
        cin>>pancake;

        int l = strlen(pancake);
        int ans = 0;
        char temp = pancake[0];
        for (int i = 1; i < l; i++)
        {
            if (pancake[i] == temp);
            else if (temp == '+') {
                ans++;
                temp = '-';
            }
            else if (temp == '-') {
                ans++;
                temp ='+';
            }
        }
        if (temp == '-') ans++;
        cout<<"Case #"<<j<<": "<<ans<<endl;

    }

    fclose(stdin);
    fclose(stdout);
}
