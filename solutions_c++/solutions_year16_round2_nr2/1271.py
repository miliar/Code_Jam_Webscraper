#include<bits/stdc++.h>
using namespace std;
string str[4][1000];
pair <int,int> pp[100001];
void operate(int n)
{
    int temp=n;
    string ptr="";
    while(n)
        ptr=(char)(n%10+'0')+ptr,n/=10;
    int m=ptr.size(),j;
    for(j=m;j<=3;j++)
        str[j][temp]=ptr,ptr="0"+ptr;
}
int main()
{
    ifstream cin("a.txt");
    ofstream cout("b.txt");
    int t,var=0,j,i;
    for(i=0;i<1000;i++)
        operate(i);
    string a,b;
    cin>>t;
    while(t--)
    {
        cin>>a>>b;
        var++;
        cout<<"Case #"<<var<<": ";
        vector <int> A,B;
        if(a.size()==1)
        {
            if(a=="?" && b=="?")
                cout<<0<<" "<<0<<'\n';
            else if(a=="?")
                cout<<b<<" "<<b<<'\n';
            else if(b=="?")
                cout<<a<<" "<<a<<'\n';
            else
                cout<<a<<" "<<b<<'\n';
        }
        else if(a.size()==2)
        {
            for(i=0;i<100;i++)
            {
                bool cond=true;
                for(j=0;j<2;j++)
                    if(a[j]!='?' && a[j]!=str[2][i][j])
                        cond=false;
                if(cond)
                A.push_back(i);
                cond=true;
                for(j=0;j<2;j++)
                    if(b[j]!='?' && b[j]!=str[2][i][j])
                        cond=false;
                if(cond)
                B.push_back(i);
            }
            int ind=0,minn=10000;
            for(i=0;i<A.size();i++)
            for(j=0;j<B.size();j++)
            {
                if(minn>abs(A[i]-B[j]))
                    minn=abs(A[i]-B[j]),ind=0,pp[ind++]=make_pair(A[i],B[j]);
                else if(minn==abs(A[i]-B[j]))
                    pp[ind++]=make_pair(A[i],B[j]);
            }
            sort(pp,pp+ind);
            cout<<str[2][pp[0].first]<<" "<<str[2][pp[0].second]<<'\n';
        }
        else
        {
            for(i=0;i<1000;i++)
            {
                bool cond=true;
                for(j=0;j<3;j++)
                    if(a[j]!='?' && a[j]!=str[3][i][j])
                        cond=false;
                if(cond)
                A.push_back(i);
                cond=true;
                for(j=0;j<3;j++)
                    if(b[j]!='?' && b[j]!=str[3][i][j])
                        cond=false;
                if(cond)
                B.push_back(i);
            }
            int ind=0,minn=10000;
            for(i=0;i<A.size();i++)
            for(j=0;j<B.size();j++)
            {
                if(minn>abs(A[i]-B[j]))
                    minn=abs(A[i]-B[j]),ind=0,pp[ind++]=make_pair(A[i],B[j]);
                else if(minn==abs(A[i]-B[j]))
                    pp[ind++]=make_pair(A[i],B[j]);
            }
            sort(pp,pp+ind);
            cout<<str[3][pp[0].first]<<" "<<str[3][pp[0].second]<<'\n';
        }
    }
}
