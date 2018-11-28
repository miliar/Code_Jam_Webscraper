#include<iostream>
#include<cstring>
#include<algorithm>
using namespace std;
int main()
{
    int test,cases=1;
    cin>>test;
    while(test--){
    char a[5][5];
    int dots=0,ans=0;
    for(int i=0;i<4;i++)
    {
        for(int j=0;j<4;j++){
            cin>>a[i][j];
            if(a[i][j]=='.') dots++;
        }
    }
    
    
    string p;
   for(int i=0;i<4;i++)
   {
       if(ans==1) break;
       p.clear();
       for(int j=0;j<4;j++){
       p+=a[i][j];
       if(p=="XXXX" || p=="XXXT" || p=="XXTX" || p=="XTXX" || p=="TXXX")
       {
           ans=1;i++;
           cout<<"Case #"<<cases<<": "<<"X won"<<endl;
           break;
       }
       
       else if(p=="OOOO" || p=="OOOT" || p=="OOTO" || p=="OTOO" || p=="TOOO")
       {
           ans=1;
           cout<<"Case #"<<cases<<": "<<"O won"<<endl;
           break;
       }
       
   }
   }
   if(ans==0){
   
     for(int i=0;i<4;i++)
   {
       if(ans==1) break;
       p.clear();
       for(int j=0;j<4;j++){
       p+=a[j][i];
       if(p=="XXXX" || p=="XXXT" || p=="XXTX" || p=="XTXX" || p=="TXXX")
       {
           ans=1;
           cout<<"Case #"<<cases<<": "<<"X won"<<endl;
           break;
       }
        else if(p=="OOOO" || p=="OOOt" || p=="OOTO" || p=="OTOO" || p=="TOOO")
       {
           ans=1;
          cout<<"Case #"<<cases<<": "<<"O won"<<endl;
           break;
       }
       
   }
   }
   
   if(ans==0){
       p.clear();
       for(int i=0;i<4;i++)
       {
           
           p+=a[i][i];
           if(p=="XXXX" || p=="XXXT" || p=="XXTX" || p=="XTXX" || p=="TXXX")
       {
           ans=1;
           cout<<"Case #"<<cases<<": "<<"X won"<<endl;
           
       }
        else if(p=="OOOO" || p=="OOOt" || p=="OOTO" || p=="OTOO" || p=="TOOO")
       {
           ans=1;
           cout<<"Case #"<<cases<<": "<<"O won"<<endl;
           
       }
       }
       
       if(ans==0){
          p.clear();
          for(int i=0;i<4;i++) 
          p += a[i][4-i-1];
          //cout<<p<<endl;
           if(p=="XXXX" || p=="XXXT" || p=="XXTX" || p=="XTXX" || p=="TXXX")
       {
           ans=1;
          cout<<"Case #"<<cases<<": "<<"X won"<<endl;
           
       }
        else if(p=="OOOO" || p=="OOOT" || p=="OOTO" || p=="OTOO" || p=="TOOO")
       {
           ans=1;
          cout<<"Case #"<<cases<<": "<<"O won"<<endl;
           
       }
       }
   }
   }
   if(ans==0 && dots==0) cout<<"Case #"<<cases<<": "<<"Draw"<<endl;
   else if(ans==0 && dots!=0)
    cout<<"Case #"<<cases<<": "<<"Game has not completed"<<endl;
   
    
   /* for(int i=0;i<4;i++){
    for(int j=0;j<4;j++)
    cout<<a[i][j];
    cout<<endl;
    
    }*/
    cases++;
    
    }
}
