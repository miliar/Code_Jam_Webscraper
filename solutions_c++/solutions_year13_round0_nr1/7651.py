#include<iostream>
#include<string>
using namespace std;
int main()
{
         freopen("input2.txt","r",stdin);
         freopen("output1.txt","w",stdout);
        int t;
        cin>>t;
        for(int l=1;l<=t;l++)
        {char ch1[4],ch2[4],ch3[4],ch4[4];
         cin>>ch1>>ch2>>ch3>>ch4;
         int c=0,a=0;
         int d=0,i=0;
        
        if(ch1[0]=='X'&&ch1[1]=='X'&&ch1[2]=='X'&&ch1[3]=='X') {c=1; goto stop;}
         if(ch1[0]=='X'&&ch1[1]=='X'&&ch1[2]=='X'&&ch1[3]=='T') {c=1; goto stop;}
         if(ch1[0]=='X'&&ch1[1]=='X'&&ch1[2]=='T'&&ch1[3]=='X') {c=1; goto stop;}
         if(ch1[0]=='X'&&ch1[1]=='T'&&ch1[2]=='X'&&ch1[3]=='X') {c=1; goto stop;}
         if(ch1[0]=='T'&&ch1[1]=='X'&&ch1[2]=='X'&&ch1[3]=='X') {c=1; goto stop;}
         if(ch2[0]=='X'&&ch2[1]=='X'&&ch2[2]=='X'&&ch2[3]=='X') {c=1; goto stop;}
         if(ch2[0]=='X'&&ch2[1]=='X'&&ch2[2]=='X'&&ch2[3]=='T') {c=1; goto stop;}
         if(ch2[0]=='X'&&ch2[1]=='X'&&ch2[2]=='T'&&ch2[3]=='X') {c=1; goto stop;}
         if(ch2[0]=='X'&&ch2[1]=='T'&&ch2[2]=='X'&&ch2[3]=='X') {c=1; goto stop;}
         if(ch2[0]=='T'&&ch2[1]=='X'&&ch2[2]=='X'&&ch2[3]=='X') {c=1; goto stop;}
         if(ch3[0]=='X'&&ch3[1]=='X'&&ch3[2]=='X'&&ch3[3]=='X') {c=1; goto stop;}
         if(ch3[0]=='X'&&ch3[1]=='X'&&ch3[2]=='X'&&ch3[3]=='T') {c=1; goto stop;}
         if(ch3[0]=='X'&&ch3[1]=='X'&&ch3[2]=='T'&&ch3[3]=='X') {c=1; goto stop;}
         if(ch3[0]=='X'&&ch3[1]=='T'&&ch3[2]=='X'&&ch3[3]=='X') {c=1; goto stop;}
         if(ch3[0]=='T'&&ch3[1]=='X'&&ch3[2]=='X'&&ch3[3]=='X') {c=1; goto stop;}
         if(ch4[0]=='X'&&ch4[1]=='X'&&ch4[2]=='X'&&ch4[3]=='X') {c=1; goto stop;}
         if(ch4[0]=='X'&&ch4[1]=='X'&&ch4[2]=='X'&&ch4[3]=='T') {c=1; goto stop;}
         if(ch4[0]=='X'&&ch4[1]=='X'&&ch4[2]=='T'&&ch4[3]=='X') {c=1; goto stop;}
         if(ch4[0]=='X'&&ch4[1]=='T'&&ch4[2]=='X'&&ch4[3]=='X') {c=1; goto stop;}
         if(ch4[0]=='T'&&ch4[1]=='X'&&ch4[2]=='X'&&ch4[3]=='X') {c=1; goto stop;}
         if(ch1[0]=='X'&&ch2[0]=='X'&&ch3[0]=='X'&&ch4[0]=='X') {c=1; goto stop;}
         if(ch1[0]=='X'&&ch2[0]=='X'&&ch3[0]=='X'&&ch4[0]=='T') {c=1; goto stop;} 
         if(ch1[0]=='X'&&ch2[0]=='X'&&ch3[0]=='T'&&ch4[0]=='X') {c=1; goto stop;}
         if(ch1[0]=='X'&&ch2[0]=='T'&&ch3[0]=='X'&&ch4[0]=='X') {c=1; goto stop;}
         if(ch1[0]=='T'&&ch2[0]=='X'&&ch3[0]=='X'&&ch4[0]=='X') {c=1; goto stop;}
         if(ch1[1]=='X'&&ch2[1]=='X'&&ch3[1]=='X'&&ch4[1]=='X') {c=1; goto stop;}
         if(ch1[1]=='X'&&ch2[1]=='X'&&ch3[1]=='X'&&ch4[1]=='T') {c=1; goto stop;}
         if(ch1[1]=='X'&&ch2[1]=='X'&&ch3[1]=='T'&&ch4[1]=='X') {c=1; goto stop;}
         if(ch1[1]=='X'&&ch2[1]=='T'&&ch3[1]=='X'&&ch4[1]=='X') {c=1; goto stop;}
         if(ch1[1]=='T'&&ch2[1]=='X'&&ch3[1]=='X'&&ch4[1]=='X') {c=1; goto stop;}
         if(ch1[2]=='X'&&ch2[2]=='X'&&ch3[2]=='X'&&ch4[2]=='X') {c=1; goto stop;} 
         if(ch1[2]=='X'&&ch2[2]=='X'&&ch3[2]=='X'&&ch4[2]=='T') {c=1; goto stop;} 
         if(ch1[2]=='X'&&ch2[2]=='X'&&ch3[2]=='T'&&ch4[2]=='X') {c=1; goto stop;}
         if(ch1[2]=='X'&&ch2[2]=='T'&&ch3[2]=='X'&&ch4[2]=='X') {c=1; goto stop;}
         if(ch1[2]=='T'&&ch2[2]=='X'&&ch3[2]=='X'&&ch4[2]=='X') {c=1; goto stop;}
         if(ch1[3]=='X'&&ch2[3]=='X'&&ch3[3]=='X'&&ch4[3]=='X') {c=1; goto stop;}
         if(ch1[3]=='X'&&ch2[3]=='X'&&ch3[3]=='X'&&ch4[3]=='T') {c=1; goto stop;}
         if(ch1[3]=='X'&&ch2[3]=='X'&&ch3[3]=='T'&&ch4[3]=='X') {c=1; goto stop;}       
         if(ch1[3]=='X'&&ch2[3]=='T'&&ch3[3]=='X'&&ch4[3]=='X') {c=1; goto stop;}
         if(ch1[3]=='T'&&ch2[3]=='X'&&ch3[3]=='X'&&ch4[3]=='X') {c=1; goto stop;}
         if(ch1[0]=='X'&&ch2[1]=='X'&&ch3[2]=='X'&&ch4[3]=='X') {c=1; goto stop;}       
         if(ch1[0]=='X'&&ch2[1]=='X'&&ch3[2]=='X'&&ch4[3]=='T') {c=1; goto stop;}       
         if(ch1[0]=='X'&&ch2[1]=='X'&&ch3[2]=='T'&&ch4[3]=='X') {c=1; goto stop;}       
         if(ch1[0]=='X'&&ch2[1]=='T'&&ch3[2]=='X'&&ch4[3]=='X') {c=1; goto stop;}       
         if(ch1[0]=='T'&&ch2[1]=='X'&&ch3[2]=='X'&&ch4[3]=='X') {c=1; goto stop;}       
         if(ch1[3]=='X'&&ch2[2]=='X'&&ch3[1]=='X'&&ch4[0]=='X') {c=1; goto stop;}       
         if(ch1[3]=='X'&&ch2[2]=='X'&&ch3[1]=='X'&&ch4[0]=='T') {c=1; goto stop;}       
         if(ch1[3]=='X'&&ch2[2]=='X'&&ch3[1]=='T'&&ch4[0]=='X') {c=1; goto stop;}       
         if(ch1[3]=='X'&&ch2[2]=='T'&&ch3[1]=='X'&&ch4[0]=='X') {c=1; goto stop;}       
         if(ch1[3]=='T'&&ch2[2]=='X'&&ch3[1]=='X'&&ch4[0]=='X') {c=1; goto stop;}       
        
         if(ch1[0]=='O'&&ch1[1]=='O'&&ch1[2]=='O'&&ch1[3]=='O')  {a=1; goto stop;}
         if(ch1[0]=='O'&&ch1[1]=='O'&&ch1[2]=='O'&&ch1[3]=='T') {a=1; goto stop;}
         if(ch1[0]=='O'&&ch1[1]=='O'&&ch1[2]=='T'&&ch1[3]=='O') {a=1; goto stop;}
         if(ch1[0]=='O'&&ch1[1]=='T'&&ch1[2]=='O'&&ch1[3]=='O') {a=1; goto stop;}
         if(ch1[0]=='T'&&ch1[1]=='O'&&ch1[2]=='O'&&ch1[3]=='O') {a=1; goto stop;}
         if(ch2[0]=='O'&&ch2[1]=='O'&&ch2[2]=='O'&&ch2[3]=='O') {a=1; goto stop;}
         if(ch2[0]=='O'&&ch2[1]=='O'&&ch2[2]=='O'&&ch2[3]=='T') {a=1; goto stop;}
         if(ch2[0]=='O'&&ch2[1]=='O'&&ch2[2]=='T'&&ch2[3]=='O') {a=1; goto stop;}
         if(ch2[0]=='O'&&ch2[1]=='T'&&ch2[2]=='O'&&ch2[3]=='O') {a=1; goto stop;}
         if(ch2[0]=='T'&&ch2[1]=='O'&&ch2[2]=='O'&&ch2[3]=='O') {a=1; goto stop;}
         if(ch3[0]=='O'&&ch3[1]=='O'&&ch3[2]=='O'&&ch3[3]=='O') {a=1; goto stop;}
         if(ch3[0]=='O'&&ch3[1]=='O'&&ch3[2]=='O'&&ch3[3]=='T') {a=1; goto stop;}
         if(ch3[0]=='O'&&ch3[1]=='O'&&ch3[2]=='T'&&ch3[3]=='O') {a=1; goto stop;}
         if(ch3[0]=='O'&&ch3[1]=='T'&&ch3[2]=='O'&&ch3[3]=='O') {a=1; goto stop;}
         if(ch3[0]=='t'&&ch3[1]=='O'&&ch3[2]=='O'&&ch3[3]=='O') {a=1; goto stop;}
         if(ch4[0]=='O'&&ch4[1]=='O'&&ch4[2]=='O'&&ch4[3]=='O') {a=1; goto stop;}
         if(ch4[0]=='O'&&ch4[1]=='O'&&ch4[2]=='O'&&ch4[3]=='T') {a=1; goto stop;}
         if(ch4[0]=='O'&&ch4[1]=='O'&&ch4[2]=='T'&&ch4[3]=='O') {a=1; goto stop;}
         if(ch4[0]=='O'&&ch4[1]=='T'&&ch4[2]=='O'&&ch4[3]=='O') {a=1; goto stop;}
         if(ch4[0]=='T'&&ch4[1]=='O'&&ch4[2]=='O'&&ch4[3]=='O') {a=1; goto stop;}
         if(ch1[0]=='O'&&ch2[0]=='O'&&ch3[0]=='O'&&ch4[0]=='O') {a=1; goto stop;}
         if(ch1[0]=='O'&&ch2[0]=='O'&&ch3[0]=='O'&&ch4[0]=='T') {a=1; goto stop;} 
         if(ch1[0]=='O'&&ch2[0]=='O'&&ch3[0]=='T'&&ch4[0]=='O') {a=1; goto stop;}
         if(ch1[0]=='O'&&ch2[0]=='T'&&ch3[0]=='O'&&ch4[0]=='O') {a=1; goto stop;}
         if(ch1[0]=='T'&&ch2[0]=='O'&&ch3[0]=='O'&&ch4[0]=='O') {a=1; goto stop;}
         if(ch1[1]=='O'&&ch2[1]=='O'&&ch3[1]=='O'&&ch4[1]=='O') {a=1; goto stop;}
         if(ch1[1]=='O'&&ch2[1]=='O'&&ch3[1]=='O'&&ch4[1]=='T') {a=1; goto stop;}
         if(ch1[1]=='O'&&ch2[1]=='O'&&ch3[1]=='T'&&ch4[1]=='O') {a=1; goto stop;}
         if(ch1[1]=='O'&&ch2[1]=='T'&&ch3[1]=='O'&&ch4[1]=='O') {a=1; goto stop;}
         if(ch1[1]=='T'&&ch2[1]=='O'&&ch3[1]=='O'&&ch4[1]=='O') {a=1; goto stop;}
         if(ch1[2]=='O'&&ch2[2]=='O'&&ch3[2]=='O'&&ch4[2]=='O') {a=1; goto stop;} 
         if(ch1[2]=='O'&&ch2[2]=='O'&&ch3[2]=='O'&&ch4[2]=='T') {a=1; goto stop;} 
         if(ch1[2]=='O'&&ch2[2]=='O'&&ch3[2]=='T'&&ch4[2]=='O') {a=1; goto stop;}
         if(ch1[2]=='O'&&ch2[2]=='T'&&ch3[2]=='O'&&ch4[2]=='O') {a=1; goto stop;}
         if(ch1[2]=='T'&&ch2[2]=='O'&&ch3[2]=='O'&&ch4[2]=='O') {a=1; goto stop;}
         if(ch1[3]=='O'&&ch2[3]=='O'&&ch3[3]=='O'&&ch4[3]=='O') {a=1; goto stop;}
         if(ch1[3]=='O'&&ch2[3]=='O'&&ch3[3]=='O'&&ch4[3]=='T') {a=1; goto stop;}
         if(ch1[3]=='O'&&ch2[3]=='O'&&ch3[3]=='T'&&ch4[3]=='O') {a=1; goto stop;}       
         if(ch1[3]=='O'&&ch2[3]=='T'&&ch3[3]=='O'&&ch4[3]=='O') {a=1; goto stop;}
         if(ch1[3]=='T'&&ch2[3]=='O'&&ch3[3]=='O'&&ch4[3]=='O') {a=1; goto stop;}
         if(ch1[0]=='O'&&ch2[1]=='O'&&ch3[2]=='O'&&ch4[3]=='O') {a=1; goto stop;}       
         if(ch1[0]=='O'&&ch2[1]=='O'&&ch3[2]=='O'&&ch4[3]=='T') {a=1; goto stop;}       
         if(ch1[0]=='O'&&ch2[1]=='O'&&ch3[2]=='T'&&ch4[3]=='O') {a=1; goto stop;}       
         if(ch1[0]=='O'&&ch2[1]=='T'&&ch3[2]=='O'&&ch4[3]=='O') {a=1; goto stop;}       
         if(ch1[0]=='T'&&ch2[1]=='O'&&ch3[2]=='O'&&ch4[3]=='O') {a=1; goto stop;}       
         if(ch1[3]=='O'&&ch2[2]=='O'&&ch3[1]=='O'&&ch4[0]=='O') {a=1; goto stop;}       
         if(ch1[3]=='O'&&ch2[2]=='O'&&ch3[1]=='O'&&ch4[0]=='T') {a=1; goto stop;}       
         if(ch1[3]=='O'&&ch2[2]=='O'&&ch3[1]=='T'&&ch4[0]=='O') {a=1; goto stop;}       
         if(ch1[3]=='O'&&ch2[2]=='T'&&ch3[1]=='O'&&ch4[0]=='O') {a=1; goto stop;}       
         if(ch1[3]=='T'&&ch2[2]=='O'&&ch3[1]=='O'&&ch4[0]=='O') {a=1; goto stop;}       
        for(int j=0;j<4;j++)
        {
                if(ch1[j]=='.'||ch2[j]=='.'||ch3[j]=='.'||ch4[j]=='.') {i=1; break;}
                }
                if(i==0) d=1;       
        stop: if(c==1) cout<<"Case #"<<l<<": "<<"X won"<<endl;
              else if(a==1) cout<<"Case #"<<l<<": "<<"O won"<<endl;
               else if(d==1) cout<<"Case #"<<l<<": "<<"Draw"<<endl;
               else if(i==1) cout<<"Case #"<<l<<": "<<"Game has not completed"<<endl;
        }
         return 0;
         }
