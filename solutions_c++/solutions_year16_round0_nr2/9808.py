#include <bits/stdc++.h>

using namespace std;


int ans(string u)
{
    int l=u.length();

if(l==0)
    return 0;
    int i;
    int cnt=0;
    int g=0;
   if(u[l-1]=='+')
   {
       int cnt=0;
       int rit=l-1;
       while(u[rit]=='+')
       {
           cnt++;
           rit--;
       }
     g= ans(u.substr(0,l-cnt));
     return g;
   }
   else {
    int cnt1=0,cnt2=0,kj=0;
    int pos=0;
    if(u[0]=='+')
    {

        for(i=0;i<l;i++){


if((u[i]=='+')&&(kj==0)){
            while((u[i]=='+'))
            {
                cnt1++;
            i++;
            }
            i--;
            }
            else if(u[i]=='-')
            {
                cnt2++;
                pos=i;
            }
            else
                break;
                kj=1;

        }
        string h="";

        for(i=l-1;i>pos;i--)
        {
            if(u[i]=='+')
                h=h+"-";
            else
                h=h+"+";
        }
        g=2+ans(h);
return g;
    }
    else
    {
        int cnty=0;
        int pos=0;
        for(i=0;i<l;i++)
        {
            if(u[i]=='-'){
            cnty++;
            pos=i;
            }
            else
                break;
        }

        string h="";
            for(i=l-1;i>pos;i--)
        {
            if(u[i]=='+')
                h=h+"-";
            else
                h=h+"+";
        }
        g=1+ans(h);
        return g;
    }




   }





}


int main()
{

   int t;
   int r=1;
   cin>>t;
   //freopen("new.txt","w",stdout);
   while(t--){

    string s;
    cin>>s;
   cout<<"Case #"<<r<<": "<<ans(s)<<endl;
r++;





   }

//fclose(stdout);


    return 0;
}
