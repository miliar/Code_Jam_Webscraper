#include<bits/stdc++.h>
using namespace std;
int main()
{
    //freopen("in.txt","r",stdin);
    //freopen("out.txt","w",stdout);
    int flag,k,n,i,j,alpha[26];
    string num[]={"ZERO","ONE","TWO","THREE","FOUR","FIVE","SIX","SEVEN","EIGHT","NINE"};
    string even="ZOWRUFXSGI";


    cin>>n;
    string str;
    for(i=0;i<n;i++)
    {
        vector<int> vec;
        cout<<"Case #"<<i+1<<": ";
        cin>>str;
        //cout<<str;
        for(j=0;j<26;j++)
            alpha[j]=0;
        for(j=0;j<str.length();j++)
            alpha[str[j]-'A']++;
        for(j=0;j<10;j+=2)
        {
            if(alpha[even[j]-'A'])
            {
                //cout<<alpha[even[j]-'A']<<"\n";
                int tmp=alpha[even[j]-'A'];
                for(k=0;k<tmp;k++)
                {

                    vec.push_back(j);
                    for(int l=0;l<num[j].length();l++)
                        alpha[num[j][l]-'A']--;
                }

                //ans+=alpha[even[j]-'A'];
            }
        }
        for(j=1;j<10;j+=2)
        {
            if(alpha[even[j]-'A'])
            {
                //cout<<alpha[even[j]-'A']<<" ";
                int tmp=alpha[even[j]-'A'];
                for(k=0;k<tmp;k++)
                {vec.push_back(j);
                for(int l=0;l<num[j].length();l++)
                    alpha[num[j][l]-'A']--;
                }
                //ans+=alpha[even[j]-'A'];
            }
        }
        sort(vec.begin(),vec.end());
        /*for(j=0;j<10;j+=2)
        {
            if(alpha[even[j])
            flag=0;
            while(!flag)
            {
                for(k=0;k<num[j].length();k++)
                {
                    if(alpha[num[j][k]-'A']>0)
                        alpha[num[j][k]-'A']--;
                    else
                    {
                        flag=1;
                        break;
                    }
                }
                if(flag)
                {
                    for(int l=0;l<k;l++)
                        alpha[num[j][l]-'A']++;
                }
                else
                {
                    cout<<j;
                }
            }
        }
        */
        for(j=0;j<vec.size();j++)
            cout<<vec[j];
        k=0;
        for(j=0;j<26;j++)
        {
            k+=alpha[j];
        }
        //cout<<" "<<k;
        cout<<"\n";

    }

    return 0;
}
