#include"iostream"
using namespace std;

int main()
{
    int T;
    int i,j;
    cin>>T;
    int cas=0;
    while(T--)
    {
      cas++;
        char a[4][4],b[3][3];
        int temp=0,x,y,done=0;
        for(i=0;i<4;i++)
            for(j=0;j<4;j++)
                cin>>a[i][j];
        cout<<"Case #"<<cas<<": ";
        int X1=0,X2=0,X3=0,X4=0,X5=0,X6=0,X7=0,X8=0;
        int O1=0,O2=0,O3=0,O4=0,O5=0,O6=0,O7=0,O8=0;
        for(i=0;i<4;i++)
        {
                if(a[0][i]=='X' || a[0][i]=='T')
                    X1++;
                if(a[i][0]=='X' || a[i][0]=='T')
                    X5++;
                if(a[1][i]=='X' || a[1][i]=='T')
                    X2++;
                if(a[i][1]=='X' || a[i][1]=='T')
                    X6++;
                if(a[2][i]=='X' || a[2][i]=='T')
                    X3++;
                if(a[i][2]=='X' || a[i][2]=='T')
                    X7++;
                if(a[3][i]=='X' || a[3][i]=='T')
                    X4++;
                if(a[i][3]=='X' || a[i][3]=='T')
                    X8++;
                if(a[0][i]=='O' || a[0][i]=='T')
                    O1++;
                if(a[i][0]=='O' || a[i][0]=='T')
                    O5++;
                if(a[1][i]=='O' || a[1][i]=='T')
                    O2++;
                if(a[i][1]=='O' || a[i][1]=='T')
                    O6++;
                if(a[2][i]=='O' || a[2][i]=='T')
                    O3++;
                if(a[i][2]=='O' || a[i][2]=='T')
                    O7++;
                if(a[3][i]=='O' || a[3][i]=='T')
                    O4++;
                if(a[i][3]=='O' || a[i][3]=='T')
                    O8++;
        }
            if(X1==4 || X2==4 || X3==4 || X4==4 || X5==4 || X6==4 || X7==4 || X8==4)
            {
                cout<<"X won"<<endl;
                done=1;
            }
            if(O1==4 || O2==4 || O3==4 || O4==4 || O5==4 || O6==4 || O7==4 || O8==4)
            {
                cout<<"O won"<<endl;
                done=1;
            }
            if((a[0][0]=='X' || a[0][0]=='T') && (a[1][1]=='X' || a[1][1]=='T') && (a[2][2]=='X' || a[2][2]=='T') && (a[3][3]=='X' || a[3][3]=='T'))
            {
                cout<<"X won"<<endl;
                done=1;
            }
            if((a[0][3]=='X' || a[0][3]=='T') && (a[1][2]=='X' || a[1][2]=='T') && (a[2][1]=='X' || a[2][1]=='T') && (a[3][0]=='X' || a[3][0]=='T'))
            {
                cout<<"X won"<<endl;
                done=1;
            }
    	    if((a[0][0]=='O' || a[0][0]=='T') && (a[1][1]=='O' || a[1][1]=='T') && (a[2][2]=='O' || a[2][2]=='T') && (a[3][3]=='O' || a[3][3]=='T'))
            {
                cout<<"O won"<<endl;
                done=1;
            }
            if((a[0][3]=='O' || a[0][3]=='T') && (a[1][2]=='O' || a[1][2]=='T') && (a[2][1]=='O' || a[2][1]=='T') && (a[3][0]=='O' || a[3][0]=='T'))
            {
                cout<<"O won"<<endl;
                done=1;
            }
            if(done==1)
              continue;
            int t=0;
            for(i=0;i<4;i++)
              for(j=0;j<4;j++)
              {
                if(t==0)
                {
                  if(a[i][j]=='.')
                  {
                    cout<<"Game has not completed"<<endl;
                    t=1;
                  }
                }
              }
            if(t==1)
              continue;
            cout<<"Draw"<<endl;
    }
    return 0;
}
