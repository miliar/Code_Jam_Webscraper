#include <iostream>
#include <fstream>
using namespace std;

int main()
{
    ofstream fout("key.txt", ios::out);
    ifstream fin("in.txt", ios::in);
    short S[1004];
    int T, n;
    fin>>T;
    int ctr=1;
    while(T--)
    {
        fin>>n;
        //cout<<"searching for "<<n<<" chars\n";
        string s;
        fin>>s;
        //cout<<s<<endl;
        for(int i=0; i<=n; i++)
        {
            S[i]=s[i]-'0';
            //cout<<S[i]<<" ";
        }
        //cout<<endl;
        int more=0;
        int curr=S[0];
        for(int i=1; i<=n; i++)
        {
            if(S[i]==0)
                continue;
            else
            {
                if(i <= curr)
                    curr+=S[i];
                else
                {
                    more+=(i-curr);
                    curr+=S[i]+i-curr;
                }

            }
        }
        fout<<"Case #"<<ctr++<<": "<<more<<endl;
    }
    fout.close();
    fin.close();
    return 0;
}
