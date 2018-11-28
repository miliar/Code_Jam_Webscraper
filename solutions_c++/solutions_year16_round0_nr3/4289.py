#include<bits/stdc++.h>
#define rep(i) for(i=0;i<=1;i++)
using namespace std;

long long int convert(string s,long long int b)
{
    long long int i,ans=0,j;

    for(i=s.size()-1,j=1;i>=0;i--,j=j*b)
        if(s[i]=='1')
            ans=ans+j;

    return ans;
}



main()
{
    freopen("in.txt","r",stdin);
    freopen("output.txt","w",stdout);

    long long int i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12,i13,i14,i,j=0,T,x,y,cs;


    char s[20],str[]="01";

    s[0]='1';
    cin>>T;
    for(cs=1;cs<=T;cs++)
    {
        cin>>x>>y;

        cout<<"Case #"<<cs<<":"<<endl;

        rep(i1)rep(i2)rep(i3)rep(i4)rep(i5)rep(i6)rep(i7)rep(i8)rep(i9)rep(i10)rep(i11)rep(i12)rep(i13)rep(i14)
        {
            //cout<<i1<<endl;
            s[1]=str[i1];
            s[2]=str[i2];
            s[3]=str[i3];
            s[4]=str[i4];
            s[5]=str[i5];
            s[6]=str[i6];
            s[7]=str[i7];
            s[8]=str[i8];
            s[9]=str[i9];
            s[10]=str[i10];
            s[11]=str[i11];
            s[12]=str[i12];
            s[13]=str[i13];
            s[14]=str[i14];
            s[15]='1';

            s[16]='\0';

            string str(s);
            int k=0;

            for(i=2;i<=10;i++)
            {
                long long int a;
                a=convert(str,i);
                //cout<<a<<" ";
                if(a%2==0||a%3==0||a%5==0||a%7==0||a%11==0)
                    k++;
            }
            //cout<<endl;
            //cout<<k<<endl;
            if(k==9)
            {
                j++;
                cout<<str<<" ";

                for(i=2;i<=10;i++)
                {
                    long long int a;
                    a=convert(str,i);
                    //cout<<a<<" ";
                    //cout<<"="<<a<<" ";
                    if(a%2==0)
                        cout<<2<<" ";
                    else if(a%3==0)
                        cout<<3<<" ";
                    else if(a%5==0)
                        cout<<5<<" ";
                    else if(a%7==0)
                        cout<<7<<" ";
                    else if(a%11==0)
                        cout<<11<<" ";
                }
                cout<<endl;
            }

            if(j==50)
                return 0;
        }

    }

    return 0;
}

