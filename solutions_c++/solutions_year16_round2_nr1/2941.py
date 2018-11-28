#include <iostream>
using namespace std;
#define ll long long
#include <vector>
#include <algorithm>

int main()
{   ll t,j;
    cin>>t;
    for(j=1;j<=t;++j)
    {   string s;
        ll i,z[26]={0},l,k=1;
        vector<int> w;
        cin>>s;
        l=s.length();
        for(i=0;i<l;++i)
            ++z[s[i]-65];
        k=1;
        cout<<"Case #"<<j<<": ";
        while(k)
        {   if(z[25] && z[4] && z[17] && z[14])
            {   w.push_back(0);
                z[25]--;
                z[4]--;
                z[17]--;
                z[14]--;
            }
            else if(z[22] && z[19] && z[14])
            {   z[22]--;
                z[19]--;
                w.push_back(2);
                z[14]--;
            }
            else if(z[20] && z[17] && z[14] && z[5])
            {   z[5]--;
                z[14]--;
                w.push_back(4);
                z[20]--;
                z[17]--;
            }
            else if(z[5] && z[8] && z[21] && z[4])
            {   z[5]--;
                w.push_back(5);
                z[8]--;
                z[21]--;
                z[4]--;
            }
            else if(z[18] && z[8] && z[23])
            {   z[18]--;
                z[8]--;
                w.push_back(6);
                z[23]--;
            }
            else if(z[18] && z[4]>1 && z[21] && z[13])
            {   z[18]--;
                z[4]-=2;
                z[21]--;
                w.push_back(7);
                z[13]--;
            }
            else if(z[4] && z[8] && z[6] && z[7] && z[19])
            {   z[4]--;
                z[8]--;
                z[6]--;
                z[7]--;
                w.push_back(8);
                z[19]--;
            }
            else if(z[13]>1 && z[8] && z[4])
            {   z[13]-=2;
                z[8]--;
                z[4]--;
                w.push_back(9);
            }
            else if(z[17] && z[4]>1 && z[19] && z[7])
            {   z[7]--;
                z[19]--;
                z[17]--;
                w.push_back(3);
                z[4]-=2;
            }
            else if(z[14] && z[13] && z[4])
            {   z[14]--;
                w.push_back(1);
                z[13]--;
                z[4]--;
            }
            for(i=0;i<26;++i)
            {    if(z[i]!=0)
                {    k=1;
                    break;
                }
                k=0;
            }
        }
        sort(w.begin(),w.end());
        for(i=0;i<w.size();i++)
            cout<<w[i];
        cout<<"\n";
    }
    return 0;
}
