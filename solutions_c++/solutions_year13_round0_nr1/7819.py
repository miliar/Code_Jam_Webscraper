#include<iostream>
using namespace std;

int main()
{
    int t;
    cin>>t;
    int cnt=0;
    while(cnt<t)
    {
              cnt++;
              char arr[4][4];
              for(int i=0;i<4;i++)
                      for(int j=0;j<4;j++)
                              cin>>arr[i][j];
                              
        
            int cnt1=0;
            int cnt2=0;
            int flag=0;
            int dot=0;
            if(flag==0)
            {
                       for (int i =0;i<4;i++)
            {
                if(((arr[i][0]=='X')||(arr[i][0]=='T'))&&((arr[i][1]=='X')||(arr[i][1]=='T'))&&((arr[i][2]=='X')||(arr[i][2]=='T'))&&((arr[i][3]=='X')||(arr[i][3]=='T')))
                {flag++;cout<<"Case #"<<cnt<<": X won"<<endl;}
                else if(((arr[i][0]=='O')||(arr[i][0]=='T'))&&((arr[i][1]=='O')||(arr[i][1]=='T'))&&((arr[i][2]=='O')||(arr[i][2]=='T'))&&((arr[i][3]=='O')||(arr[i][3]=='T')))
                {flag++;cout<<"Case #"<<cnt<<": O won"<<endl;}
                
            }
            }
            if(flag==0)
            {
            for (int i =0;i<4;i++)
            {
                if(((arr[0][i]=='X')||(arr[0][i]=='T'))&&((arr[1][i]=='X')||(arr[1][i]=='T'))&&((arr[2][i]=='X')||(arr[2][i]=='T'))&&((arr[3][i]=='X')||(arr[3][i]=='T')))
                {flag++;cout<<"Case #"<<cnt<<": X won"<<endl;}
               else if(((arr[0][i]=='O')||(arr[0][i]=='T'))&&((arr[1][i]=='O')||(arr[1][i]=='T'))&&((arr[2][i]=='O')||(arr[2][i]=='T'))&&((arr[3][i]=='O')||(arr[3][i]=='T')))
                {flag++;cout<<"Case #"<<cnt<<": O won"<<endl;} 
            }
            }
            if(flag==0)
            {
                       if(((arr[0][0]=='O')||(arr[0][0]=='T'))&&((arr[1][1]=='O')||(arr[1][1]=='T'))&&((arr[2][2]=='O')||(arr[2][2]=='T'))&&((arr[3][3]=='O')||(arr[3][3]=='T')))
            {flag++;cout<<"Case #"<<cnt<<": O won"<<endl;}
            }
            if(flag==0)
            {if(((arr[0][0]=='O')||(arr[0][0]=='T'))&&((arr[1][1]=='O')||(arr[1][1]=='T'))&&((arr[2][2]=='O')||(arr[2][2]=='T'))&&((arr[3][3]=='O')||(arr[3][3]=='T')))
            {flag++;cout<<"Case #"<<cnt<<": O won"<<endl;}
            }
            if(flag==0)
            {if(((arr[0][3]=='O')||(arr[0][3]=='T'))&&((arr[1][2]=='O')||(arr[1][2]=='T'))&&((arr[2][1]=='O')||(arr[2][1]=='T'))&&((arr[3][0]=='O')||(arr[3][0]=='T')))
            {flag++;cout<<"Case #"<<cnt<<": O won"<<endl;}
            }
            if(flag==0)
            {if(((arr[0][3]=='O')||(arr[0][3]=='T'))&&((arr[1][2]=='O')||(arr[1][2]=='T'))&&((arr[2][1]=='O')||(arr[2][1]=='T'))&&((arr[3][0]=='O')||(arr[3][0]=='T')))
            {flag++;cout<<"Case #"<<cnt<<": O won"<<endl;}
            }
            if((flag==0)&&(dot==0))
            cout<<"Case #"<<cnt<<": Draw"<<endl;
            if((flag==0)&&(dot!=0))
            cout<<"Case #"<<cnt<<": Game has not completed"<<endl;
            
    }

}
