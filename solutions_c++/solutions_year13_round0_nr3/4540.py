#include<stdio.h>
#include<iostream>
#include<math.h>
//#include<vector>
#include<fstream>

float palin(float s);
using namespace std;

int main()
{
//vector<int> sri;
//int a[1000];
//FILE *f = fopen("c.txt","r");
//ofstream outfile("code1.txt");
//ofstream myFile;
//myFile.open("code2.txt");
//if(myFile.is_open())
//{
#ifndef ONLINE_JUDGE
  freopen("c.txt","r",stdin);
#endif


 int t,i=0;
cin>>t;
while(t--)
{int count=0;
   float a,b;
//int b;
   cin>>a;
   cin>>b;
      while(a<=b)
         {
          float q;
          q=palin(a);
              if(q==1)
                 {
                 float k=sqrt(a);
//cout<<k<<endl;
                  q=palin(k);
//cout<<q<<endl;
                 if(q==1)
                    {
                     count++;

                     }
                 }
          a++;
         }

     cout<<"Case #"<<i+1<<": "<<count<<endl;
  i++;
}
//outfile.close();

//fclose(f);

//else
//cout<<"Unable to Open"<<endl;

return 0;
}






float palin(float s)
{
 int temp=s;
int sum=0,n;
while(temp!=0)
{
 n=temp%10;
sum=(sum*10)+n;
temp/=10;
}
if(sum==s)
return 1;
else
return 0;
}


