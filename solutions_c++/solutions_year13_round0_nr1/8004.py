#include<fstream>
using namespace std;
int main()
{
    ifstream in;
    ofstream out;
    in.open("cj1.in");
    out.open("ans.out");
    int t,caseno;
    in>>t;
    caseno=t;
    while(t--)
    {
       int i,j,k,l,count=0,flag=1;
       char wins,tictac[4][4];
       
       for(i=0;i<4;i++)
        for(j=0;j<4;j++)
        {
           in>>tictac[i][j];
           if(tictac[i][j]!='.')
            count++;
        }
         
       for(i=0;i<4 && flag;i++)
        for(j=0;j<4;j++)
        {           
           /*check horizontally*/
           for(k=0;k<4;k++)
            if(tictac[i][j]!=tictac[i][k] && tictac[i][k]!='T')
             break;
           if(k==4 && tictac[i][j]!='.')
           {
             wins=tictac[i][j];
             flag=0;
             break;
           }
           /*check vertically*/
           for(k=0;k<4;k++)
            if(tictac[i][j]!=tictac[k][j] && tictac[k][j]!='T')
             break;
           if(k==4 && tictac[i][j]!='.')
           {
             wins=tictac[i][j];
             flag=0;
             break;
           }
           /*check diagonally*/
           if(i==0 && j==0)
           {
              k=1; l=1;
              while(k<4)
               if(tictac[k++][l++]!=tictac[0][0] && tictac[k-1][l-1]!='T')
                break;
              if(k==4 && tictac[0][0]!='.')
              {
                 wins=tictac[0][0];
                 flag=0;
                 break;
              }
           }
           if(i==0 && j==3)
           {
              k=1; l=2;
              while(l>=0)
               if(tictac[k++][l--]!=tictac[0][3] && tictac[k-1][l+1]!='T')
                break;
              if(l<0 && tictac[0][3]!='.')
              {
                 wins=tictac[0][3];
                 flag=0;
                 break;
              }
           }
           if(i==3 && j==0)
           {
              k=2; l=1;
              while(k>=0)
               if(tictac[k--][l++]!=tictac[0][3] && tictac[k+1][l-1]!='T')
                break;
              if(k<0 && tictac[3][0]!='.')
              {
                 wins=tictac[3][0];
                 flag=0;
                 break;
              }
           }
           if(i==3 && j==3)
           {
              k=2; l=2;
              while(k>=0)
               if(tictac[k--][l--]!=tictac[3][3] && tictac[k+1][l+1]!='T')
                break;
              if(k<0 && tictac[3][3]!='.')
              {
                 wins=tictac[3][3];
                 flag=0;
                 break;
              }
           }
        }
        if(t>0)
        {
        if(!flag)
          out<<"Case #"<<caseno-t<<": "<<wins<<" won"<<endl;
         else if(flag && count==16)
          out<<"Case #"<<caseno-t<<": Draw"<<endl;
         else
          out<<"Case #"<<caseno-t<<": Game has not completed"<<endl;
        }
        else
        {
        if(!flag)
          out<<"Case #"<<caseno-t<<": "<<wins<<" won";
         else if(flag && count==16)
          out<<"Case #"<<caseno-t<<": Draw";
         else
          out<<"Case #"<<caseno-t<<": Game has not completed";
        }
        
          
        //cout<<"flag: "<<flag<<" wins: "<<wins<<" count: "<<count<<endl<<endl;
    
    }
return 0;
}

              
