#include <fstream>
#include <iostream>
using namespace std;

int main()
{
    ifstream fin("war.in");
    ofstream fout("war.out");
    
    int t; fin >> t;
    for(int i=0; i<t; ++i) {
        fout << "Case #" << i+1 << ": ";
        //cout << "=========== Case #" << i+1 << " =============\n";
        double naomi[1005];
        double ken[1005];
        int n; fin >> n;
        for(int j=0; j<n; ++j) fin >> naomi[j];
        for(int j=0; j<n; ++j) fin >> ken[j];
        sort(naomi, naomi+n);
        sort(ken, ken+n);
        
        int war=0;
        int highest=n-1;
        int kvis[1005]; memset(kvis, 0, sizeof(kvis));
        //cout << "War: " << endl;
        for(int j=n-1; j>=0; --j) {
            // if Ken can beat Naomi
            if(naomi[j] < ken[highest]) {
                int k;
                //for(int x=0; x<n; ++x) cout << kvis[x] << ' '; cout << endl;
                for(k=0; k<n; ++k) {
                    if(kvis[k]) continue;
                    if(ken[k] > naomi[j]) break;
                }
                kvis[k]=1;
                //cout << "1Ken plays " << ken[k] << " when Naomi plays " << naomi[j] << endl;
                int x=n-1; highest=n-1;
                while(x>-1 && kvis[x]) {--x; --highest;}
            // otherwise there's no point in trying
            } else {
                int k=0;
                //for(int x=0; x<n; ++x) cout << kvis[x] << ' '; cout << endl;
                while(k<n && kvis[k]) ++k;
                kvis[k] = 1; ++war;
                //cout << "2Ken plays " << ken[k] << " when Naomi plays " << naomi[j] << endl;
                int x=n-1; highest=n-1;
                while(x>-1 && kvis[x]) {--x; --highest;}
            }
        }
        //cout << "======================\n";
        
        int nowar=0;
        highest=n-1;
        int lowest=0;
        for(int j=0; j<n; ++j) {
            // Naomi lies; she changes her lowest one to be ever so slightly
            // less than Ken's largest one
            // We know Ken always follows his strategy
            // So Ken will always play highest or lowest
            if(naomi[j] > ken[lowest]) {
                //cout << "2Ken plays " << ken[lowest] << " when Naomi plays " << naomi[j] << endl;
                ++nowar; ++lowest;
            } else if(naomi[j] < ken[highest]) {
                //cout << "1Ken plays " << ken[highest] << " when Naomi plays " << naomi[j] << endl;
                --highest;
            }
            //cout << highest << ' ' << lowest << endl;
        }
        fout << nowar << ' ' << war << endl;
    }
    //system("pause");
}
