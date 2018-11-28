#include <iostream>
using namespace std;

int main()
{
    int k=0;
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t;
    scanf("%d",&t);
    while(t--)
    {
        k++;
        int sm;
        scanf("%d",&sm);
        string s;
        cin>>s;
        int c,count=0,added=0;
        //char a=s[0];
        count+=(int)(s[0]-'0');
        for(int i=1;i<=s.length();i++)
        {
            c=(int)(s[i]-'0');
            if(i>count)
            {
                added+=i-count;
                count+=i-count;
            }
            count+=(int)(s[i]-'0');
        }
        
        printf("Case #%d: %d\n",k,added);
    }
}