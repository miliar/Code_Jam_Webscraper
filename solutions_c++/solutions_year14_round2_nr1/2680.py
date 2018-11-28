#include<fstream>
#include<algorithm>
#include<cstring>
#include<string>
#include<cstdlib>
#include<vector>
#include<cstdio>
#include<iostream>
using namespace std;

string remdup(string a)
{
    int i=0;
    string x="";
    for(i=0;i<a.size();i++)
    {
        if(a[i]==a[i+1])
        {
            while(a[i]==a[i+1])
                    i++;
            //x+=a[i];
            i--;
        }
        else
            x+=a[i];
            //cout<<"x: " <<x<<endl;
    }
    return x;
}
int main()
{

    freopen("A.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t,ctr=1;
    int n,i;
    int a[100];
    int cnt[100][100];
    bool possible;
    vector<string> s;
    string x;
    cin>>t;
    while(ctr<=t)
    {
        possible=true;
        cin>>n;
        for(i=0;i<n;i++)
        {
            cin>>x;
            s.push_back(x);
        }
        x=remdup(s[0]);
        //cout<< "x: "<<x <<endl;
        for(i=1;i<n;i++)
        {
            if(x!=remdup(s[i]))
            {
                possible=false;
                break;
            }
        }
        if(possible)
        {
            int ind;
                for(int j=0;j<s.size();j++)
                {
                    ind=0;
                    string b=s[j];
                    int coun=1;
                    for(int k=0;k<b.size();k++)
                    {
                        if(b[k]==b[k+1])
                        {
                            while(b[k]==b[k+1])
                                    coun++,k++;
                            k--;

                        }
                        else{
                            cnt[j][ind++]=coun;
                        //cout<<"j: "<<j<<" ind: "<<ind-1<<" count :"<<coun<<endl;
                        coun=1;
                        }
                    }
                    cnt[j][ind]=coun;
                    //cout<<"j: "<<j<<" ind: "<<ind-1<<" count :"<<coun<<endl;
                }
/*
                for(i=0;i<s.size();i++)
                {
                    for(int j=0;j<ind;j++)
                        cout<<cnt[i][j]<<" ";
                    cout<<endl;
                }
*/
            int ans=0;
            int mean[100]={0};
            int j;
            for(i=0;i<s.size();i++)
                for(j=0;j<ind;j++)
                    mean[j]+=cnt[i][j];

            for(i=0;i<ind;i++)
            {
                mean[i]/=n;
                //cout<<mean[j]<<" ";
            }
            for(i=0;i<s.size();i++)
                for(int j=0;j<x.size();j++)
                    ans+=abs(cnt[i][j]-mean[j]);

            printf("Case #%d: %d\n",ctr++,ans);
        }
        else
        printf("Case #%d: Fegla Won\n",ctr++);
        s.clear();
    }
return 0;
}
