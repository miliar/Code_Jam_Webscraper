#include <bits/stdc++.h>
using namespace std;
char z[30];
vector<int>v;
int main()
{

    freopen("dw.txt","r",stdin);
    freopen("out1.txt","w",stdout);
    int a,b,c,d,e,f,g,h,i,j,k,p,q;
    int x[10]={0,2,6,8,3,4,5,7,1,9};
    char s[3001];
    cin>>a;
    for(k=1;k<=a;k++)
    {   v.clear();
        memset(z,0,sizeof(z));
        cin>>s;
        b=strlen(s);
        for(j=0;j<b;j++)
        {
            z[s[j]-'A']++;
        }
        for(p=0;p<=9;p++)
        {   i=x[p];
            if(i==9)
            {
                f=z['N'-'A']/2;
                for(j=0;j<f;j++)
                {
                    v.push_back(i);
                }
                z['N'-'A']-=2*f;
                z['I'-'A']-=f;
                z['E'-'A']-=f;


            }
            else if(i==8)
            {
                f=z['G'-'A'];

                for(j=0;j<f;j++)
                {
                    v.push_back(i);
                }
                z['H'-'A']-=f;
                z['G'-'A']-=f;
                z['I'-'A']-=f;
                z['E'-'A']-=f;
                z['T'-'A']-=f;

            }
            else if(i==7)
            {

                g=z['S'-'A'];

                for(j=0;j<g;j++)
                {
                    v.push_back(i);
                }
                z['E'-'A']-=g*2;
                z['S'-'A']-=g;
                z['V'-'A']-=g;
                z['N'-'A']-=g;

            }
            else if(i==6)
            {

                f=z['X'-'A'];

                for(j=0;j<f;j++)
                {
                    v.push_back(i);
                }
                z['I'-'A']-=f;
                z['X'-'A']-=f;
                z['S'-'A']-=f;

            }
            else if(i==5)
            {
                g=z['F'-'A'];

                for(j=0;j<g;j++)
                {
                    v.push_back(i);
                }
                z['F'-'A']-=g;
                z['I'-'A']-=g;
                z['V'-'A']-=g;
                z['E'-'A']-=g;

            }
            else if(i==4)
            {

                g=z['R'-'A'];

                for(j=0;j<g;j++)
                {
                    v.push_back(i);
                }
                z['F'-'A']-=g;
                z['O'-'A']-=g;
                z['U'-'A']-=g;
                z['R'-'A']-=g;
            }
            else if(i==3)
            {

                g=z['H'-'A'];



                for(j=0;j<g;j++)
                {
                    v.push_back(i);
                }
                z['E'-'A']-=g*2;
                z['H'-'A']-=g;
                z['T'-'A']-=g;
                z['R'-'A']-=g;
            }
            else if(i==2)
            {

                f=z['W'-'A'];

                for(j=0;j<f;j++)
                {
                    v.push_back(i);
                }
                z['T'-'A']-=f;
                z['W'-'A']-=f;
                z['O'-'A']-=f;
            }
            else if(i==1)
            {
                f=z['O'-'A'];

                for(j=0;j<f;j++)
                {
                    v.push_back(i);
                }
                z['O'-'A']-=f;
                z['N'-'A']-=f;
                z['E'-'A']-=f;
            }
            else if(i==0)
            {
                g=z['Z'-'A'];

                for(j=0;j<g;j++)
                {
                    v.push_back(i);
                }
                z['Z'-'A']-=g;
                z['E'-'A']-=g;
                z['R'-'A']-=g;
                z['O'-'A']-=g;
            }
        }
        sort(v.begin(),v.end());
        e=v.size();
        cout<<"Case #"<<k<<": ";
        for(i=0;i<e;i++)
            cout<<v[i];
        cout<<endl;

    }

 return 0;



    }
