#include<cstdio>
#include<iostream>
#include<fstream>
#include<string>
#include<fstream>
#include<vector>
using namespace std;

void add(char *a, int &n)
{
    int c=2;
    for(int i=n-1;i>=0;i--)
    {
        int p=a[i]-'0'+c;
        a[i]=p%2+'0';
        c=p/2;
        if(c==0)
            break;
    }
}
long long convert_base(char *a, int n, int b)
{
    long long ans=0;
    for(int i=0;i<n;i++)
        ans=ans*b+a[i]-'0';
    return ans;


}
int first_div(long long n)
{
    if(n%2==0) return 2;
    for(int i=3;i*i<=n;i+=2)
      if(n%i==0)return i;
    return -1;
}
int main()
{
    int t;
    fstream fout;
    fout.open("out3.txt",ios::out);
    cin>>t;
    for(int i=1;i<=t;i++)
    {
        int n,j;
        cin>>n>>j;
        char n1[n+1];
        vector<int>v[j];
        string ans[j];
        n1[0]=n1[n-1]='1';
        n1[n]='\0';
        for(int k=1;k<n-1;k++)
         n1[k]='0';
         int o=0;
        while(1)
        { vector<int>temp;
          for(int i=2;i<=10;i++)
          {
            int p=first_div(convert_base(n1,n,i));
            if(p==-1)break;
             temp.push_back(p);
          }
          if(temp.size()==9)
          {
             ans[o]=n1;
             v[o]=temp;
             o++;
             cout<<n1<<endl;
          }
          if(o==j)break;
          add(n1,n);
        }
        fout<<"Case #"<<i<<": \n";
        for(int k=0;k<j;k++)
        {fout<<ans[k]<<' ';
         for(int l=0;l<v[k].size();l++)
            fout<<v[k][l]<<' ';
         fout<<'\n';
        }
    }
    return 0;
}
