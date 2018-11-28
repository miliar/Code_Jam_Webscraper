#include <iostream>
#include <vector>
#include <set>
#include <cmath>
#include <stdio.h>
#include <string.h>
using namespace std;
typedef long long ll;
char arr[100007];
char m[200][200];
int mm[200][200];
//char val[4]={1,'i','j','k'};
int doo()
{
    m[1]['i']='i';
    m[1]['j']='j';
    m[1]['k']='k';
    m[1][1]=1;
    m['i']['i']=1;
    m['i']['j']='k';
    m['i']['k']='j';
    m['i'][1]='i';
    m['j']['i']='k';
    m['j']['j']=1;
    m['j']['k']='i';
    m['j'][1]='j';
    m['k']['i']='j';
    m['k']['j']='i';
    m['k']['k']=1;
    m['k'][1]='k';
    for(int i=0;i<200;i++)
        for(int j=0;j<200;j++)
            mm[i][j]=1;
    mm['i']['i']=-1;
    mm['j']['j']=-1;
    mm['k']['k']=-1;
    mm['i']['k']=-1;
    mm['j']['i']=-1;
    mm['k']['j']=-1;
}

int main()
{
    freopen("mn3.in","r",stdin);
    freopen("out.out","w",stdout);
    doo();
    int t;
    cin>>t;
    for(int q=1;q<=t;q++)
    {
        int l,n;
        cin>>l>>n;
        scanf("%s",arr);

        int ans=0;
        int cnt=0;
        char a=arr[0];
        int flg=1;

        for(int i=1;i<=l*n;i++)
        {
        //    cout<<" vis frus "<<(int)a;

            if(a=='i'&&cnt==0)
            {
               // cout<<"   in i "<<endl;
                cnt++;
                a=1;
            }
            else if(a=='j'&&cnt==1)
            {
                    //cout<<" in j "<<endl;
                cnt++;
                a=1;
            }
            else if(a=='k'&&cnt==2)
            {
               // cout<<" in k"<<endl;
               // cout<<" dude "<<(int)get('k');
               if(i==l*n)
               {
                ans=11;
                break;
               }

            }
            int pp=a;
            a =  m[a][arr[i%l]];
            flg=flg*mm[pp][arr[i%l]];
             //  cout<<" f "<<flg<<" a "<<(int)a<<" arr[i] "<<arr[i%l]<<" cnt "<<cnt<<endl;

        }
       // cout<<ans;
        if(ans==11&&flg==1)
            cout<<"Case #"<<q<<": YES"<<endl;
        else
             cout<<"Case #"<<q<<": NO"<<endl;
    }
}

