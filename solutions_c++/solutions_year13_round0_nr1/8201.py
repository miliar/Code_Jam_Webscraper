#include<iostream>
using namespace std;
int main()
{
    int t,i,j,z,k,kp;
    char val='N';
    cin>>t;
    string str[4];
    for(kp=1;kp<=t;kp++)
    {
        val='U';
        for(i=0;i<4;i++)
        cin>>str[i];
    

     for(j=0;j<3;j++)
   
    {
        z=1;k=1;
         for(i=0;i<3;i++)
    {
    if(str[j][i]==str[j][i+1]||str[j][i]=='T'||str[j][i+1]=='T')z=z*1;else z=z*0;
    
    
    if(str[i][j]==str[i+1][j]||str[i][j]=='T'||str[i+1][j]=='T')k=k*1;else k=k*0;}
    if(z==1){val=str[j][i-1];if(val=='T')val=str[j][i-1];break;}
    if(k==1){val=str[i-1][j];if(val=='T')val=str[i-2][j];break;}
}



      if(val!='X'&&val!='O')
    {
        z=1;k=1;
        for(i=0;i<3;i++)
    if(str[i][i]==str[i+1][i+1]||str[i][i]=='T'||str[i+1][i+1]=='T')z=z*1;else z=z*0;
    
    if(z==1)val=str[0][0];
    if(val=='T')val=str[1][1];
    
     for(i=3;i>0;i--)
    if(str[i][3-i]==str[i-1][4-i]||str[i][3-i]=='T'||str[i-1][4-i]=='T')k=k*1;else k=k*0;
    
    if(k==1)val=str[3][0];
    if(val=='T')val=str[2][1];
    }   
        
  if(val=='X')cout<<"Case #"<<kp<<": X won"<<endl;
  if(val=='O')cout<<"Case #"<<kp<<": O won"<<endl;
   if(val!='X'&&val!='O')
   {k=1;
       for(i=0;i<4;i++)
       for(j=0;j<4;j++)if(str[i][j]=='.')k=k*0;else k=k*1;
       if(k==0)cout<<"Case #"<<kp<<": Game has not completed"<<endl;
       else
       cout<<"Case #"<<kp<<": Draw"<<endl;
   }    
}    
    
    //system("PAUSE");
    return 0;
}        
        
