#include <bits/stdc++.h>
#define REP(i,a,b) for(i=a;i<b;i++)
#define rep(i,n) REP(i,0,n)
#define ll long long
#define ull unsigned ll
using namespace std;
char s[100007],f[200][200];
int fm[200][200];
int pre()
{
    f[1]['i']='i';
    f[1]['j']='j';
    f[1]['k']='k';
    f[1][1]=1;
   	f['j']['j']=1;
    f['j']['k']='i';
    f['j'][1]='j';
    f['k']['i']='j';
    f['k']['j']='i';
    f['k']['k']=1;
    f['k'][1]='k';
   	f['i']['i']=1;
    f['i']['j']='k';
    f['i']['k']='j';
    f['i'][1]='i';
    f['j']['i']='k';
    for(int i=0;i<200;i++)
        for(int j=0;j<200;j++)
            fm[i][j]=1;
    fm['i']['i']=-1;
    fm['j']['j']=-1;
    fm['k']['k']=-1;
    fm['i']['k']=-1;
    fm['j']['i']=-1;
    fm['k']['j']=-1;
}
int main()
{
    freopen("input.txt","r",stdin);//redirects standard input
    freopen("output.txt","w",stdout);//redirects standard output
	pre();
    int t;
    cin>>t;
    for(int j=1;j<=t;j++)
    {
        int l,n,ans=0,flag=1,cnt=0;
        cin>>l>>n;
        cin>>s;
        char a=s[0];
        for(int i=1;i<=l*n;i++)
        {
            if(a=='i' && cnt==0)
            {

                cnt++;
                a=1;
            }
            else if(a=='j' && cnt==1)
            {

                cnt++;
                a=1;
            }
            else if(a=='k' && cnt==2)
            {

               if(i==l*n)
               {
                ans=11;
                break;
               }
            }
            int cf=a;
            a =  f[a][s[i%l]];
            flag=flag*fm[cf][s[i%l]];
        }

        if(ans==11 && flag==1)
            cout<<"Case #"<<j<<": YES"<<endl;
        else
             cout<<"Case #"<<j<<": NO"<<endl;
    }
    return 0;
}