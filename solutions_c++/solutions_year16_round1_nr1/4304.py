#include<bits/stdc++.h>
using namespace std;
char a[1005];
int main ()
{
    int m;
    cin>>m;
   for (int kl = 1; kl<= m; kl++)
   {
        scanf("%s", a);
        int n=strlen(a);
        string b="";
        b+=a[0];
        for (int i=1;i<n;i++)
        {
            if (a[i] >= b[0]) b=a[i]+b;
                else
                    b+=a[i];
        }
       printf("Case #%i: ", kl);
      cout<<b<<endl;
        
   }
    
	return 0;
}