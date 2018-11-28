#include<bits/stdc++.h>
using namespace std;

typedef long long int ll;

int main()
{
    ios_base::sync_with_stdio(false);
    ll T,N,i,j,cnt,sum;
    string str;
    freopen ("A-small-attempt1.in","r",stdin);
    freopen ("output.txt","w",stdout);
    cin>>T;
    for(j=0;j<T;++j)
    {
        cin>>N>>str;
        cnt = sum = 0;
        for(i=0;i<=N;++i)
        {
            //cout<<sum<<" "<<cnt<<"\n";
            if(sum<i)
            {
                if((str[i]-'0')!=0)
                {
                    cnt += i-sum;
                    sum += cnt;
                }
            }
            sum += str[i]-'0';
        }
        cout<<"Case #"<<j+1<<": "<<cnt<<"\n";
    }
    //fclose(stdin);
    //fclose(stdout);
    return 0;
}
