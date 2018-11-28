#include<iostream>
#include<fstream>
using namespace std;
int main()
{
    freopen("largeb.in", "r", stdin);
    freopen("bout.txt", "w", stdout);
    int t;
    scanf("%d",&t);
    for(int in =1; in <=t;in++)
    {
        char s[105]={'\0'};
        scanf("%s",s);
        printf("Case #%d: ",in);
        int cnt =0;
        for(int i=0;s[i]!='\0';i++)
        {
            //cout << "true\n";
            if(s[i]=='-')
            {
                if(i==0)cnt++;
                else if(s[i-1]=='+')cnt+=2;
            }
        }
        printf("%d\n",cnt);

    }
}

