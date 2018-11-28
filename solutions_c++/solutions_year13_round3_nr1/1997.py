#include<iostream>
#include<fstream>
using namespace std;
int main()
{
    string s;
    long long int sum,r,l,p;
    int tt,t,y,x,i,len,offset,sw;
    cin>>t;
    for(tt=1;tt<=t;tt++)
    {
                        sum=0;
                        cin>>s>>x;
                        len=s.length();
                        offset=0;
                        l=0;
                        y=0;
                        for(i=0;i<len;i++)
                        {
                                             if(s[i]=='a'||s[i]=='i'||s[i]=='o'||s[i]=='e'||s[i]=='u')
                                             {
                                                     if(y>=x)
                                                     {
                                                             r=len-i;
                                                             l-=offset;
                                                             p=y-x+1;
                                                             sum+=(r+1)*(l+1)+(y-x)*(r+l)+(p*(p+1))/2;
                                                             sum-=1;
                                                             offset=i-x+1;
                                                     }
                                                     sw=1;
                                                     y=0;
                                             }
                                             else if(sw==0)
                                             y++;
                                             else if(sw==1)
                                             {
                                                  l=i;
                                                  y++;
                                                  sw=0;
                                             }
                        }
                        if(sw==0&&y>=x)
                        {
                           r=len-i;
                           l-=offset;
                           p=y-x+1;
                           sum+=(r+1)*(l+1)+(y-x)*(r+l)+(p*(p+1))/2;
                           sum-=1;
                        }
                        cout<<"Case #"<<tt<<": "<<sum<<endl;
    }
}     
