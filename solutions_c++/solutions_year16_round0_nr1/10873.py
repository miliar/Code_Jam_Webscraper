#include <iostream>
#include <string>
#include <cstdlib>
#include <sstream>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(0);
    int t;
    long long n;
    cin>>t;
    int g=t;

   while(t--) {
        cin>>n;
        if(n == 0) {
            cout<<"Case #"<< g-t << ": INSOMNIA" << endl;
            continue;
        }
        int k = n;

        bool tab[10];
        for(int i=0;i<10;i++)
            tab[i] = false;
        int ile = 0;

        while (true) {

            ostringstream ss;
            ss << k;
            string str = ss.str();

            for(int i = 0; i < str.size(); i++) {
                long long tmp = str[i] - 48;

                if(tab[tmp] == false) {
                    tab[tmp] = true;
                    ile++;
                }
            }

            if(ile == 10) {
                cout<<"Case #"<< g-t << ": "<<k << endl;
                break;
            }

            k += n;
        }



    }


    return 0;
}
