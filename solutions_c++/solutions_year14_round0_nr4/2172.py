#include <iostream>
#include <deque>
#include <algorithm>

using namespace std;

int main()
{
    int t;
    cin >> t;
    
    for(int tcase = 1; tcase <= t; ++tcase)
    {
        int n;
        cin >> n;
        
        deque<double> nblocks(n);
        deque<double> kblocks(n);
        
        for(int i = 0; i < n; ++i)
            cin >> nblocks[i];
            
        for(int i = 0; i < n; ++i)
            cin >> kblocks[i];
            
        sort(nblocks.begin(), nblocks.end());
        sort(kblocks.begin(), kblocks.end());
        
        deque<double> nblocksd = nblocks;
        deque<double> kblocksd = kblocks;
        
        // Deceitful War
        int dpoints = 0;
        for(int wn = n; wn > 0; --wn)
        {
            // Naomi chooses
            /*
            int i;
            for(i = 0; i < wn && nblocksd[i] < kblocksd.back(); ++i)
            {}
            double Cn, Tn;
            
            Cn = nblocksd[i % wn];
            
            if(wn == 1)
            {
                Tn = Cn;
            }
            else
            {
                Tn = (i%wn ? Cn : ((kblocksd[wn-1] + kblocksd[wn-2])/2));
            }*/
            
            double Cn, Tn;
            int i = 0;
            if(wn == 1)
            {
                Cn = Tn = nblocksd.front();
            }
            else if(nblocksd.front() < kblocksd.front())
            {
                Cn = nblocksd.front();
                Tn = ((kblocksd[wn-1] + kblocksd[wn-2])/2);
            }
            else
            {
                for(i = 0; i < wn && nblocksd[i] < kblocksd.back(); ++i)
                {}
                
                Cn = nblocksd[i % wn];
                Tn = ((kblocksd[wn-1] + kblocksd[wn-2])/2);
            }
            
            // Ken chooses
            int j;
            for(j = 0; j < wn && kblocksd[j] < Tn; ++j)
            {}
            
            double Ck = kblocksd[j % wn];
            
            if(Cn > Ck)
                ++dpoints;
            
            nblocksd.erase(nblocksd.begin() + (i%wn));
            kblocksd.erase(kblocksd.begin() + (j%wn));
        }
        
        // War
        int points = 0;
        for(int wn = n; wn > 0; --wn)
        {
            double Cn = nblocks.back();
            
            int j;
            for(j = 0; j < wn && kblocks[j] < Cn; ++j)
            {}
            
            double Ck = kblocks[j % wn];
            
            if(Cn > Ck)
                ++points;
            
            nblocks.pop_back();
            kblocks.erase(kblocks.begin() + (j%wn));
        }
        
        cout << "Case #" << tcase << ": " << dpoints << " " << points << endl;
    }
    
    return 0;
}
