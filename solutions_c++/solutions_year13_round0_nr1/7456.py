#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <cmath>
using namespace std;
#define INF 0x3f3f3f3f

char ma[6][6];
bool wi[222];
int main()
{
	#ifdef Effca
	freopen("1.in","r",stdin);
	freopen("2.out","w",stdout);
	#endif
    int t,ca=1;
    cin>>t;
    while(t--)
    {
        cout<<"Case #"<<ca++<<": ";
        bool has=0;
        memset(wi,0,sizeof wi);
        for(int i=1;i<=4;i++)
            for(int j=1;j<=4;j++)
            {
                cin>>ma[i][j];
                if(ma[i][j]=='.') has=1;
            }
        for(int i=1;i<=4;i++)
        {
            int j=1,id=1;
            if(ma[i][id]=='T') {id++;j++;}
            for(j;j<=4;j++)
            {
                if(ma[i][j]=='.') break;
                if(ma[i][j]!=ma[i][id]&&ma[i][j]!='T') break;
            }

            if(j>4) wi[ma[i][id]]=1;

            id=1;j=1;
            if(ma[id][i]=='T') {id++;j++;}
            for(j;j<=4;j++)
            {
                if(ma[j][i]=='.') break;
                if(ma[j][i]!=ma[id][i]&&ma[j][i]!='T') break;
            }

            if(j>4) wi[ma[id][i]]=1;
        }

        int id=1,i=1;
        if(ma[1][1]=='T') {id=2;i++;}
        for(i;i<=4;i++)
        {
            if(ma[i][i]=='.') break;
            if(ma[i][i]!=ma[id][id]&&ma[i][i]!='T') break;
        }

        if(i>4) wi[ma[id][id]]=1;

        i=1;id=1;
        if(ma[1][4]=='T') {id =2;i++;}
        for(i;i<=4;i++)
        {
            if(ma[i][5-i]=='.') break;
            if(ma[i][5-i]!=ma[id][5-id]&&ma[i][5-i]!='T') break;
        }

        if(i>4) wi[ma[id][5-id]]=1;

        if(wi['X']==1&&wi['O']!=1) cout<<"X won"<<endl;
        if(wi['X']!=1&&wi['O']==1) cout<<"O won"<<endl;
        if(wi['X']!=1&&wi['O']!=1&&has) cout<<"Game has not completed"<<endl;
        if(wi['X']==1&&wi['O']==1) cout<<"Draw"<<endl;
        if(wi['X']!=1&&wi['O']!=1&&!has) cout<<"Draw"<<endl;
    }








	return 0;
}





