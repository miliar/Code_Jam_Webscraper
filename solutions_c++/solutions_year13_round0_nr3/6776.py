#include<iostream>
//#include<conio.h>
#include<math.h>
#include<stdio.h>
using namespace std;
int polin(int num1);
int main()
{
    int tcase,strt,endp,cnt,flag;
    FILE *ip,*op;
    ip=fopen("input.txt","r");
    op=fopen("output.txt","w");
    fscanf(ip,"%d/n",&tcase);
    cout<<tcase;
  // cin>>strt;
  //  cin>>endp;
  float te;
    for(int i=0;i<tcase;i++)
    {
          cnt=0;
          fscanf(ip,"%d %d/n",&strt,&endp);
          cout<<strt<<endl<<endp;
          
            for(int j=strt;j<=endp;j++)
            {  flag=0;
                   // cout<<"strt is="<<j<<endl;
                    flag+=polin(j);
                    te=(int)sqrt(j);
                    cout<<te<<endl;
                    if(te==sqrt(j))
                    flag+=polin(te);
                   // cout<<"flag="<<flag<<endl;
                    if(flag==2)
                    cnt++;
                   
                    }
                   // cout<<"no of fair"<<cnt;
                   fprintf(op,"Case #%d: %d\n",i+1,cnt);
    }
                    fclose(ip);
                    fclose(op);
                   // getch();
                    
}           
 int polin(int num1)
 {
     int num;
     num=num1;
     int temp=0;
     while(num!=0)
     {            
                  temp=(temp*10)+(num%10);
                  num=num/10;
                  }
                  //cout<<temp<<endl;
                  if(num1==temp) return 1;
                  else return 0;
}                        
