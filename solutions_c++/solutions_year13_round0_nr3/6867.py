#include<iostream>
#include<cmath>
#include<cstring>
#include<sstream>
#include<algorithm>
using namespace std;
int main()
{
    int t,a,b,k;
    cin>>t;
    for(k=1;k<=t;k++)
    {
        int count=0;
        cin>>a>>b;
        for(int i=a;i<=b;i++)
        {
            double aa=sqrt(i);
            stringstream ss,ss1;
            ss<<i;
            string s=ss.str(),s2;
            int kk=s.length();
            bool flag=1;
            //cout<<kk<<endl;
            for(int z=0;z<=kk/2;z++)
            {   
                if(s[z]!=s[kk-z-1])
                    flag=0;
            }
            //cout<<aa<<" "<<s<<endl;
            if(flag)
            {
                if(aa-int(aa)==0)
                {
                    ss1<<aa;
                    s2=ss1.str();
                    kk=s2.length();
                    for(int z=0;z<=kk/2;z++)
                        if(s2[z]==s2[kk-z-1])
                            flag=0;
                    //cout<<s2<<endl;
                    if(!flag)
                    {
                        count++;
                      //  cout<<s<<" "<<s2<<" "<<endl;
                    }
                }
            }
        }
        cout<<"Case #"<<k<<": "<<count<<endl;
    }
    return 0;
}
