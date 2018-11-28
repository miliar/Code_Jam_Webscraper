#include<iostream>
#include<fstream>
using namespace std;
int main()
{
    ifstream fin("A-large.in");
    ofstream fout("quesatry22211.txt");
    long long int T,i,j,k,temp,N,*ans;
    int cnt[10],flag=1;
    fin>>T;
    ans=new long long int [T];
    for(i=0;i<T;i++)
    {
        flag=1;
        for(k=0;k<10;k++)
            cnt[k]=0;
        fin>>N;
        fout<<"Case #"<<i+1<<": ";
        if(N!=0){
        for(j=1;flag==1;j++)
        {
            temp=N*j;
            while(temp!=0)
            {
                cnt[(temp%10)]=1;
                temp=temp/10;
            }
            flag=0;
            for(k=0;k<10;k++)
                if(cnt[k]==0)
                {
                    flag=1;
                    break;
                }

        }
        ans[i]=N*(j-1);
        fout<<ans[i];
        if(i<T)
            fout<<endl;
        }
        else
        {
            fout<<"INSOMNIA";
        if(i<T)
            fout<<endl;
        }
    }
    fin.close();
    fout.close();
    delete ans;
}
