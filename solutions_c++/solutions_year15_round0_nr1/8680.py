#include<iostream>
#include<fstream>
using namespace std;

int main()
{
    std::ios_base::sync_with_stdio(false);
    int t,T;
    cin>>t;
    T=t;

    ofstream myfile;
    myfile.open ("Asmall.out");

    char str[1080];
    int maxS,per,curPer,ans;
    while(t--)
    {
        cin>>maxS;
        cin>>str;
        curPer=0;
        ans=0;
        for(int i=0;i<=maxS;i++)
        {
            if(curPer<i)
            {
                ans+=(i-curPer);
                curPer=i;
            }
            per=str[i]-'0';
            curPer+=per;
        }
        //cout<<"Case #"<<T-t<<": "<<ans<<"\n";
        myfile<<"Case #"<<T-t<<": "<<ans<<"\n";
    }
    myfile.close();
    return 0;
}
