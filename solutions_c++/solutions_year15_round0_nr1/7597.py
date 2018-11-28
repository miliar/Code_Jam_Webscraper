#include<iostream>
using namespace std;
#define MAX 1000
int main()
{
    int i,j, t, m, cnt, standing;
    cin>>t;
    char a[MAX+1];
    int s[MAX+1];
    for(j=0;j<t;j++)
    {
        cnt = 0;
        cin>>m;
        cin>>a;
        for(i=0;i<=m;i++)
        {
            s[i] = a[i] - '0';
        }
        standing = s[0];
        for(i=1;i<=m;i++)
        {
            if(standing<i && s[i])
            {
                cnt = cnt + i - standing;
                standing = i+ s[i];

            }
            else
            {
                standing = standing + s[i];
            }

        }
        cout<<"Case #"<<j+1<<": "<<cnt<<"\n";
    }
}


