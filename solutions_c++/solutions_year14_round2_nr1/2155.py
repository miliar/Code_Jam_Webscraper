//#include<iostream>
#include<vector>
#include<fstream>
#include<cmath>
using namespace std;
ifstream cin("A-small-attempt0.in");
ofstream cout("A-small-attempt0.out");
int t;
vector<pair<int,int> > v;
int q[200][200];
int main()
{
    cin>>t;
    for(int ii=0;ii<t;ii++)
    {
        bool c=false;
        v.clear();
        for(int i=0;i<150;i++)
        for(int j=0;j<150;j++)
        q[i][j]=0;
        int n;
        cin>>n;
        string s;
        cin>>s;
        v.push_back(make_pair(s[0],1));
        for(int i=1;i<s.size();i++)
            if(s[i]==s[i-1])
                v[v.size()-1].second++;
            else
                v.push_back(make_pair(s[i],1));
        for(int i=0;i<v.size();i++)
            q[0][i]=v[i].second;
        for(int i=1;i<n;i++)
        {
            cin>>s;
            int k=0;
            if(s[0]!=v[0].first)
            {
                c=true;
                break;
            }
            q[i][0]=1;
            v[0].second++;
            for(int j=1;j<s.size();j++)
            {
                if(s[j]==s[j-1])
                {
                    q[i][k]++;
                    v[k].second++;
                }
                else
                if(s[j]==v[k+1].first)
                {
                    k++;
                    q[i][k]=1;
                    v[k].second++;
                }
                else
                {
                    c=true;
                    break;
                }
            }
            if(k<v.size()-1)
            c=true;
        }
        int sum=0;
        for(int i=0;i<v.size();i++)
        {
            if(v[i].second%n>n/2)
            {
                v[i].second/=n;
                v[i].second++;
            }
            else
            v[i].second/=n;
        }
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<v.size();j++)
                sum+=abs(v[j].second-q[i][j]);
                
        }
        cout<<"Case #"<<ii+1<<": ";
        if(c)
        cout<<"Fegla Won"<<endl;
        else
        cout<<sum<<endl;
    }
   // cin>>t;
}
