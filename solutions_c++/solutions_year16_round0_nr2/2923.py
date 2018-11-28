#include<bits/stdc++.h>
using namespace std;
char str[110];
int main()
{
    //freopen("B-large.in","r",stdin);
    //freopen("out.txt","w",stdout);
    int T,Case=1;
    cin>>T;
    while(T--)
    {
        printf("Case #%d: ",Case++);
        scanf("%s",str);
        int le=strlen(str),num=0;
        for(int i=0;i<le;i++)
        {
            if(str[i]=='-') {
                num++;
                while(str[i]=='-'&&i<le) {
                    i++;
                }
                i--;
            }
        }
        num*=2;
        if(str[0]=='-') num--;
        cout<<num<<endl;
    }
    return 0;
}
