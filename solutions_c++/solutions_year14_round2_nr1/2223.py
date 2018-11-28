#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<fstream>
using namespace std;

int main()
{
    int t,n,m;
    vector<string>str;
    vector<vector<int> >arr;
    vector<vector<char> >match;
    fstream in("A-small-attempt0.in");
    fstream out("out.txt");

    if(in.is_open()){
    in>>t;
    m=t;
    while(t-->0)
    {
        in>>n;
        str.resize(n);
        for(int i=0;i<n;i++)
            in>>str[i];

        arr.resize(n);
        for(int i=0;i<n;i++)arr[i].resize(100);

        for(int i=0;i<n;i++)for(int j=0;j<100;j++)arr[i][j]=0;

        match.resize(n);

        for(int i=0;i<n;i++)match[i].resize(100);

        int maxc=0;

        for(int i=0;i<n;i++)
        {
            int j=0,k=0;
            //cout<<str[i].length()<<endl;
            while(j<str[i].length())
            {
                char c=str[i].at(j);
                while(j<str[i].length() && c==str[i].at(j))
                {
                    arr[i][k]++;
                    j++;
                }
               // j++;
                match[i][k]=c;
                k++;

            }
            maxc=max(k,maxc);
        }
        bool flag=true;
        for(int j=0;j<maxc;j++)
        {
            char c=match[0][j];
            for(int i=1;i<n;i++)
            {
                if(c!=match[i][j])
                {
                    flag=false;
                    break;
                }
            }
            if(!flag)break;

        }
        if(!flag)
            out<<"Case #"<<m-t<<": Fegla Won"<<endl;
        else
        {
        int tcnt=0;
        for(int j=0;j<maxc;j++)
        {
            int cnt=0;
            for(int i=0;i<n;i++)
                cnt+=arr[i][j];

            if(cnt%n==0)
            {
                int a=cnt/n;
                for(int i=0;i<n;i++)
                {
                    tcnt+=abs(a-arr[i][j]);
                }
            }
            else
            {
                int tcnt1=0,tcnt2=0,b=cnt/n,c=cnt/n+1;
                for(int i=0;i<n;i++)
                {
                    tcnt1+=abs(b-arr[i][j]);
                }
                for(int i=0;i<n;i++)
                {
                    tcnt2+=abs(c-arr[i][j]);
                }
                tcnt+=min(tcnt1,tcnt2);
            }
        }
        out<<"Case #"<<m-t<<": "<<tcnt<<endl;
        }


    }
  }

  return 0;
}

