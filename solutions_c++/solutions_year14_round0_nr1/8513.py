#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cctype>
#include<cmath>
#include<iostream>


using namespace std;


int case_no,t=1,i,j,k,a,b,c,d,first_cards[4][4],second_cards[4][4];

double rec(double curTime, double curPro, double rest)
{
    double re=C/curPro;
    if(re)return re=re+rest/curPro;

    re += C/curPro;
    return re=rec(re,curPro+F,rest-C);
}


int main()
{
   // freopen("in.txt","r",stdin);
  //  freopen("out.txt","w",stdout);
    cin>>case_no;
    for(t=1;t<=case_no;t++)
    {
        cin>>a;a--;
        for(i=0;i<16;i++)cin>>first_cards[i/4][i%4];
        cin>>b;b--;
        for(i=0;i<16;i++)cin>>second_cards[i/4][i%4];
        c=0;
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                if(first_cards[a][i]==second_cards[b][j])
                {
                    c++;
                    d=first_cards[a][i];
                }
            }
        }
        printf("Case #%d: ",t);
        if(c==0)cout<<"Volunteer cheated!\n";
        else if(c==1)cout<<d<<endl;
        else cout<<"Bad magician!\n";
    }
    return 0;
}

