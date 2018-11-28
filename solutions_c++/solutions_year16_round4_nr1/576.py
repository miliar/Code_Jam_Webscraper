#include <bits/stdc++.h>
#define MOD 1000000007

using namespace std;

typedef long long ll;
typedef pair<int,int> ii;
typedef pair<int,ii> iii;
typedef pair<string,string> ss;

string rez;
int n,a,b,c;

void sortrez(int n,int s){
    if(n==0)
        return;
    int offset=1<<(n-1);
    sortrez(n-1,s);
    sortrez(n-1,s+offset);
    for(int ctr1=s;ctr1<s+offset;ctr1++)
    {
        if(rez[ctr1]>rez[ctr1+offset]){
            for(int ctr2=0;ctr2<offset;ctr2++)
                swap(rez[s+ctr2],rez[s+ctr2+offset]);
            break;
        }
        else if(rez[ctr1]<rez[ctr1+offset])
            break;
    }

}

bool rek(int rock,int paper,int scisor){
    if(rock+paper+scisor==1){
        if(rock)
            rez="R";
        if(paper)
            rez="P";
        if(scisor)
            rez="S";
        return true;
    }
    int l=min(rock,scisor); // p
    for(int ctr1=0;ctr1<=l;ctr1++){
        if((paper-scisor+ctr1)==rock-ctr1){
            if(rek(ctr1,rock-ctr1,scisor-ctr1)){
                string rt;
                for(int ctr2=0;ctr2<rez.length();ctr2++){
                    if(rez[ctr2]=='R')
                        rt.push_back('R'),rt.push_back('S');
                    if(rez[ctr2]=='P')
                        rt.push_back('P'),rt.push_back('R');
                    if(rez[ctr2]=='S')
                        rt.push_back('P'),rt.push_back('S');
                }
                rez=rt;
                return true;
            }
        }
    }
    return false;
}


int main()
{
    ifstream fin("input.in");
    ofstream fout("output.out");
    int t;
    fin >> t;
    int T=t;

    while(t--)
    {
        rez.clear();
        fout<<"Case #"<<T-t<<": ";
        fin>>n>>a>>b>>c;
        if(rek(a,b,c)){
            sortrez(n,0);
            fout<<rez;
        }
        else fout<<"IMPOSSIBLE";
        fout<<"\n";

    }
    fin.close();
    fout.close();
    return 0;
}
