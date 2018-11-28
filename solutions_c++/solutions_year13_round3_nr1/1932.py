#include<iostream>
#include<cstring>
#include<cstdio>
using namespace std;
int main()
{
  int t;
  cin>>t;
  int q=1;
  while(q<=t)
  {
   char ch[3000];
   int n,total=0,st1=-1,last1=-1,st2=-1,last2=-1;
   scanf("%s%d",&ch,&n);
   int ount=0;
   int len=strlen(ch);
   for(int i=0;i<len;i++)
   { if(st1>=len || st2>=len || last1>=len|| last2>=len)
      break;
     if(ch[i]!='a'&& ch[i]!='e' && ch[i]!='i'&& ch[i]!='o' && ch[i]!='u')
     { if(ount==0)
        if(total==0)
        st1=i;
        else 
        st2=i;
        
       ount++;
       if(ount==n)
        { if(total==0)
          {
          last1=i;
          total=len-last1+(st1*(len-last1));
         // cout<<st1<<" "<<last1<<" "<<"total1 "<<total<<endl;
          st2=st1+1;
          last2=-1;
          // cout<<st1<<" "<<last1<<" "<<"total1 "<<total<<endl<<;
          ount--;
          }
          else
          {
              last2=i;
              if(last1<st2)
              { total+= (len-last2+(st2-st1-1)*(len-last2));
               // cout<<"1 "<<total;
               }else
                total=total+(len-last2);
              //  cout<<st2<<" "<<last2<<" "<<"total "<<total<<endl;
              st1=st2;
              st2=st1+1;
              last1=last2;
              last2=-1;
              ount--;
          }
        }
       
     }
     else 
     { 
      ount=0;
     }
   }    
   cout<<"Case #"<<q<<": "<<total<<endl;     
   q++;
  }   
}
