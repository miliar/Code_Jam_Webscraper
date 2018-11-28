#include<iostream>


using namespace std;

int main()
{
    int tc;
    cin>>tc;
    
    
    for(int i=0;i<tc;i++)
    {
            
            int flag=0;
                    
            string str[4];
            
            for(int j=0;j<4;j++)cin>>str[j];
            
            for(int j=0;j<4;j++)
            {
                    
                    if(str[j].find(".")!=-1)
                    {
                            flag=4;
                    }
                    
                    if(str[j].find(".")==-1 && str[j].find("O")==-1){flag=1;break;}
                                       
                    if(str[j].find(".")==-1 && str[j].find("X")==-1){flag=2;break;}
                           
                    
            }
            
            for(int j=0;j<4;j++)
            {
                    if(flag==1 || flag==2)break;
                    
                    string temp="";
                    for(int k=0;k<4;k++)
                    {
                            temp+=str[k][j];
                    }
                    
                    if(temp.find(".")==-1 && temp.find("O")==-1){flag=1;break;}
                                       
                    if(temp.find(".")==-1 && temp.find("X")==-1){flag=2;break;}
            }
            
            string temps="",tempd="";
            
            for(int j=0;j<4;j++)
            {
                    if(flag==1 || flag==2)break;
                    
                    
                    temps+=str[j][j];
                    tempd+=str[j][3-j];
            }
            if(flag!=1 && flag!=2)
            {
            if(temps.find(".")==-1 && temps.find("O")==-1){flag=1;}
                                       
            if(temps.find(".")==-1 && temps.find("X")==-1){flag=2;}
            
            if(tempd.find(".")==-1 && tempd.find("O")==-1){flag=1;}
                                       
            if(tempd.find(".")==-1 && tempd.find("X")==-1){flag=2;}
            }                
                     
            if(flag==1)cout<<"Case #"<<i+1<<": X won"<<endl;
            
            else if(flag==2)cout<<"Case #"<<i+1<<": O won"<<endl;
            
            else if(flag==4)cout<<"Case #"<<i+1<<": Game has not completed"<<endl;
            
            else cout<<"Case #"<<i+1<<": Draw"<<endl;
                              
    }
    
    
    return 0;
}
