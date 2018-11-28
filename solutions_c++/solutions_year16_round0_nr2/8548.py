// Example program
#include <iostream>
#include <string>
using namespace std;
int main()
{
    int T;
    cin >> T;
    for (int i=0; i<T; i++) {
        char ins[1000];
        cin>> ins;

        int count = 0;
        for(int j=0; j<1000;j++) {

            if(ins[j+1] == '\0') {
                if(ins[j] == '-') {
                    count++;
                }
                cout<<"Case #"<<i+1<<": "<<count<<endl;
                break;
            }
            if(ins[j] != ins[j+1]) {

                count++;
            }
        }

    }
    return 0;
}

