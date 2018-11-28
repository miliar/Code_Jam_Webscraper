#include<iostream>
using namespace std;
int main()
{
    freopen("A:\\in.in","r",stdin);
    freopen("A:\\out.txt","w",stdout);
    int t,c=1;
    cin>>t;
    while(t--)
    {
        string arr[4];
        for(int i=0;i<4;i++)
        cin>>arr[i];
        
        int s=0,o=0,d=0;
        for(int i=0;i<4;i++)
        {
                int scount=0,ocount=0;
                for(int j=0;j<4;j++)
                {
                        if(arr[i][j]=='X'||arr[i][j]=='T')
                        scount++;
                        if(arr[i][j]=='O'||arr[i][j]=='T')
                        ocount++;
                }
                if(scount==4)
                {
                             s=1;
                             break;
                }
                if(ocount==4)
                {
                             o=1;
                             break;
                }
        }
        //cout<<o<<"\n";
        for(int i=0;i<4;i++)
        {
                int scount=0,ocount=0;
                for(int j=0;j<4;j++)
                {
                        if(arr[j][i]=='X'||arr[i][j]=='T')
                        scount++;
                        if(arr[j][i]=='O'||arr[i][j]=='T')
                        ocount++;
                }
                if(scount==4)
                {
                             s=1;
                             break;
                }
                if(ocount==4)
                {
                             o=1;
                             break;
                }
        }
        //cout<<o<<"\n";
        int scount=0,ocount=0;
        for(int i=0;i<4;i++)
        {
                if(arr[i][i]=='X'||arr[i][i]=='T')
                scount++;
                if(arr[i][i]=='O'||arr[i][i]=='T')
                ocount++;
                if(scount==4)
                {
                             s=1;
                             break;
                }
                if(ocount==4)
                {
                             o=1;
                             break;
                }
                
        }

        if((arr[0][3]=='X'||arr[0][3]=='T')&&(arr[1][2]=='X'||arr[1][2]=='T')&&(arr[2][1]=='X'||arr[2][1]=='T')&&(arr[3][0]=='X'||arr[3][0]=='T'))
        s=1;
        
        if((arr[0][3]=='O'||arr[0][3]=='T')&&(arr[1][2]=='O'||arr[1][2]=='T')&&(arr[2][1]=='O'||arr[2][1]=='T')&&(arr[3][0]=='O'||arr[3][0]=='T'))
        o=1;
        //cout<<o<<"\n";
        if(s==0&&o==0)
        for(int i=0;i<4;i++)
        {
                for(int j=0;j<4;j++)
                {
                        if(arr[i][j]=='.')
                        d=1;
                }
        }
        if(s==1)
        cout<<"Case #"<<c<<": X won"<<"\n";
        else if(o==1)
        cout<<"Case #"<<c<<": O won"<<"\n";
        else if(d==1)
        cout<<"Case #"<<c<<": Game has not completed"<<"\n";
        else
        cout<<"Case #"<<c<<": Draw"<<"\n";
        
        c++;
    }
}
