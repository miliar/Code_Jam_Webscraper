#include <iostream>
#include <fstream>
#include <cstring>
using namespace std;
ifstream fin("A-large.in");
ofstream fout("fout-large.txt");
typedef unsigned long long uLong;
uLong data[4][4];
uLong count=0;
uLong countC[4];//ÁÐ
uLong countR[4];//ÐÐ
uLong countD[2];//Ð±Ïß
const uLong X=0x00000001;
const uLong O=0x00010000;
const uLong T=0x00010001;
int ans;
void clear()
{
    count=0;
    memset(data,0,sizeof(data));
    memset(countC,0,sizeof(countC));
    memset(countR,0,sizeof(countR));
    memset(countD,0,sizeof(countD));
}
bool JudgeOne(uLong & a)
{
    if((a&0xFFFF0000)==0x00040000)
    {
        ans=0;//O win
        return true;
    }
    if((a&0x0000FFFF)==0x0000004)
    {
        ans=1;//X win
        return true;
    }
    return false;
}
void Judge()
{
    int i=0;
    for(i=0;i<4;i++)
    {
        if(JudgeOne(countC[i]))
        {
            return ;
        }
        if(JudgeOne(countR[i]))
        {
            return ;
        }
    }
    if(JudgeOne(countD[0]))
    {
        return ;
    }
    if(JudgeOne(countD[1]))
    {
        return ;
    }
    if(count<16)
    {
        ans=2;
        return;
    }
    ans=3;

}
int main()
{
    int itemCount=0,i,j,k;
    char tmp;
    unsigned utmp;
    fin>>itemCount;
    k=0;
    while(k++<itemCount)
    {
        clear();
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                fin>>tmp;
                switch(tmp)
                {
                case 'X':
                    utmp=X;
                    count++;
                    break;
                case 'O':
                    utmp=O;
                    count++;
                    break;
                case 'T':
                    utmp=T;
                    count++;
                    break;
                default :
                    utmp=0;
                    break;
                }
                countR[i]+=utmp;
                countC[j]+=utmp;
                if(i+j==3)
                {
                    countD[0]+=utmp;
                }
                else if(i==j)
                {
                    countD[1]+=utmp;
                }
            }

        }
        Judge();
        fout<<"Case #"<<k<<": ";
        switch(ans)
        {
        case 0:
            fout<<"O won";
            break;
        case 1:
            fout<<"X won";
            break;
        case 2:
            fout<<"Game has not completed";
            break;
        default:
            fout<<"Draw";
            break;
        }
        fout<<endl;
    }
    fin.close();
    fout.close();
    return 0;
}
