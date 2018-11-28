#include<cstdio>
#include<iostream>
#include<fstream>
#include<string>
#include<fstream>
using namespace std;

void func(int *a, int &n, int &sum)
{
    int k=n;
    while(k)
    {  if(!a[k%10])
         {a[k%10]++;
          sum++;
         }
        k/=10;
    }
    /*cout<<n<<endl;
    for(int i=0;i<10;i++)cout<<a[i]<<' ';
    cout<<endl;*/
}

int main()
{
    int t;
    fstream fout;
    fout.open("out2.txt",ios::out);
    cin>>t;
    for(int i=1;i<=t;i++)
    {
        string s;
        cin>>s;
        int k=s.length()-1;
        int ans=0;
        while(1)
        {
           while(k>=0&&s.at(k)=='+')k--;
           if(k<0)break;
           for(int i=0;i<=k;i++)
            if (s.at(i)=='+')
              s.at(i)='-';
           else
              s.at(i)='+';
           ans++;
        }

        fout<<"Case #"<<i<<": "<<ans<<endl;
    }
    return 0;
}
