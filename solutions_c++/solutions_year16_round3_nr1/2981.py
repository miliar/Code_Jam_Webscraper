#include<iostream>
#include<cstdio>
#include<map>
#include<set>
#include<iomanip>
using namespace std;
long long int nhj[79],nfkgid,kjfdsjifhjsdjfo,joieruiogjeossk,jglkfdkjhoid;
int main()
{
 freopen("input.in","r",stdin);
    freopen("oput.txt","w",stdout);
    long int i,gugu1,gintahu=1,gum,t;
    scanf("%ld",&t);
    while(t--)
    {
        long long int sum=0,bjsdkjfhskjdhfjkfklsdlf,pap1=-99999999999,pap2=-999999999999,gugu2;
        cin>>gum;
        for(i=0;i<gum;i++)
        {
            cin>>nhj[i];
            sum+=nhj[i];
        }
        cout<<"Case #"<<gintahu<<": ";
        if(gum==1)
        {
            while(sum>=2)
            cout<<"AA"<<" ",sum-=2;
            if(sum>0)
            cout<<"A"<<" ",sum-=1;
        }
        else if(gum>=2)
        {
            while(sum>0)
            {
                for(i=0;i<gum;i++)
                {
                if(pap1<=nhj[i])
                {
                pap1=nhj[i];
                gugu1=i;
                }
                }
                for(i=0;i<gum;i++)
                {
                    if(i!=gugu1)
                    {
                        if(pap2<=nhj[i])
                        {
                            pap2=nhj[i];
                            gugu2=i;
                        }
                    }
                }
                if(pap1==pap2&&pap1!=1)
                {
                    nhj[gugu1]-=1;
                    nhj[gugu2]-=1;
                    sum-=2;

                    cout<<(char)('A'+gugu1)<<(char)('A'+gugu2)<<" ";
                }
                if(pap1==pap2&&pap1==1)
                {
                    if(sum%2==0)
                    {
                    nhj[gugu1]--;
                    nhj[gugu2]--;
                    sum-=2;

                    cout<<(char)('A'+gugu1)<<(char)('A'+gugu2)<<" ";
                    }
                    else
                    {
                    nhj[gugu1]--;
                    sum-=1;

                    cout<<(char)('A'+gugu1)<<" ";
                    }
                }
                else if(pap1!=pap2)
                {
                    nhj[gugu1]-=2;
                    sum-=2;
                    cout<<(char)('A'+gugu1)<<(char)('A'+gugu1)<<" ";
                }
                pap1=-9999999999;
                pap2=-9999999999;
            }
        }
        cout<<endl;
        gintahu++;
        }

return 0;
}
