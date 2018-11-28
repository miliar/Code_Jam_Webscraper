#include <bits/stdc++.h>

using namespace std;
double eps=0.00001;
map<string,vector<int>> rec;
string reci[3010];
vector<int> poj[3010];
void getwords(int idx,string s)
{
    string word="";
    for(int i=0; i<s.length(); i++)
    {
        if(s[i]==' ')
        {
            rec[word].push_back(idx);
            word="";
        }
        else word+=s[i];
    }
    if(word!="")rec[word].push_back(idx);
}
int main()
{
    int t;
    freopen("input.txt","r",stdin);
   freopen("output.txt","w",stdout);
    int idx=1;
    scanf("%d",&t);
    string emp;
    getline(cin,emp);
    while(t--)
    {
       // cout<<"TP: "<<idx<<endl;
        rec.clear();
        int n;
        scanf("%d",&n);
        getline(cin,emp);
        for(int i=0; i<n; i++)
        {
            string seq;
            getline(cin,seq);
            getwords(i,seq);
        }
        int ans=999999;
        map<string,vector<int> >::iterator it;
        int fix=0;
        int cur=0;
        //cout<<"odabrane reci ";
        for(it=rec.begin();it!=rec.end();++it)
        {
            vector<int> v=it->second;
            string word=it->first;
            if(v.size()==2&&v[0]==0&&v[1]==1)
            {
                fix++;
            }
            else if(v.size()==1&&(v[0]==0||v[0]==1))continue;
            else
            {
               reci[cur]=word;
               poj[cur]=v;
               cur++;
          //     cout<<word<<" ";
            }
        }
        //cout<<endl;
        n-=2;

        for(int i=0; i<(1<<n); i++)
        {
            int curans=fix;
            for(int j=0;j<cur;j++)
            {
                bool eng=false,fra=false;
                for(int k=0;k<poj[j].size();k++)
                {
                    int num=poj[j][k];
                    if(num==0)eng=true;
                    else if(num==1)fra=true;
                    else
                    {
                        num-=2;
                        if(i&(1<<num))eng=true;
                        else fra=true;
                    }
                }
                if(eng&&fra)curans++;
            }
            ans=min(ans,curans);
        }
        printf("Case #%d: %d\n",idx++,ans);
    }
    return 0;
}
