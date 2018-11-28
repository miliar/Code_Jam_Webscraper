#include<iostream>
using namespace std;

#define t(c)  if(((m[4*i]==c || m[4*i]=='T') && (m[4*i+1]==c ||m[4*i+1]=='T') && (m[4*i+2]==c || m[4*i+2]=='T') && (m[4*i+3]==c || m[4*i+3]=='T')) || \
              ((m[i]==c || m[i]=='T') && (m[i+4]==c ||m[i+4]=='T') && (m[i+8]==c || m[i+8]=='T') && (m[i+12]==c || m[i+12]=='T')) || \
              ((m[0]==c || m[0]=='T') && (m[5]==c ||m[5]=='T') && (m[10]==c || m[10]=='T') && (m[15]==c || m[15]=='T')) || \
              ((m[3]==c || m[3]=='T') && (m[6]==c ||m[6]=='T') && (m[9]==c || m[9]=='T') && (m[12]==c || m[12]=='T')))
#define f(i,n) for(int i=0;i<n;i++)
char m[16];
int co=0,cx=0,wx=0,wo=0;

int main()
{
    int t;
    int flag;
    cin>>t;

    f(j,t)
    {
        wx=0,wo=0,cx=0,co=0;
        flag=0;

        f(i,16)
        {
            cin>>m[i];
            if(m[i]=='T')flag=1;
            if(m[i]=='O')co++;
            else if(m[i]=='X')cx++;
        }

        f(i,4)
        {
            t('O') wo=1;
            t('X') wx=1;
        }

        cout<<"Case #"<<j+1<<": ";
        if(wx)cout<<"X won\n";
        else if(wo) cout<<"O won\n";
        else if(( cx+co==15 && flag)|| (cx+co==16)) cout<<"Draw\n";
        else cout<<"Game has not completed\n";
    }

    return 0;
}
