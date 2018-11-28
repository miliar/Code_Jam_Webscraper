#include<iostream>
#include<map>
#include<set>
using namespace std;

int main(int argc, char *argv[]) {
	int caseNo=1, i, c, t;
	int map[10];
	long n, nn;
    bool allDigitsSeen, present;
    set<long> myset;
	cin>>t;
	while(t--) {
            // reset map
			for(i=0; i<10; i++) map[i] = 0;

            cin>>n;

            // multiplier
            c=1;
            present = false;
            allDigitsSeen=false;

            do {
                //cout<<"here\n";
                nn=n*c++;
                present = myset.find(nn) != myset.end();
                // if cycle of numbers, then break
                if(present) break;
                myset.insert(nn);
                while(nn) {
                    map[nn%10]++;
                    nn/=10;
                }
                allDigitsSeen = true;
                for(i=0; i<10; i++) {
                    //cout<<map[i]<<'\n';
                    if(map[i] == 0) allDigitsSeen=false;
                }
            } while(!allDigitsSeen);
            cout<<"Case #"<<caseNo++<<": ";
            if(present)
                cout<<"INSOMNIA\n";
            else
                cout<<n*(c-1)<<"\n";
//				cout<<i<<" => "<<map[i]<<'\n';
            myset.clear();

    }

	return 0;
}

