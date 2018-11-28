#include<bits/stdc++.h>
using namespace std;
int main()
{
    ifstream fin;
    ofstream fout("ans.txt");
    fin.open ("input1.txt");

    if(!fin.is_open())
    {
        cout<<"file error";
    }
int t;
fin>>t;
int x=1;
while(t--)
{

long long int ch[26],nu[10];
for(int i=0;i<26;i++)
ch[i]=0;
for(int i=0;i<10;i++)
nu[i]=0;
   string s;
   fin>>s;
   for(int i=0; i<s.length();i++)
   {
      int m=s[i];
      ch[m-65]++;
   }
   while(ch[25]>0)
   {
    ch[4]--;
    ch[17]--;
    ch[14]--;
    ch[25]--;
   nu[0]++;
   }
while(ch[22]>0)
   {
    ch[19]--;
    ch[22]--;
    ch[14]--;

    nu[2]++;
   }

   while(ch[20]>0)
   {
    ch[20]--;
    ch[5]--;
    ch[14]--;
    ch[17]--;
    nu[4]++;
   }
    while(ch[14]>0)
   {
    ch[14]--;
    ch[13]--;
    ch[4]--;

    nu[1]++;
   }
    while(ch[23]>0)
   {
    ch[8]--;
    ch[18]--;
    ch[23]--;
    nu[6]++;
   }
 while(ch[6]>0)
   {
    ch[4]--;
    ch[8]--;
    ch[6]--;
    ch[7]--;
    ch[19]--;
    nu[8]++;
   }
   while(ch[7]>0)
   {
    ch[19]--;
    ch[17]--;
    ch[7]--;
    ch[4]-=2;
    nu[3]++;
   }
   while(ch[5]>0)
   {
    ch[5]--;
    ch[8]--;
    ch[21]--;
    ch[4]--;
    nu[5]++;
   }
    while(ch[18]>0)
   {
    ch[18]--;
    ch[4]-=2;
    ch[21]--;
    ch[13]--;
    nu[7]++;
   }

   while(ch[13]>0)
   {
    ch[13]-=2;
    ch[8]--;
    ch[4]--;

    nu[9]++;
   }
fout<<"Case #"<<x++<<": ";
   for(int i=0;i<10;i++)
   {
   long long int n=nu[i];
   while(n--)
   fout<<i;
      //if(nu[i]>0)
      //{
      //int n=nu[i];
      //while(n--)
//      cout<<i;
            }

  fout<<endl; }

}





