#include<iostream>
using namespace std;

int vcheck(char a)
{
  if(a=='a'||a=='e'||a=='i'||a=='o'||a=='u')
  return 1;
  else
  return 0;
}
int main()
{
    int a;
    cin>>a;
    
    int t=1;
    while(t<=a)
    {
    char l[110];
    cin>>l;
    int p;
    int n;
    int count;
    int flag;
    p=strlen(l);
    int pr;
    cin>>n;
    count=0;
    pr=0;
    for(int i=0;i<p,i+n<=p;)
    {
    
   // cout<<endl<<l[i];
   // cout<<"\nv:"<<vcheck(l[i]);
    if(!vcheck(l[i]))
    {
      flag=0;
      for(int j=1;j<n;j++)
      {  // cout<<"\nv:"<<vcheck(l[i+j]);
          if(!vcheck(l[i+j]))
         {continue;
         //cout<<"here";
         }else
         {//cout<<"flag1";
         flag=1;
          i=i+j;
          break;
         }
      }  
      if(flag==0)
      {//cout<<"\ncountp"<<count<<endl;
      //cout<<"i"<<i<<"pr"<<pr<<"p"<<p<<endl;
       count=count+(i-pr+1)*(p-(i+n-1));
       
       i++; 
       pr=i;  
       //cout<<"\ncountn"<<count<<endl;      
       }
    }
    else
    i++;
    }
    
    cout<<"Case #"<<t<<": "<<count<<endl;
    t++;
    }
    

    return 0;
}
