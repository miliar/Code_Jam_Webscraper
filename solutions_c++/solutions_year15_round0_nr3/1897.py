#include<iostream>
#include<string>
using namespace std;



int main()
{
    long long t,n,x;
    cin>>t;
    char all;
    char l[20000];
    char biao[300][300];
    biao['1']['1']='1';
    biao['1']['2']='2';
    biao['1']['i']='i';
    biao['1']['j']='j';
    biao['1']['k']='k';
    biao['1']['I']='I';
    biao['1']['J']='J';
    biao['1']['K']='K';

    biao['i']['1']='i';
    biao['i']['2']='I'; 
    biao['i']['i']='2';
    biao['i']['j']='k';
    biao['i']['k']='J';
    biao['i']['I']='1';
    biao['i']['J']='K';
    biao['i']['K']='j';

    biao['j']['1']='j';
    biao['j']['2']='J';
    biao['j']['i']='K';
    biao['j']['j']='2';
    biao['j']['k']='i';
    biao['j']['I']='k';
    biao['j']['J']='1';
    biao['j']['K']='I';

    biao['k']['1']='k';
    biao['k']['2']='K';
    biao['k']['i']='j';
    biao['k']['j']='I';
    biao['k']['k']='2';
    biao['k']['I']='J';
    biao['k']['J']='i';
    biao['k']['K']='1';

    biao['2']['1']='2';
    biao['2']['2']='1';
    biao['2']['i']='I';
    biao['2']['j']='J';
    biao['2']['k']='K';
    biao['2']['I']='i';
    biao['2']['J']='j';
    biao['2']['K']='k';

    biao['I']['1']='I';
    biao['I']['2']='i';
    biao['I']['i']='1';
    biao['I']['j']='K';
    biao['I']['k']='j';
    biao['I']['I']='2';
    biao['I']['J']='k';
    biao['I']['K']='J';

    biao['J']['1']='J';
    biao['J']['2']='j';
    biao['J']['i']='k';
    biao['J']['j']='1';
    biao['J']['k']='I';
    biao['J']['I']='K';
    biao['J']['J']='2';
    biao['J']['K']='i';

    biao['K']['1']='K';
    biao['K']['2']='k';
    biao['K']['i']='J';
    biao['K']['j']='i';
    biao['K']['k']='1';
    biao['K']['I']='j';
    biao['K']['J']='I';
    biao['K']['K']='2';

    for (int tt=0;tt<t;tt++)
    {
        bool tf=true;
        cout<<"Case #"<<tt+1<<": ";
        cin>>n>>x;
        for (int i=0;i<n;i++)
            cin>>l[i];
        long long buf=0;
        long long pointer=0;
        char now = '1';
        while (now != 'i')
        {
            now = biao[now][l[pointer % n]];
            pointer++;
            buf++;
//            cout<<now<<' ';
            if (buf>4*n)
            {
                tf=false;
                break;
            }
        }
        if (!tf)
        {
            cout<<"NO"<<endl;
            continue;
        }
        buf=0;
        now = '1';
 //       cout<<pointer<<' ';
        while (now != 'j')
        {
            now = biao[now][l[pointer % n]];
            pointer++;
            buf++;
            if (buf>4*n)
            {
                tf=false;
                break;
            }
        }
        if (!tf)
        {
            cout<<"NO"<<endl;
            continue;
        }
  //      cout<<pointer<<' ';
        buf=0;
        now = '1';
        while (now != 'k')
        {
            now = biao[now][l[pointer % n]];
            pointer++;
            buf++;
            if (buf>4*n)
            {
                tf=false;
                break;
            }
        }
        if (!tf)
        {
            cout<<"NO"<<endl;
            continue;
        }
        if (pointer>n*x)
        {
            cout<<"NO"<<endl;
            continue;
        }
   //     cout<<pointer<<' ';
        now = '1';
        while (pointer % n !=0)
        {
            now = biao[now][l[pointer % n]];
            pointer++;
        }
        char ch='1';
        for (int i=0;i<n;i++)
            ch=biao[ch][l[i]];
 //       cout<<ch<<' ';
        for (int i=0;i<((x-pointer/n) % 4);i++)
            now = biao[now][ch];
        if (now == '1')
            cout<<"YES"<<endl;
        else
            cout<<"NO"<<endl;
    }
}
