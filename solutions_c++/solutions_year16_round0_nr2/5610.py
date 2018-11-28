#include <iostream>
#include<bits/stdc++.h>
#include<string>
using namespace std;

int main()
{
   long int T=0,ans,curr;
   string s,temp;
   //cin>>T;

   int i,j,k,flag;
     ifstream ob;
    ob.open("B-large.in");
    ofstream ot;
    ot.open("out.txt");
    getline(ob,temp);
    for(i=0;i<temp.length();i++)
    {
        T*=10;
        T+=(temp[i]-48);

    }
    //ob>>T;
   for(i=1;i<=T;i++)
   {
       //cin>>s;
       //cout<<s;
       getline(ob,s);
       ans=0;

             flag=0;
            for(j=s.length()-1;j>=0;j--)
            {
                if(s[j]=='-')
                {
                    flag=1;
                    break;
                }
            }
            curr=j;
            while(flag==1)
            {

                if(s[curr]=='-')
                {
                    for(j=0;j<=curr;j++)
                    {
                        if(s[j]=='-')
                            s[j]='+';
                        else
                            s[j]='-';
                    }

                }
                flag=0;
                for(k=curr-1;k>=0;k--)
                {
                    if(s[k]=='-')
                    {
                        flag=1;
                        break;
                    }
                }
                   if(flag==1)
                        curr=k;
                   ans+=1;
                   if(k==0)//only last single char left
                    {
                        ans+=1;
                        flag=0;
                    }

            }

                //cout<<"Case #"<<i<<": "<<ans<<"\n";
                ot<<"Case #"<<i<<": "<<ans<<"\n";


   }
   ob.close();
   ot.close();
   return 0;
}
