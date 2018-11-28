#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
int t;
string a[4];
int colx[4],rowx[4],coly[4],rowy[4],colT[4],rowT[4];
int diag1x,diag1y,diag1T,diag2x,diag2y,diag2T,bcnt;
string res="";

void compute()
{    bool xflag=false;
     bool yflag=false;

    for(int i=0;i<4;i++)
    {  if(!xflag&&( (rowx[i]==4)||(rowx[i]==3&&rowT[i]==1)||(colx[i]==4)||(colx[i]==3&&colT[i]==1)))
          xflag=true;
   
       if(!yflag&&( (rowy[i]==4)||(rowy[i]==3&&rowT[i]==1)||(coly[i]==4)||(coly[i]==3&&colT[i]==1)))
         yflag=true;   
               
    }
    
    if(diag1x==4||diag2x==4||(diag1x==3&&diag1T==1)||(diag2x==3&&diag2T==1))
       xflag=true;
    if(diag1y==4||diag2y==4||(diag1y==3&&diag1T==1)||(diag2y==3&&diag2T==1))
       yflag=true;
       
    if(!xflag&&!yflag&&bcnt)
      res+="Game has not completed";    
    else if(xflag)                   
       res+="X won";
    else if(yflag)
       res+="O won";        
    else if(!bcnt)
      res+="Draw";   
}     
int main()
{  scanf("%d",&t);
   int m=1;
   while(t--)
   {   res="";
       memset(rowx,0,sizeof(rowx));
       memset(colx,0,sizeof(colx));
       memset(rowy,0,sizeof(rowy));
       memset(coly,0,sizeof(coly));
       memset(rowT,0,sizeof(rowT));
       memset(colT,0,sizeof(colT));
       bcnt=0;
       diag1x=diag2x=diag1y=diag2y=diag1T=diag2T=0;
        for(int i=0;i<4;i++)
         {   cin>>a[i];
             for(int j=0;j<4;j++)
             {  switch(a[i][j])
               {  case 'X' : rowx[i]++;
                             colx[j]++;
                             break;
                  case 'O' : rowy[i]++;
                             coly[j]++;break;
                  case 'T' : rowT[i]++;colT[j]++;break;
                  case '.' : bcnt++;
               }
             }
            switch(a[i][i])
            {    case 'X':diag1x++;break;
                 case 'O':diag1y++;break;
                 case 'T':diag1T++;break;
            }  
            switch(a[i][3-i])
            {    case 'X':diag2x++;break;
                 case 'O':diag2y++;break;
                 case 'T':diag2T++;break;
            }   
         }     
         compute();
        cout<<"Case #"<<m++<<": "<<res<<"\n";
        
    }
    //system("pause");
    
}                 
