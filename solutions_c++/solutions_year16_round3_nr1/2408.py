#include<bits/stdc++.h>
using namespace std;
ifstream fin("A-large.in");
ofstream fout("out26.txt");
bool comp(pair<int,int>p,pair<int,int>p1)
{
    if(p.first>p1.first)
        return true;
    else if(p.first==p1.first)
    {
        if(p.second<p1.second)
            return true;
        else
            return false;
    }
    else
        return false;
}
int main()
{
    //ios_base::sync_with_stdio(false);
    //fin.tie(false);
    char ch='A';
    char cha[26];
    for(int i=0;i<26;i++)
    {
        cha[i]=ch;
        ch++;
    }
    int t;
    fin>>t;
    int h=1;
    while(t--)
    {
        int n;
        fin>>n;
        int arr[n];
        vector<pair<int,int> >v;
        int sum=0;
        for(int i=0;i<n;i++)
        {
            fin>>arr[i];
            v.push_back(make_pair(arr[i],i));
            sum=sum+arr[i];
        }
        vector<string>v1;
        while(sum>0)
        {
           sort(v.begin(),v.end(),comp);
          // fout<<v[0].first<<" "<<v[1].first<<" ";
           if(v[0].first==v[1].first)
           {
            string w;
            char a=cha[v[0].second];
            char b=cha[v[1].second];
            w=w+a+b;
            v1.push_back(w);
            //fout<<w<<"\n";
            v[0].first=v[0].first-1;
            v[1].first=v[1].first-1;
            sum=sum-2;
           }
           else
           {
                string w;
            char a=cha[v[0].second];
            w=w+a ;
            v1.push_back(w);
           // fout<<w<<"\n";
            v[0].first=v[0].first-1;
            sum=sum-1;
           }

        }

        int l=v1.size();

        if(v1[l-1].length()==1)
        {
            for(int i=l-2;i>=0;i--)
            {
               // fout<<v1[i]<<"\n";
                if(v1[i].length()==2)
                {
                    string a=v1[i];
                    char c=v1[i][0];
                    char b=v1[i][1];
                    string w;
                    w=w+c;
                    v1[i]=w;
                    v1[l-1]=v1[l-1]+b;
                    //fout<<v1[i]<<" "<<v1[l-1]<<"\n";
                    break;
                }
            }
        }
        fout<<"Case #"<<h<<":"<<" ";
        for(int i=0;i<l;i++)
        {
            fout<<v1[i]<<" ";
        }
        fout<<"\n";
        h++;
    }
    return 0;
}
