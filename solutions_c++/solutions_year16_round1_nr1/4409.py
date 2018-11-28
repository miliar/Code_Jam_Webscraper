#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("word_in.txt", "r", stdin);
    freopen("word_out.txt", "w", stdout);
   int m=1,t;
   cin >> t;
   while(t--)
   {
        string s;
        cin >> s;
        char v1[10007];
        char v2[10007];
       v1[0]=s[0];
       int l1=1,l2=0;
       for(int i=1;i<s.length();i++)
       {
           if((s[0]-s[i])>0)
           {
             v1[l1]=s[i];
             l1++;
           }
           else
           {
               v2[l2]=s[i];
               s[0]=s[i];
               l2++;
           }
       }
       printf("Case #%d: ",m);
       for(int i=l2-1;i>=0;i--)
         cout << v2[i];
       for(int i=0;i<l1;i++)
         cout << v1[i];
       cout << endl;
       m++;
   }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
