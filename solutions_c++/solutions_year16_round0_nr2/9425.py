#include<bits/stdc++.h>
using namespace std;
int main()
{
int T ;
scanf("%d",&T);
for(int t=1;t<=T;t++)
        {
           string str; cin>>str;
           int inversionNo=0;
           for(int i=1;i<str.size();i++)
               if(str[i]!=str[i-1]) inversionNo++;
           if(str[str.size()-1]=='-') inversionNo++;

           printf("Case #%d: %d\n",t,inversionNo);
        }
    return(0);
}
