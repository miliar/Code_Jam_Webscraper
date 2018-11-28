#include <iostream>
using namespace std;
int main()
{
    int t;
    cin>>t;
    char a[16];
    int b[16];
    bool xflag=false,yflag=false,drawflag=false,iflag=false;
    for(int j=0;j<t;j++)
    {
        for (int i=0;i<16;i++)
        {
            cin>>a[i];
            b[i]=int(a[i]);
        }
         //enough to check from first row only
         //0 1 2 3
         //4 5 6 7
         //8 9 10 11
         //12 13 14 15
         //b[0]+b[1]+b[2]+b[3]==4*88|| b[4]+b[5]+b[6]+b[7]==4*88 || 
            
        //checking rowwise
        for(int k=0;k<16;k++)
        {
            if(b[k]==46)
                iflag=true;//which means there is an incomplete line somewhere
        }
        for(int k=0;k<13;k=k+4)
        {
            int temp=b[0+k]+b[1+k]+b[2+k]+b[3+k];
            if(temp==4*88 || temp==(3*88)+84)
            {
               xflag=true; 
               yflag=false;
               drawflag=false;
               iflag=false;
            }
            if(temp==4*79 || temp==(3*79)+84)
             {
               xflag=false; 
               yflag=true;
               drawflag=false;
               iflag=false;
            }
                
        }
        //checking columnwise
        for(int k=0;k<4;k++)
        {
            int temp=b[0+k]+b[4+k]+b[8+k]+b[12+k];
            if(temp==4*88 || temp==(3*88)+84)
            {
               xflag=true; 
               yflag=false;
               drawflag=false;
               iflag=false;
            }
            if(temp==4*79 || temp==(3*79)+84)
             {
               xflag=false; 
               yflag=true;
               drawflag=false;
               iflag=false;
            }
        }
        int temp1=b[0]+b[5]+b[10]+b[15];
        int temp2=b[3]+b[6]+b[9]+b[12];
        if(temp1==4*88|| temp2==4*88 || temp1==(3*88)+84 || temp2==(3*88)+84)
        {
               xflag=true; 
               yflag=false;
               drawflag=false;
               iflag=false;

        }
        if(temp1==4*79|| temp2==4*79 || temp1==(3*79)+84 || temp2==(3*79)+84)
        {
               xflag=false; 
               yflag=true;
               drawflag=false;
               iflag=false;

        }
        if(!xflag && !yflag && !iflag) //all rows full but neither x nor y has won
            drawflag=true;

        if(xflag)
            cout<<"Case #"<<j+1<<": "<<"X won"<<"\n";
        if(yflag)
            cout<<"Case #"<<j+1<<": "<<"O won"<<"\n";
        if(drawflag)
            cout<<"Case #"<<j+1<<": "<<"Draw"<<"\n";
        if(iflag)
            cout<<"Case #"<<j+1<<": "<<"Game has not completed"<<"\n";
         xflag=false;
         yflag=false;
         drawflag=false;
         iflag=false;

        }
               return 0;
}
    
    


    


        
            //checking if horizontal matches)
            //
        
    
        
