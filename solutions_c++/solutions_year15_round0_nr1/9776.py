#include<iostream>
using namespace std;
int main()
{
    int test, maxm, x, cnt=0, fnd=0, zpos=0;
    string s;
    cin>>test;
    for(int k=1; k<=test; k++)
    {
        cin>>maxm;
        cin>>s;
        for(int i=maxm; i>0; i--){
            if(s[i]=='0'){
                zpos++;
            }
            else
                break;
        }
        //cout<<zpos<<endl;
        for(int i=0; i<maxm-zpos; i++)
        {
            x = s[i]-'0';
            cnt+=x;
            if(cnt<(i+1)){
                fnd++;
                cnt++;
            }
        }
        cout<<"Case #"<<k<<": "<<fnd<<endl;
        cnt=0, fnd=0, zpos=0;
    }
    return 0;
}
