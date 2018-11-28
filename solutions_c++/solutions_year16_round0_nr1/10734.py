#include<bits/stdc++.h>
using namespace std;
int main(void)
{   freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    int t,note;
    cin>>t;
    for(int j=1;j<=t;j++)
    {
        int n;
        cin>>n;
        vector <int> v;
        int i=1,m=0;
        xyz:
        ++m;
        i=m*n;
        int x=i,temp;
        while(x>0)
        {
            temp=x%10;
            v.push_back(temp);
            x/=10;
        }


        std::sort(v.begin(),v.end());

        int d=0;

        note=0;
        while(d<=9&&n!=0)
        {


            bool damn=binary_search(v.begin(),v.end(),d);
            if(damn)
            {
                if(d==9)
                {
                    note=m;
                    break;
                }

                else if(d<9)
                    ++d;
            }
            else
                goto xyz;
        }
        int answer=note*n;
        if(answer!=0)
        cout<<"Case #"<<j<<": "<<answer<<'\n';
        else
            printf("Case #%d: INSOMNIA\n",j);

    }
}
