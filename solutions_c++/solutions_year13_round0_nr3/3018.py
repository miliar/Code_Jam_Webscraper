#include<iostream>
#include<fstream>
#include<vector>
#include<string>
#include<math.h>
#include<sstream>

using namespace std;

vector<string> v;
void palin(string &s,int n,int l)
{
    int i;
    if(n>(int)(l/2.0+0.5))
    {v.push_back(s);return;}
    for(i=0;i<=9;i++)
    {
        s[n-1]=s[l-n]=i+'0';
        palin(s,n+1,l);
    }
}

bool check(long long int b)
{
    int l=0;
    string a;
    while(b>0)
    {
        a.push_back(b%10+'0');
        b=b/10;l++;
    }
    int i=0,j=l-1;
    while(i<=j && a[i]==a[j])
    {
        i++;j--;
    }
    if(i>j)
    return 1;
    else
    return 0;
}

int main()
{
    int i,j,t,p,n,m,k,an,a,b;
    ifstream fin("input.txt");
    ofstream fout("output.txt");

    for(i=1;i<=7;i++)
    {
        string s(i,0);
        for(j=1;j<=9;j++)
        {s[0]=s[i-1]=j+'0';
        palin(s,2,i);}
    }
    typeof(v.end()) it;
    fin>>t;
    for(p=1;p<=t;p++)
    {
        fin>>a>>b;
        float s=sqrt(a),e=sqrt(b);
        int ans=0;
        //cout<<"here";
        for(it=v.begin();it!=v.end();it++)
        {
            string s1=*it;
            stringstream ss;
            ss<<s1;
            int a1;
            ss>>a1;
            if(a1<s)
            continue;
            if(a1>e)
            break;
            long long int b=a1*a1;
            if(check(b))
            {cout<<b<<" ";ans++;}
        }
         fout<<"Case #"<<p<<": "<<ans<<"\n";
    }
    return 0;
}
