#include<bits/stdc++.h>
using namespace std;
typedef pair<int,int> pii;
typedef unsigned long long lli;
bool flag[11];
int main() {
    ifstream fin("input.txt");
    ofstream fout("output.txt");
    int t,case_no=1;
    fin>>t;
    while(t--)
    {
        memset(flag,false,sizeof(flag));
        lli n,save;
        fin>>n;
        save=n;
        if(n==0)
        {
            fout<<"Case #"<<case_no<<": INSOMNIA\n";
            case_no++;
            continue;
        }
        int tt=0;
        while(true)
        {
            //tt++;
            bool f=true;
            for(int i=0;i<=9;i++)
            {
                if(flag[i]==false)f=false;
            }
            if(f)
            {
               fout<<"Case #"<<case_no<<": "<<n-save<<"\n";
               //fout<<tt;
               case_no++;
               break;
            }
            lli tmp=n;
            while(n>0)
            {
                int k=n%10;
                flag[k]=true;
                n/=10;
            }
            n=tmp+save;
        }
    }
    return 0;
}
