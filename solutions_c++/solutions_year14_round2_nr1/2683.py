#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

int main()
{
    int T, tempi=0;
    cin>>T;
    for (int tempi = 0; tempi < T; ++tempi)
    {
        int N, j, count = 0;
        string s;
        cin>>N;
        string final = "%%";
        vector<vector<int> > finalcounts;
        vector<float> fcounts(101,0);
        
        for(j=0;j<N;j++) 
        {
            cin>>s;
            string s2 = s;
            string::iterator end = unique(s.begin(),s.end());
            s.erase(end, s.end());

            if(final == "%%" || final == s) {
                vector<int> counts(s.size(),0);
                final = s;
                int a=0,b=0;
                while(a<final.size() && b<s2.size()) {
                    if(final[a] == s2[b]) {
                        counts[a]++;
                        fcounts[a]++;
                        b++;
                    } else {
                        a++;
                    }
                }
                finalcounts.push_back(counts);
            } else {
                count = -1;
                break;
            }

        }

        for(int i=0;i<fcounts.size();i++) {
            fcounts[i] = floor(fcounts[i]/N + 0.5);
        }
        
        if(count == -1) {
            cout<<"Case #"<<tempi+1<<": Fegla won"<<endl;
        } else {
            for(int i=0;i<finalcounts.size();i++) {
                vector<int> tempcounts = finalcounts[i];
                for(int j=0;j<tempcounts.size();j++) {
                    count += abs(tempcounts[j] - fcounts[j]);
                }
            }

            cout<<"Case #"<<tempi+1<<": "<<count<<endl;
        }
        
        
        
    }
    return 0;
}