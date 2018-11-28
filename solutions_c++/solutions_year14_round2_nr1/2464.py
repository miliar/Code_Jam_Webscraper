#include<iostream>
#include<string>
#include<stdio.h>
#include<stdlib.h>
#include<algorithm>
#include<vector>
#include<math.h>
#include<set>
#include<map>
using namespace std;

int main()
{
    freopen("A-small-attempt3.in","r",stdin);
    freopen("A-small-attempt3.out","w",stdout);
    int t,ti;
    cin>>ti;
    for(t=1;t<=ti;t++)
    {
        int n,i,j,flag=0;
         int k,p;
        cin>>n;
        vector<string>vs(n);
        string check1;
            for(i=0;i<n;i++)
            cin>>vs[i];
            char ch;
        int l=vs[0].size();
        for(i=0;i<l;)
        {   ch=vs[0][i];
            check1+=ch;
            while(vs[0][i]==ch)
                i++;
        }

        for(i=1;i<n;i++)
        {
           string check2;
               l=vs[i].size();
               for(j=0;j<l;)
               {
                ch=vs[i][j];
            check2+=ch;
            while(vs[i][j]==ch)
                j++;
               }
         if( check1!=check2)
         {
             flag=1; break;
         }
        }
        //for(i=0;i<s.size();i++)
          //  cout<<s[i];
        if(flag==1)
        {
           printf("\nCase #%d: Fegla Won",t);
           continue;
        }
        int si=check1.size();
         vector < vector <int > > count(si);
         for(i=0;i<si;i++){
         count[i].resize(n);
         for(j=0;j<n;j++)
             count[i][j]=0;
         }
         vector<int>pos(n,0);
         for(i=0;i<si;i++){
       for(j=0;j<n;j++)
      {
          ch=check1[i];
          int li=vs[j].size();
          k=pos[j];
        while(vs[j][k]==ch){
            count[i][j]++;k++;pos[j]++;}
          }
      }
    int ans=0;
    vector<int>avg(si);
    for(i=0;i<si;i++)
    {
        int sum=0;
        for(j=0;j<n;j++)
            sum+=count[i][j];
        avg[i]= sum/n;
    }
   ans=0;
    for(i=0;i<n;i++)
    {
        for(j=0;j<si;j++)
        {
            ans+= abs(count[j][i]-avg[j]);
        }
    }
    printf("\nCase #%d: %d",t,ans);
}
    return 0;
}
