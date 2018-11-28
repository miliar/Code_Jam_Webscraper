#include<iostream>
#include<algorithm>
#include<vector>

using namespace std;

// myMoteAfter = getMotesNeeded(myMote, mote, motesNeeded);
unsigned getMotesNeeded(unsigned current, unsigned goal, unsigned& numNeeded) {
    numNeeded = 0;
    return current;
}

int main() {
    unsigned cases;
    cin >> cases;
    
    unsigned N, mote, myMote;
    
    for (unsigned casen = 1; casen <= cases; casen++) {
        cin >> myMote >> N;
//        cout << "Case " << casen << ", myMote=" << myMote << ", N=" << N << endl;
        
        vector<unsigned> motes; // with added things
        vector<unsigned> allOps;
        unsigned ops = 0;
        for (unsigned n = 0; n < N; n++) {
            cin >> mote;
            motes.push_back(mote);
        }
        
        if (myMote == 1) {
            cout << "Case #" << casen << ": " << N << endl;
            continue;
        }
        
        sort(motes.begin(), motes.end());
        for (unsigned i = 0; i < N; i++) {
            mote = motes[i];
            // add all the motes needed
            while (mote >= myMote) {
                // add a mote of value myMote-1
                myMote += (myMote-1);
                ops++;
            }
            
            myMote += mote;
            allOps.push_back(ops);
        }
        // now we are finished with 'ops' operations ... 
//        cout << "The operations required:" << endl;
//        for (unsigned i = 0; i < N; i++) {
//            cout << allOps[i] << " " << endl;
//        }
        
        // see if removing things from the end is better
        unsigned bestOps = N; // remove all
        for (unsigned i = 0; i < N; i++) {
            int propOps = allOps[i] + (N-1-i);
            if (propOps < bestOps) {
                bestOps = propOps;
//                cout << "removing from " << i+1 << endl;
            }
        }
        
        cout << "Case #" << casen << ": " << bestOps << endl;
    }
}
