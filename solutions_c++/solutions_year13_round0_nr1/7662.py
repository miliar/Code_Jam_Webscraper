#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<string>
#include<cstring>
using namespace std;
int main()
{

    int t;
    cin>>t;
    char ch;
    int arr[4][4];
    int counter=1;
    while(t--)
    {  int result=-5;int incomplete=0;
        for(int i=0;i<4;i++){
            for(int j=0;j<4;j++){
                cin>>ch;
                if(ch=='X')
                    arr[i][j]=1;
                else if(ch=='O')
                    arr[i][j]=0;
                else if(ch=='T')
                    arr[i][j]=2;
                else if(ch=='.')
                    arr[i][j]=-1;
            }
        }
       /* for(int i=0;i<4;i++){
            for(int j=0;j<4;j++)
            cout<<arr[i][j];cout<<endl;}*/

        for(int i=0;i<4;i++)
        {
            if((arr[i][0]==1||arr[i][0]==2)&&(arr[i][1]==1||arr[i][1]==2)&&(arr[i][2]==1||arr[i][2]==2)&&(arr[i][3]==1||arr[i][3]==2))
            result=1;
            if((arr[i][0]==0||arr[i][0]==2)&&(arr[i][1]==0||arr[i][1]==2)&&(arr[i][2]==0||arr[i][2]==2)&&(arr[i][3]==0||arr[i][3]==2))
            result=0;

        }
        for(int j=0;j<4;j++)
        {
            if((arr[0][j]==1||arr[0][j]==2)&&(arr[1][j]==1||arr[1][j]==2)&&(arr[2][j]==1||arr[2][j]==2)&&(arr[3][j]==1||arr[3][j]==2))
            result=1;

            if((arr[0][j]==0||arr[0][j]==2)&&(arr[1][j]==0||arr[1][j]==2)&&(arr[2][j]==0||arr[2][j]==2)&&(arr[3][j]==0||arr[3][j]==2))
            result=0;

        }
        if((arr[0][0]==1||arr[0][0]==2)&&(arr[1][1]==1||arr[1][1]==2)&&(arr[2][2]==1||arr[2][2]==2)&&(arr[3][3]==1||arr[3][3]==2))
            result=1;
        if((arr[0][0]==0||arr[0][0]==2)&&(arr[1][1]==0||arr[1][1]==2)&&(arr[2][2]==0||arr[2][2]==2)&&(arr[3][3]==0||arr[3][3]==2))
            result=0;
        if((arr[0][3]==1||arr[0][3]==2)&&(arr[1][2]==1||arr[1][2]==2)&&(arr[2][1]==1||arr[2][1]==2)&&(arr[3][0]==1||arr[3][0]==2))
            result=1;
        if((arr[0][3]==0||arr[0][3]==2)&&(arr[1][2]==0||arr[1][2]==2)&&(arr[2][1]==0||arr[2][1]==2)&&(arr[3][0]==0||arr[3][0]==2))
            result=0;
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++){
            if(arr[i][j]==-1)
            {
                incomplete=1;
                break;
            }
            }
            if(incomplete)
            break;
        }
        if(result==1)
        cout<<"Case #"<<counter<<": "<<"X won"<<endl;
        else if(result==0)
        cout<<"Case #"<<counter<<": "<<"O won"<<endl;
        else if(result==-5&&incomplete==0)
        cout<<"Case #"<<counter<<": "<<"Draw"<<endl;
        else
        cout<<"Case #"<<counter<<": "<<"Game has not completed"<<endl;
        counter++;
    }
return 0;
}
