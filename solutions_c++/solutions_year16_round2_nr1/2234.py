#include<bits/stdc++.h>
using namespace std;

int main()
{
    freopen("in3.in","r",stdin);
    freopen("out3.out","w",stdout);

    int i,j,k,n;
    int t;
    int x,y;

    string str,result;

    cin>>n;
    cin.ignore(256,'\n');

    t=1;
    while(t<=n)
    {
        getline(cin,str);
        vector<int> freq(26,0);

        for(i=0;i<str.length();i++)
        {
            freq[str[i]-'A']++;
        }

        vector<int> number(10,0);

        if(freq['Z'-'A']>0)
        {
            //zeroes
            x=freq['Z'-'A'];

            number[0]=x;

            //decrease ZERO
            freq['Z'-'A']-=x;
            freq['E'-'A']-=x;
            freq['R'-'A']-=x;
            freq['O'-'A']-=x;
        }

        if(freq['W'-'A']>0)
        {
            //zeroes
            x=freq['W'-'A'];

            number[2]=x;

            //decrease TWO
            freq['T'-'A']-=x;
            freq['W'-'A']-=x;
            freq['O'-'A']-=x;
        }
        
        if(freq['U'-'A']>0)
        {
            //zeroes
            x=freq['U'-'A'];

            number[4]=x;

            //decrease FOUR
            freq['F'-'A']-=x;
            freq['O'-'A']-=x;
            freq['U'-'A']-=x;
            freq['R'-'A']-=x;
        }
        
        if(freq['X'-'A']>0)
        {
            x=freq['X'-'A'];

            number[6]=x;

            //decrease SIX
            freq['S'-'A']-=x;
            freq['I'-'A']-=x;
            freq['X'-'A']-=x;
        }

        if(freq['G'-'A']>0)
        {
            x=freq['G'-'A'];

            number[8]=x;

            //decrease EIGHT
            freq['E'-'A']-=x;
            freq['I'-'A']-=x;
            freq['G'-'A']-=x;
            freq['H'-'A']-=x;
            freq['T'-'A']-=x;
        }
        
        if(freq['O'-'A']>0)
        {
            x=freq['O'-'A'];

            number[1]=x;

            //decrease ONE
            freq['O'-'A']-=x;
            freq['N'-'A']-=x;
            freq['E'-'A']-=x;
        }
        
        if(freq['R'-'A']>0)
        {
            x=freq['R'-'A'];

            number[3]=x;

            //decrease THREE
            freq['T'-'A']-=x;
            freq['H'-'A']-=x;
            freq['R'-'A']-=x;
            freq['E'-'A']-=x;
            freq['E'-'A']-=x;
        }
        
        if(freq['F'-'A']>0)
        {
            x=freq['F'-'A'];

            number[5]=x;

            //decrease FIVE
            freq['F'-'A']-=x;
            freq['I'-'A']-=x;
            freq['V'-'A']-=x;
            freq['E'-'A']-=x;
        }
        
        if(freq['S'-'A']>0)
        {
            x=freq['S'-'A'];

            number[7]=x;

            //decrease THREE
            freq['S'-'A']-=x;
            freq['E'-'A']-=x;
            freq['V'-'A']-=x;
            freq['E'-'A']-=x;
            freq['N'-'A']-=x;
        }

        if(freq['I'-'A']>0)
        {
            x=freq['I'-'A'];

            number[9]=x;

            //decrease NINE
            freq['N'-'A']-=x;
            freq['I'-'A']-=x;
            freq['N'-'A']-=x;
            freq['E'-'A']-=x;
        }

        cout<<"Case #"<<t<<": ";

        for(i=0;i<10;i++)
        {
            for(j=1;j<=number[i];j++)
            {
                cout<<i;
            }
        }

        cout<<endl;
        t++;
    }

    return 0;
}
