#include<bits/stdc++.h>
using namespace std;

int main()
{
    ifstream fin;
    ofstream fout;
    fin.open("aud.in",ios::in);
    fout.open("ans1.txt",ios::out);
    int t,lol=0;
    fin>>t;
    while(t--)
    {
        lol++;
        int k,standup=0,toadd=0;
        char aud[1010];
        fin>>k;
        k++;
        fin>>aud[0];
        standup=aud[0]-'0';
        for(int i=1;i<k;i++)
        {
            fin>>aud[i];
            if((aud[i]-'0')==0)
                continue;
            if(i <= standup)
            {
                standup+=(aud[i]-'0');
            }
            else
            {
                toadd+=(i-standup);
                standup+=((aud[i]-'0')+toadd);
            }
        }
        fout<<"Case #"<<lol<<": "<<toadd<<endl;
    }
    fin.close();
    fout.close();
}
