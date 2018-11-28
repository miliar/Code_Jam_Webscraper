#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen("input.in","r",stdin);
    freopen("output.out","w",stdout);
    int T,t=1;
    scanf("%d",&T);
    while(T--)
    {
        string s1,s2,s3;
        cin>>s1;
        int i,j=0,k=0,l,len1,len2,len3;
           s2+=s1[0];

        len1=s1.size();

   for (i=1;i<len1;i++)
   {
       if (s1[i]>=s2[j])
       {
           s3=s1[i];
           s3+=s2;
           s2=s3;

       }
       else if (s1[i]<=s2[j])
       {
           s2+=s1[i];

       }
   }

cout<<"Case #"<<t<<": "<<s2<<endl;
t++;
    }
    return 0;
}
