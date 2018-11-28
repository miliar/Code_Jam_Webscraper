#include <bits/stdc++.h>
using namespace std;
string s, j;
string anss,ansj;
int mini = 9999999;
void evaluate(string a,string b)
{
    int a1 = 0;
    int b1 = 0;
    int len = s.length();
    //cout<<"fes"<<endl;
    for(int i = 0;i<len;i++)
    {
        a1+=(a[i]-48)*pow(10,len-i-1);
        b1+=(b[i]-48)*pow(10,len-i-1);


    }

   // cout<<a1<<" "<<b1<<endl;
    int diff = abs(a1-b1);
    if(diff < mini)
        {
            mini = diff;
            anss = a;
            ansj = b;
            return;
        }
    if(diff == mini)
    {
        if(a < anss)
        {
            anss = a;
            ansj = b;
        }
        else if(a == anss)
        {
            if(b < ansj)
            {
                ansj = b;
            }
        }
    }


}
void go(string s1,string j1,int k)
{
    int len = s.length();
    while(s[k] != '?' && j[k] != '?' && k<len)
       {
           s1+=s[k];
           j1+=j[k];
           k++;
       }
    if(k == len)
    {
        evaluate(s1,j1);
    }

           if(s[k] == '?' && j[k] == '?')
           {
               for(char h = '0';h<='9';h++)
               {
                   for(char f = '0';f<='9';f++)
                   {
                       go(s1+h,j1+f,k+1);
                   }
               }
           }
           else if(s[k] == '?')
           {
               for(char h = '0';h<='9';h++)
               {
                   go(s1+h,j1+j[k],k+1);
               }
           }
            else if(j[k] == '?')
           {
               for(char h = '0';h<='9';h++)
               {
                   go(s1+s[k],j1+h,k+1);
               }
           }

}
int main()
{
   int n;
   cin>>n;
   for(int i = 1;i<=n;i++)
   {

       cin>>s>>j;
       mini = 9999999;
       string s1 = "",j1 = "";
       go(s1,j1,0);




       cout<<"Case #"<<i<<": ";
       cout<<anss<<" "<<ansj<<endl;

   }

}
