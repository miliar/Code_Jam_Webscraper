#include<iostream>
#include<algorithm>
#include<cmath>
using namespace std;
int main()
{
int t;
//cin>>t;
//while(t--)
//{
cin>>t;
int x=0;
while(x<t){
  int arr[50],tmp[50],f[10],w=0;
  for(int i=0;i<50;i++)
  {
  arr[i]=-1;
  tmp[i]=-1;
  }
  for(int i=0;i<10;i++)
  f[i]=0;
  string n;
  int k,r=1;
  cin>>n;


 for(int i=49,j=n.length()-1;j>=0;i--,j--)
 {
 arr[i]=n[j]-48;
 tmp[i]=n[j]-48;
 }
if(n.length()==1 && arr[49]==0)
{
cout<<"Case #"<<x+1<<": INSOMNIA"<<endl;

}
else{

//for(int k=49;k>=0;k--)
//cout<<arr[k];
//cout<<endl;
int count=0;
for(int k=1;;k++)
{w=0;
 count=0;
for(int i=0;i<50;i++)
  arr[i]=tmp[i];
  int a=49;

     int c=0;
     while(arr[a]!=-1)
       {
          if(arr[a]*k+c >=10)
            {
              int temp=(arr[a]*k+c)/10;
              int temp1=(arr[a]*k+c)%10;
              c=temp;
              arr[a]=temp1;
              a--;
              if(a==2)
              break;
            }
         else
            {
              arr[a]=arr[a]*k+c;
              a--;
              c=0;
               if(a==2)
              break;
            }
        }

     if(c>0)
       arr[a]=c;
//}
int h=49;
      while(arr[h]==0)
      {
      count++;
      h--;

      }
     int l=49;
      while(arr[l]!=-1)
      {
      w=w*10+arr[l];
      l--;
      }


    int j=49;
    while(arr[j]!=-1)
      {
         // cout<<arr[j];
          f[arr[j]]=1;
          j--;

      }
  //cout<<endl;
     for(int i=0;i<10;i++)
     {
        if(f[i]==0)
        {
         r=0;
         break;
        }
       else
         {
         r=1;
     //    cout<<" ("<<i<<") ";
         }
      }
      if(r==1)
      break;


   }
   if(r==0)
   cout<<"INSOMNIA";
else{
int q=0;
while(w>0)
{
q=q*10+w%10;
w=w/10;
}
while(count--)
q=q*10;
cout<<"Case #"<<x+1<<": "<<q<<endl;

}}
x++;}
}


