#include<iostream>
using namespace std;
bool xwin=false, owin=false, draw=false, gnc=false;
int checkwin(int arr[4][4]){
    
    //ARRAY IN CHECKWIN
    /*
     for(int i=0;i<4;i++)
    {
            
            for(int j=0;j<4;j++)
            {
                    cout<<arr[i][j]<<" ";
                    }
                    cout<<"\n";
                    }
                    */
    int rsum[4]={0};
    int csum[4]={0};
    int diag[2]={0};
//diag
    for(int i=0;i<4;i++)
    {
            
            for(int j=0;j<4;j++)
            {
               rsum[i]+=arr[i][j];
               csum[j]+=arr[i][j];     
                    
                    }
            
            }
            
    for(int i=0;i<4;i++)
    {diag[0]+=arr[i][i];
    diag[1]+=arr[i][3-i];
    }
            
            
for(int i=0;i<4;i++)
if(rsum[i]==0 || csum[i] ==0 || diag[0]==0 || diag[1]==0)
return 0;
else if (rsum[i]==4 || csum[i] ==4 || diag[0]==4 || diag[1]==4)
return 1;

return 3;
    
    }
bool justcheckans(int tt[4][4]){
     
     int ans=checkwin(tt);
    
        if(ans==0)
        {
                owin=true;
                  //O wins
                  }
                  else if (ans==1)
                  {
                      xwin=true;
                       // X wins
                       
                       }
                       else
                       return false;
return true;
     
     
     }
bool checkcomplete(int arr[4][4]){
     
     for(int i=0;i<4;i++)
     for(int j=0;j<4;j++)
     if(arr[i][j]==-10)
     return false;
     
return true;
     }

void checkans(int tt[4][4]){
     
   
        int ans=checkwin(tt);
       
        if(ans==0)
        {
               owin=true;
                  //O wins
                  }
                  else if (ans==1)
                  {
                    xwin=true;
                       // X wins
                       
                       }
        else if(ans==3) //no one win
         {
               bool rez= checkcomplete(tt);
           
               if(rez)
               {
                   draw=true;
                      //draw
                      }
                      else
                      {
                         gnc=true;
                          
                          //game not complete
                          
                          }
                   
                   }
           
          
          
     
     }



int main(){
    int t1;
    int tot;
    cin>>t1;
    tot=t1;
    while(t1--) {
                xwin=false;
                 owin=false;
                  draw=false;
                   gnc=false;
    char tto[5][5];
    for(int i=0;i<4;i++)
    cin>>tto[i];
    
    //check if t
    bool t=false;
    int tx=-1,ty=-1;
    for(int i=0;i<4;i++)
    for(int j=0;j<4;j++)
    if(tto[i][j]=='T')
    {t=true;
    tx=i;
    ty=j;
    }
    
    int tt[4][4]={0};
     for(int i=0;i<4;i++)
    for(int j=0;j<4;j++)
    if(tto[i][j]=='X')
    tt[i][j]=1;
    else if(tto[i][j]=='O')
    tt[i][j]=0;
    else if(tto[i][j]=='.')
    tt[i][j]=-10;
    /*
      for(int i=0;i<4;i++)
    {
            
            for(int j=0;j<4;j++)
            {
                    cout<<tt[i][j]<<" ";
                    }
                    cout<<"\n";
                    }
                    */
    if(t){
          //cout<<"heret";
           //put t as X
           tt[tx][ty]=1;
          bool xt=justcheckans(tt);
       if(xt==false){
       tt[tx][ty]=0;
       checkans(tt);
       }
       }else
      // cout<<"here";
        checkans(tt);
          
          
    cout<<"Case #"<<tot-t1<<": ";
    if(xwin)
    cout<<"X won";
    else if(owin)
    cout<<"O won";
    else if(draw)
    cout<<"Draw";
    else
    cout<<"Game has not completed";
    cout<<"\n";       
   
    
    
    }
    //system("pause");
}
