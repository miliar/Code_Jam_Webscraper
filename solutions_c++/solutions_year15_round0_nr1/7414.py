#include<iostream>
#include<string>
using namespace std;

int main()
{
    int t,i,j,smax,ppl,extra,num;
    string s;
    cin>>t;
    for(i=0;i<t;i++)
    {
        cin>>smax;
        cin>>s;
        
        ppl=0;
        extra=0;
        for(j=0;j<=smax;j++)
        {
            num=int(s[j])-48;
            if(ppl>=j && num)
                ppl+=num;
            else if(ppl<j)
            {
                extra+=(j-ppl);
                ppl+=(j-ppl+num);
            }
            //cout<<num<<" "<<j<<" "<<ppl<<" "<<extra<<endl;
        }
        cout<<"Case #"<<i+1<<": "<<extra<<endl;
    }
}






