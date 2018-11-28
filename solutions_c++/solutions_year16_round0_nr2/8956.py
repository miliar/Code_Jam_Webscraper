#include <bits/stdc++.h>

using namespace std;

int main()
{
    int test,length,i,ans;
    string s;
    cin>>test;
    for(int zam=1;zam<=test;zam++)
    {
       
        cin>>s;
        length=s.length();
            ans=0;
            i=0;
                while(s[i]=='-' && i<length)
                {
                    i++;
                    ans=1;
                }
                while(i<length)
                {
                while(s[i]=='+' && i<length)
                    i++;
                if(s[i]=='-')
                {
                    ans+=2;
                    while(s[i]=='-' && i<length)
                        i++;
                }
                }
         std::cout<<"Case #"<<zam<<": "<<ans<<endl;
    }
    return 0;
}
	