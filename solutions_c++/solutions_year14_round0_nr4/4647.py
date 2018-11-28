#include<iostream>
#include<fstream>
using namespace std;

int T;
int main()
{
  freopen("D-large.in","r",stdin);
  freopen("output.txt","w",stdout);
  cin>>T;
for(int k=0;k<T;k++)
{
 int N;
 cin>>N;long double naomi[N],naomi2[N],ken[N],ken2[N];int realwin=N,cheatwin=0;
 for(int i=0;i<N;i++)
  cin>>naomi[i];
 for(int i=0;i<N;i++)
  cin>>ken[i]; 
 
//sorting
 for(int i=0;i<(N-1);i++)
  for(int j=0;j<(N-1-i);j++)
   {
     if(naomi[j]>naomi[j+1])
     {
       long double temp=naomi[j];
       naomi[j]=naomi[j+1];
       naomi[j+1]=temp;                       
     }       
   }
//sorting
 for(int i=0;i<(N-1);i++)
  for(int j=0;j<(N-1-i);j++)
   {
     if(ken[j]>ken[j+1])
     {
       long double temp=ken[j];
       ken[j]=ken[j+1];
       ken[j+1]=temp;                       
     }       
   }

//Duplicate
for(int i=0;i<N;i++)
{
  naomi2[i]=naomi[i];
  ken2[i]=ken[i];       
}

//Deceithful War 
for(int i=(N-1);i>=0;i--)
{
 if(naomi[i]>ken[i]) cheatwin++;
 else
 {
  if(i==0) break;                  
  long double temp=naomi[0];int p=-1;
  do
  { 
   p++;
   naomi[p]=naomi[p+1];      
  }
  while(p!=(i-1));
  naomi[i]=temp;                   
 }        
}

//War
for(int i=0,j=0;i<N;i++,j++)
{
int k=0;
 if(ken2[j]<naomi2[i])
 {
  while((j+k+1)!=N) if(ken2[j+(++k)]>naomi2[i]) { realwin--;break;}                       
  long double temp=ken2[j];
  ken2[j]=ken2[j+k];
  ken2[j+k]=temp;
 }
 else realwin--;        
}
  cout<<"Case #"<<k+1<<": "<<cheatwin<<" "<<realwin<<endl;     
}
  return 0;    
}
