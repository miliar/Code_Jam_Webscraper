#include <iostream>
using namespace std;

int main()
{
    int t=0,k;cin>>k;
    char p;
    while(k--)
    {	t++;
        int arr[4][4]={0};
        int ro[10]={0};
        int flag=0,s=0;
        //int co[4]={0};
        for(int i=0;i<4;i++)
        for(int j=0;j<4;j++)
        {
            cin>>p;
            if(p=='X')arr[i][j]=1;
            else if(p=='O')arr[i][j]=10;
            else if(p=='T')arr[i][j]=5;
            else arr[i][j]=0;
            s+=arr[i][j];
        }
        for(int i=0;i<4;i++)
        for(int j=0;j<4;j++)
        ro[i]+=arr[i][j];
        for(int i=0;i<4;i++)
        for(int j=0;j<4;j++)
        ro[i+4]+=arr[j][i];
        ro[8]=arr[0][0]+arr[1][1]+arr[2][2]+arr[3][3];
        ro[9]=arr[3][0]+arr[2][1]+arr[1][2]+arr[0][3];
        for(int i=0;i<10;i++)
        {
            if(ro[i]==4||ro[i]==8)
            {
                cout<<"Case #"<<t<<": X won"<<endl;
                flag=1;break;
            }
            else if(ro[i]==40||ro[i]==35)
            {
                cout<<"Case #"<<t<<": O won"<<endl;
                flag=1;break;
            }
        }
        if(flag==0&&(s==83||s==88))cout<<"Case #"<<t<<": Draw"<<endl;
        else if(flag==0) cout<<"Case #"<<t<<": Game has not completed"<<endl;
        
            
    }
    return 0;
    
}
