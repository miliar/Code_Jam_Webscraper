//#include<iostream>
#include<fstream>
#include<set>
using namespace std;

string str;
int len;
int memo[111][111];

void init()
{
    for(int i=0; i<111; i++)
        for(int j=0; j<111; j++)
            memo[i][j]=-1;

}

int dp(int idx, int counter){

    if(idx==len)
        return 0;

    int &res = memo[idx][counter];
    if(res!=-1)
        return res;

    if(str[idx]=='+'){

        res=dp(idx+1,counter+2);
         if(counter&1)
         res=min(res,1+dp(idx+1,counter+1));
        if(counter>=2)
        res=min(res,dp(idx+1,counter-counter%2));

    }
    else {
        res=1+dp(idx+1,counter+1);
        if(counter>0){
            if(counter&1)
            res=min(res,dp(idx+1,counter-1));
            else
                 res=min(res,dp(idx+1,counter));
        }
    }

    return res;
}
int main()
{
    int T;
    ifstream cin("/Users/saymyname/Desktop/Competitive/GCJ/B/input.txt");
    ofstream cout("/Users/saymyname/Desktop/Competitive/GCJ/B/output.txt");
    cin>>T;
    for(int i=1; i<=T; i++)
    {
        cin>>str;
        len = str.length();
        init();
        char last = str[0];
        int ans=0;
        for(int i=1;i<len;i++){
            if(str[i]!=last){
                last=str[i];
            ans++;
            }

        }
        if(last=='-')
            ans++;
        cout<<"Case #"<<i<<": "<<ans<<endl;
    }
    return 0;
}
