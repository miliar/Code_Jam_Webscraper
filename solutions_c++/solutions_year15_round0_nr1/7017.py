#include<iostream>
#include<vector>
#include<algorithm>
#include<numeric>
#include<fstream>
using namespace std;
int main()
{

    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int tt;
    cin>>tt;
    for(int test=1;test<=tt;test++)
    {
        int smax;
        string str;
        cin>>smax;
        cin>>str;

        int stand=str[0]-'0';
        int ans=0;
        if(stand==0)
        {
            ans=1;
            stand=1;
        }
        int len=str.size();


        vector <int> v(len,1);
        v[0]=0;
        int temp=0;
       // for(int i=1;i<=smax;i++)
        {
            for(int j=1;j<len;j++)
            {
                int s=str[j]-'0';
                if(stand>=j&&s!=0)
                {
                        stand+=s;



                }
                else if(s!=0&&stand<j){
                        temp=j-stand;

                        ans+=temp;
                        stand+=temp+(str[j]-'0');


                }

            }

        }



        cout<<"Case #"<<test<<": "<<ans<<endl;




    }

}
